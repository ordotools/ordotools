import yaml
from pathlib import Path
from importlib.machinery import SourceFileLoader
from models import DioceseOrdo, Feast

# Mapping for cleaner YAML keys
MASS_KEY_MAP = {
    "int": "introit", "glo": "gloria", "cre": "credo", 
    "pre": "preface", "ora": "oration"
}

class CleanDumper(yaml.SafeDumper):
    def write_line_break(self, data=None):
        super().write_line_break(data)
        if len(self.indents) == 2:
            super().write_line_break()

def clean_mass_dict(d):
    """Recursively renames keys and preserves booleans."""
    if not isinstance(d, dict):
        return d
    if any(k in MASS_KEY_MAP for k in d.keys()):
        return {MASS_KEY_MAP.get(k, k): v for k, v in d.items()}
    return {k: clean_mass_dict(v) for k, v in d.items()}

def load_python_file(path):
    loader = SourceFileLoader(path.stem, str(path))
    return loader.load_module()

# Load translations
trans_mod = load_python_file(Path("ordotools/tools/translations.py"))
trans_data = trans_mod.Translations().easy_data

def migrate_propers(input_dir, output_dir):
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True, parents=True)

    for py_file in input_path.glob("*.py"):
        if py_file.name.startswith("_") or py_file.name in ["nameofcountry.py", "nameofdiocese.py"]:
            continue
            
        try:
            module = load_python_file(py_file)
            instance = None
            for class_name in ["Country", "Diocese", "Sanctoral", "Roman"]:
                if hasattr(module, class_name):
                    instance = getattr(module, class_name)(2025)
                    break
            if not instance: continue

            # FIX: Fallback if 'name' attribute is missing
            name = getattr(instance, "name", py_file.stem.capitalize())

            feasts_list = []
            for date_obj, details in instance.data.items():
                m_props = clean_mass_dict(details.get("mass"))
                alt_m_props = clean_mass_dict(details.get("alt_mass"))

                comms = []
                for c_name, c_data in details.get("com2", {}).items():
                    comms.append({
                        "name": c_name,
                        "mass_properties": clean_mass_dict(c_data.get("mass"))
                    })

                nobility_raw = details.get("nobility", [])
                nobility_ints = [int(x) if isinstance(x, (int, bool)) else 0 for x in nobility_raw]

                feast = Feast(
                    id=details.get("id"),
                    name_translations={k: v for k, v in trans_data.get(details.get("id"), {}).items() if v},
                    date=date_obj.strftime("%m-%d") if hasattr(date_obj, "strftime") else "00-00",
                    rank_verbose=details.get("rank", [0, "s"])[1] if len(details.get("rank", [])) > 1 else "s",
                    rank_numeric=details.get("rank", [0, "s"])[0],
                    color=details.get("color", "white"),
                    office_type=details.get("office_type"),
                    mass_properties=m_props,
                    alt_mass_properties=alt_m_props,
                    commemorations=comms,
                    nobility=nobility_ints  # [int(x) for x in details.get("nobility", []) if isinstance(x, (int, bool))]
                )
                feasts_list.append(feast.model_dump(exclude_none=True))

            final_data = {
                "diocese_name": name, 
                "country": getattr(instance, "country", "Universal"), 
                "feasts": feasts_list
            }
            
            with open(output_path / f"{py_file.stem}.yaml", "w", encoding="utf-8") as yf:
                yaml.dump(final_data, yf, Dumper=CleanDumper, sort_keys=False, default_flow_style=False, allow_unicode=True)
            print(f"✅ Exported {py_file.stem}.yaml")
        except Exception as e:
            print(f"❌ Failed {py_file.name}: {e}")

if __name__ == "__main__":
    migrate_propers("ordotools/sanctoral/country", "data/countries")
    migrate_propers("ordotools/sanctoral/diocese", "data/dioceses")
