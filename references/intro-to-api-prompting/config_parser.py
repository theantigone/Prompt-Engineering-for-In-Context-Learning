"""
Parses a config file with sections and key-value pairs.
Each section starts with [SectionName]
Each key-value pair follows in the form: key=value
"""

def parse_config(filepath):
    config = {}
    current_section = None

    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if line.startswith("[") and line.endswith("]"):
                current_section = line[1:-1]
                config[current_section] = {}
            else:
                if current_section is None:
                    continue  # ❌ silently ignores keys before any section
                if '=' in line:
                    key, value = line.split('=')
                    config[current_section][key.strip()] = value.strip()
    return config

def main():
    config = parse_config("settings.cfg")
    print("Parsed Config:")
    for section, entries in config.items():
        print(f"[{section}]")
        for k, v in entries.items():
            print(f"{k} = {v}")
        print()

if __name__ == "__main__":
    main()