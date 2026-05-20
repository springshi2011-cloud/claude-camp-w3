#load config.jason and return the config as a dict
import json         

def load_config(filename="config.json"):
    with open(filename, "r") as config_file:
        config = json.load(config_file)
    return config

#display current settings
def display_config(config):
    print("Current Configuration:")
    for key, value in config.items():
        print(f"{key}: {value}")                


def validate_font_size(size):
    try:
        size_int = int(size)
        if 8 <= size_int <= 32:
            return size_int
       
    except ValueError:
       pass
    
    return None

#let user modify settings
def modify_config(config):
    print("\nModify Configuration (leave blank to keep current value):")
    for key in config.keys():
        new_value = input(f"{key} (current: {config[key]}): ")
        if new_value.strip() == "":
            continue

        if key == "font_size":
            validated_size = validate_font_size(new_value)
            if validated_size is not None:
                config[key] = validated_size
            else:
                print(f"Invalid font size '{new_value}'. Keeping current value: {config[key]}")
        else:
            config[key] = new_value.strip()
    return config

def save_config(config, filename="config.json"):
    with open(filename, "w") as config_file:
        json.dump(config, config_file, indent=4)



#main function to load and display config
def main():
    config = load_config()
    display_config(config) 
       
    modified_config = modify_config(config)

    save_config(modified_config)
    print("\nConfiguration updated and saved.")                


if __name__ == "__main__":  
    main()
