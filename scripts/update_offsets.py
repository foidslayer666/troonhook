import json
import urllib.request
import base64
import os

url = "https://api.github.com/repos/a2x/cs2-dumper/contents/generated/offsets.json"
output_file = os.path.join(os.path.dirname(__file__), '..', 'include', 'offsets_values.h')

try:
    with urllib.request.urlopen(url) as response:
        api_data = json.loads(response.read().decode())
    
    content = base64.b64decode(api_data['content']).decode()
    data = json.loads(content)
    
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
    # Create dummy file
    with open(output_file, 'w') as f:
        f.write("#pragma once\n\n")
        f.write("inline const struct {\n")
        f.write("    uintptr_t dwLocalPlayer = 0xDEADBEEF;\n")
        f.write("    uintptr_t dwForceJump = 0xDEADBEEF;\n")
        f.write("    uintptr_t m_fFlags = 0xDEADBEEF;\n")
        f.write("    uintptr_t m_iHealth = 0xDEADBEEF;\n")
        f.write("} client_offsets;\n")
    print(f"Created dummy offsets file: {output_file}")