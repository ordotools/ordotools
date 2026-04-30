import yaml
import sys
import os

def transform_file(file_path):
    """
    Reads a YAML file, transforms the 'nobility' key from a multiline list
    to an inline list of strings (digits), and writes it back.
    """
    print(f"Processing file: {file_path}") # Debug print
    try:
        with open(file_path, 'r') as f:
            data = yaml.safe_load(f)
    except Exception as e:
        print(f"Error loading YAML file {file_path}: {e}", file=sys.stderr)
        return

    if not isinstance(data, dict) or 'nobility' not in data or not isinstance(data['nobility'], list):
        print(f"Skipping {file_path}: 'nobility' key not found or not a list.") # Debug print
        return

    original_nobility_list = data['nobility']
    print(f"Original nobility list in {file_path}: {original_nobility_list}") # Debug print
    transformed_nobility_list = []
    is_transformable = True

    for item in original_nobility_list:
        if isinstance(item, str) and item.startswith('- '):
            digit_str = item[2:].strip()
            if digit_str: # Ensure it's not empty after strip
                transformed_nobility_list.append(digit_str) # Append as string
            else:
                is_transformable = False
                break
        elif isinstance(item, int):
            transformed_nobility_list.append(str(item))
        elif isinstance(item, str):
            transformed_nobility_list.append(item)
        else:
            is_transformable = False
            break

    print(f"Transformed nobility list: {transformed_nobility_list}, Is transformable: {is_transformable}") # Debug print

    if is_transformable and transformed_nobility_list:
        data['nobility'] = transformed_nobility_list
        print(f"Data before dump in {file_path}: {data}") # Debug print
        try:
            with open(file_path, 'w') as f:
                yaml.dump(data, f, sort_keys=False, default_flow_style=True, indent=None)
            print(f"Successfully wrote to {file_path}") # Debug print
        except Exception as e:
            print(f"Error writing YAML file {file_path}: {e}", file=sys.stderr)
    else:
        print(f"Skipping write operation for {file_path} due to transformability or empty list.") # Debug print


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python transform_script.py <file1.yaml> <file2.yaml> ...", file=sys.stderr)
        sys.exit(1)

    for file_path in sys.argv[1:]:
        transform_file(file_path)

    print("Transformation process finished.")
