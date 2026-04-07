import json
import urllib.request
import base64
import os
import subprocess
import tempfile
import shutil

output_file = os.path.join(os.path.dirname(__file__), '..', 'include', 'offsets_values.h')

def fetch_via_api():
    url = "https://api.github.com/repos/a2x/cs2-dumper/contents/generated/offsets.json"
    try:
        with urllib.request.urlopen(url) as response:
            api_data = json.loads(response.read().decode())
        content = base64.b64decode(api_data['content']).decode()
        return json.loads(content)
    except:
        return None

def generate_locally():
    with tempfile.TemporaryDirectory() as temp_dir:
        repo_dir = os.path.join(temp_dir, 'cs2-dumper')
        try:
            # Clone the repo
            subprocess.run(['git', 'clone', 'https://github.com/a2x/cs2-dumper.git', repo_dir], check=True, capture_output=True)
            # Install requirements
            subprocess.run(['pip', 'install', '-r', os.path.join(repo_dir, 'requirements.txt')], check=True, capture_output=True)
            # Run generate.py
            subprocess.run(['python', os.path.join(repo_dir, 'generate.py')], check=True, capture_output=True, cwd=repo_dir)
            # Read the generated file
            with open(os.path.join(repo_dir, 'generated', 'offsets.json'), 'r') as f:
                return json.load(f)
        except subprocess.CalledProcessError as e:
            print(f"Error generating offsets locally: {e}")
            return None

try:
    data = fetch_via_api()
    if not data:
        print("API fetch failed, trying local generation...")
        data = generate_locally()
    
    if data:
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
    else:
        raise Exception("All methods failed")
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