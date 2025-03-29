import csv
import json
from ordotools.tools.temporal_data import TemporalData

data = TemporalData().data

flattened_data = []

# Collect all field names
fieldnames = set()
mass_keys = set()
vespers_keys = set()

for entry in data.values():
    for key, val in entry.items():
        if key == "mass":
            for subkey in val:
                mass_keys.add(f"mass_{subkey}")
        elif key == "vespers":
            for subkey in val:
                if subkey != "admag":
                    vespers_keys.add(f"vespers_{subkey}")
        elif key != "rank":
            fieldnames.add(key)

fieldnames -= {"mass", "vespers"}
fieldnames.add("id")

# Final headers
final_headers = (
    ["id"]
    + sorted(fieldnames - {"id"})
    + ["rank_numeric", "rank_verbose"]
    + sorted(mass_keys)
    + sorted(vespers_keys)
    + ["vespers_admag_1", "vespers_admag_2"]
)

# Flatten entries
for entry in data.values():
    row = {}

    # Main fields
    for key in final_headers:
        if key == "rank_numeric":
            rank = entry.get("rank", [])
            row[key] = rank[0] if len(rank) > 0 else ""
        elif key == "rank_verbose":
            rank = entry.get("rank", [])
            row[key] = rank[1] if len(rank) > 1 else ""
        elif key.startswith("mass_"):
            subkey = key.split("_", 1)[1]
            val = entry.get("mass", {}).get(subkey, "")
            row[key] = "" if val == {} else val
        elif key.startswith("vespers_") and not key.startswith("vespers_admag"):
            subkey = key.split("_", 1)[1]
            val = entry.get("vespers", {}).get(subkey, "")
            if val == {}:
                row[key] = ""
            else:
                row[key] = json.dumps(val) if isinstance(val, (dict, list)) else val
        elif key == "vespers_admag_1":
            val = entry.get("vespers", {}).get("admag", [])
            row[key] = val[0] if len(val) > 0 else ""
        elif key == "vespers_admag_2":
            val = entry.get("vespers", {}).get("admag", [])
            row[key] = val[1] if len(val) > 1 else ""
        elif key in ["com_1", "com_2", "com_3"]:
            val = entry.get(key, "")
            if val == {}:
                row[key] = ""
            elif isinstance(val, dict) and set(val.keys()) == {"oration"}:
                row[key] = val["oration"]
            else:
                row[key] = json.dumps(val)
        else:
            val = entry.get(key, "")
            if val == {}:
                row[key] = ""
            else:
                row[key] = json.dumps(val) if isinstance(val, (dict, list, tuple)) else val

    flattened_data.append(row)

# Write to CSV
with open("output.csv", mode="w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=final_headers)
    writer.writeheader()
    writer.writerows(flattened_data)
