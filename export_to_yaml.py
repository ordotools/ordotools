import yaml
from pathlib import Path
from importlib.machinery import SourceFileLoader
from models import DioceseOrdo, Feast

# Build a reverse lookup: Latin Name -> ID
trans_mod = SourceFileLoader("translations", "ordotools/tools/translations.py").load_module()
trans_data = trans_mod.Translations().easy_data
# We normalize the keys (lowercase, no periods) for better matching
NAME_TO_ID = {str(v.get('la', '')).lower().replace('.', ''): k for k, v in trans_data.items()}

class CleanDumper(yaml.SafeDumper):
    def write_line_break(self, data=None):
        super().write_line_break(data)
        if len(self.indents) == 2:
            super().write_line_break()

def migrate_propers(input_dir, output_dir):
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True, parents=True)

    for py_file in input_path.glob("*.py"):
        if py_file.name.startswith("_") or py_file.name in ["nameofcountry.py", "nameofdiocese.py"]:
            continue
            
        try:
            module = SourceFileLoader(py_file.stem, str(py_file)).load_module()
            instance = None
            for cls in ["Country", "Diocese", "Sanctoral", "Roman"]:
                if hasattr(module, cls):
                    instance = getattr(module, cls)(2025)
                    break
            if not instance: continue

            feasts_list = []
            for date_obj, details in instance.data.items():
                # 1. ATTEMPT ID LOOKUP:
                # Use provided ID, or try to match by Latin name
                raw_id = details.get("id")
                if not raw_id:
                    clean_name = str(details.get("feast", "")).lower().replace('.', '')
                    raw_id = NAME_TO_ID.get(clean_name)

                feast = Feast(
                    id=raw_id, # Can be None if lookup fails
                    name_translations={k: v for k, v in trans_data.get(raw_id, {}).items() if v} if raw_id else {},
                    date=date_obj.strftime("%m-%d"),
                    rank_verbose=details.get("rank", [0, "s"])[1],
                    rank_numeric=details.get("rank", [0, "s"])[0],
                    color=details.get("color", "white"),
                    mass_properties={k: v for k, v in details.get("mass", {}).items()},
                    nobility=[int(x) for x in details.get("nobility", []) if isinstance(x, (int, bool))]
                )
                # FIX: We NO LONGER use exclude_none=True so the 'id' key always exists
                feasts_list.append(feast.model_dump())

            final_data = {"diocese_name": instance.name, "country": getattr(instance, "country", "Universal"), "feasts": feasts_list}
            with open(output_path / f"{py_file.stem}.yaml", "w", encoding="utf-8") as yf:
                yaml.dump(final_data, yf, Dumper=CleanDumper, sort_keys=False, default_flow_style=False, allow_unicode=True)
            print(f"✅ Migrated {py_file.name}")

        except Exception as e:
            print(f"❌ Failed {py_file.name}: {e}")

if __name__ == "__main__":
    migrate_propers("ordotools/sanctoral/country", "data/countries")
    migrate_propers("ordotools/sanctoral/diocese", "data/dioceses")
