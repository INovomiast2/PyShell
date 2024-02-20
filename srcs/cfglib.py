import re

def parse_config_file(file_path, encoding="utf-8"):
    """
    Parses a configuration file with the specified format, extracting and
    returning a dictionary where keys are section names and values are
    dictionaries of configuration parameters.

    Args:
        file_path (str): Path to the configuration file.
        encoding (str, optional): Encoding of the file. Defaults to "utf-8".

    Returns:
        dict: A dictionary containing parsed configuration data.

    Raises:
        ValueError: If the file format is invalid or unexpected.
    """

    config = {}
    current_section = None
    param_name = None

    try:
        with open(file_path, "r", encoding=encoding) as f:
            for line in f:
                line = line.strip()

                # Start of a new section
                if line.startswith("{") and line.endswith("}"):
                    if current_section is not None:
                        raise ValueError(f"Unclosed section: {current_section}")
                    current_section = line.strip("{ }")
                    config[current_section] = {}
                    param_name = None
                elif current_section is None:
                    raise ValueError(f"Section name missing before line: {line}")

                # Parameter definition
                elif line.startswith("CONFIG_PARAM:"):
                    param_name = line.split(":", 1)[0].strip()
                    value = line.split(":", 1)[1].strip()
                    config[current_section][param_name] = value
                elif param_name is not None:
                    # Handle values without `CONFIG_PARAM` prefix
                    config[current_section][param_name] += line.strip()
                else:
                    raise ValueError(f"Invalid line format: {line}")

                # Section separator
                if line.startswith("|-###############################-|"):
                    current_section = None
                    param_name = None

            # Check for unclosed section at the end
            if current_section is not None:
                raise ValueError(f"Unclosed section: {current_section}")

    except IOError as e:
        raise IOError(f"Error opening file: {e}") from e

    return config

if __name__ == "__main__":
    file_path = "../cfg/cfgTest.pyshc"
    encoding = "utf-8"  # Adjust if needed

    config = parse_config_file(file_path, encoding)
    print(config)
