import yaml
from pathlib import Path
from importlib.machinery import SourceFileLoader
from models import Feast # Reusing the refined Pydantic model

# Mapping for cleaner YAML keys
MASS_KEY_MAP = {
    "int": "introit", "glo": "gloria", "cre": "credo", 
    "pre": "preface", "ora": "oration", "seq": "sequence"
}

class CleanDumper(yaml.SafeDumper):
    """Custom dumper to add spacing between feasts for Neovim readability."""
    def write_line_break(self, data=None):
        super().write_line_break(data)
        if len(self.indents) == 2:
            super().write_line_break()

def clean_mass_dict(d):
    """Recursively renames keys and preserves booleans."""
    if not isinstance(d, dict): return d
    if any(k in MASS_KEY_MAP for k in d.keys()):
        return {MASS_KEY_MAP.get(k, k): v for k, v in d.items()}
    return {k: clean_mass_dict(v) for k, v in d.items()}

def load_python_file(path):
    loader = SourceFileLoader(path.stem, str(path))
    return loader.load_module()

def migrate_temporal(py_path, output_dir="data/temporal"):
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True, parents=True)

    # Load Python source and translations
    module = load_python_file(Path(py_path))
    trans_mod = load_python_file(Path("ordotools/tools/translations.py"))
    trans_data = trans_mod.Translations().data
    
    temporal_instance = module.TemporalData()
    feasts_list = []

    for t_id, details in temporal_instance.data.items():
        m_props = clean_mass_dict(details.get("mass"))
        
        # Pull translations
        names = trans_data.get(t_id, {})
        if isinstance(names, dict):
            name_translations = {k: v for k, v in names.items() if v}
        else:
            name_translations = {"la": str(names)}

        # Create the feast object
        feast = Feast(
            id=None, # We will manually set this to the string ID below
            name_translations=name_translations,
            date="00-00", 
            rank_verbose=details.get("rank", [0, "s"])[1],
            rank_numeric=details.get("rank", [0, "s"])[0],
            color=details.get("color", "white"),
            office_type=details.get("office_type"),
            mass_properties=m_props,
            nobility=[int(x) for x in details.get("nobility", [])]
        )
        
        # Merge the string ID into the standard 'id' field
        feast_dict = feast.model_dump(exclude_none=True)
        feast_dict["id"] = t_id 
        
        # Move 'id' to the top of the dictionary for better readability
        ordered_feast = {"id": feast_dict.pop("id")}
        ordered_feast.update(feast_dict)
        
        feasts_list.append(ordered_feast)

    # Save to YAML with the requested spacing
    with open(output_path / "temporal_cycle.yaml", "w", encoding="utf-8") as yf:
        yaml.dump(
            {"cycle": "Temporal", "feasts": feasts_list}, 
            yf, 
            Dumper=CleanDumper, 
            sort_keys=False, 
            default_flow_style=False, 
            allow_unicode=True
        )
    print(f"✅ Exported temporal_cycle.yaml with unified 'id' field.")

if __name__ == "__main__":
    migrate_temporal("ordotools/tools/temporal_data.py")
