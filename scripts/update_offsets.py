import json
import os
import subprocess
import tempfile
import urllib.request
import urllib.error
from datetime import datetime

output_file = os.path.join(os.path.dirname(__file__), '..', 'include', 'offsets_values.h')
cache_file = os.path.join(os.path.dirname(__file__), '..', '.offsets_cache.json')

def hazedumper_api():
    """Try hazedumper online service directly"""
    try:
        print("Trying hazedumper API...")
        with urllib.request.urlopen('https://hazedumper.github.io/offsets.json', timeout=5) as response:
            data = json.loads(response.read().decode())
        if 'client.dll' in data:
            print("✓ Hazedumper API successful")
            return data
    except Exception as e:
        print(f"✗ Hazedumper API failed: {e}")
    return None

def cs2dumper_generation():
    """Clone cs2-dumper repo and run generate.py"""
    with tempfile.TemporaryDirectory() as temp_dir:
        repo_dir = os.path.join(temp_dir, 'cs2-dumper')
        try:
            print("Trying cs2-dumper generation...")
            subprocess.run(['git', 'clone', '--depth', '1', 'https://github.com/a2x/cs2-dumper.git', repo_dir], 
                         check=True, capture_output=True, timeout=30)
            subprocess.run(['pip', 'install', '-q', '-r', os.path.join(repo_dir, 'requirements.txt')], 
                         check=True, capture_output=True, timeout=60)
            subprocess.run(['python', os.path.join(repo_dir, 'generate.py')], 
                         check=True, capture_output=True, cwd=repo_dir, timeout=60)
            with open(os.path.join(repo_dir, 'generated', 'offsets.json'), 'r') as f:
                data = json.load(f)
            if 'client.dll' in data:
                print("✓ cs2-dumper generation successful")
                return data
        except subprocess.TimeoutExpired:
            print("✗ cs2-dumper generation timed out")
        except Exception as e:
            print(f"✗ cs2-dumper generation failed: {e}")
    return None

def load_cache():
    """Load offsets from cache if available"""
    if os.path.exists(cache_file):
        try:
            with open(cache_file, 'r') as f:
                return json.load(f)
        except:
            pass
    return None

def save_cache(data):
    """Save offsets to cache"""
    try:
        with open(cache_file, 'w') as f:
            json.dump(data, f)
    except:
        pass

def write_offsets(data):
    """Write offsets to C++ header"""
    client_offsets = data.get("client.dll", {})
    with open(output_file, 'w') as f:
        f.write("#pragma once\n\n")
        f.write("// Auto-generated offsets from cs2-dumper\n")
        f.write(f"// Last updated: {datetime.now()}\n\n")
        f.write("inline const struct {\n")
        for key, value in client_offsets.items():
            if isinstance(value, int):
                f.write(f"    uintptr_t {key} = 0x{value:X};\n")
            else:
                f.write(f"    // {key}: {value}\n")
        f.write("} client_offsets;\n")

try:
    data = hazedumper_api()
    
    if not data:
        data = cs2dumper_generation()
    
    if not data:
        data = load_cache()
        if data:
            print("✓ Using cached offsets")
        else:
            raise Exception("All methods failed and no cache available")
    
    if data:
        write_offsets(data)
        save_cache(data)
        print(f"✓ Offsets written to {output_file}")
    
except Exception as e:
    print(f"✗ Error updating offsets: {e}")
    cached_data = load_cache()
    if cached_data:
        print("Using cached offsets as fallback")
        write_offsets(cached_data)
    else:
        print("Creating dummy offsets")
        with open(output_file, 'w') as f:
            f.write("#pragma once\n\n")
            f.write("// PLACEHOLDER - Update with real offsets\n")
            f.write("inline const struct {\n")
            f.write("    uintptr_t dwLocalPlayer = 0xDEADBEEF;\n")
            f.write("    uintptr_t dwForceJump = 0xDEADBEEF;\n")
            f.write("    uintptr_t m_fFlags = 0xDEADBEEF;\n")
            f.write("    uintptr_t m_iHealth = 0xDEADBEEF;\n")
            f.write("} client_offsets;\n")