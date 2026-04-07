import json
import urllib.request
import os

url = "https://raw.githubusercontent.com/a2x/cs2-dumper/main/generated/offsets.json"
output_file = os.path.join(os.path.dirname(__file__), '..', 'include', 'offsets_values.h')

try:
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())
    
    client_offsets = data.get("client.dll", {})
    
    with open(output_file, 'w') as f:
        f.write("#pragma once\n\n")
        f.write("inline const struct {\n")
        for key, value in client_offsets.items():
            if isinstance(value, int):
                f.write(f"    uintptr_t {key} = 0x{value:X};\n")
            else:
                f.write(f"    // {key}: {value}\n")
        f.write("} client_offsets;\n")
        
    print(f"Offsets updated in {output_file}")
except Exception as e:
    print(f"Error updating offsets: {e}")