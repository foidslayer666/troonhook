#!/usr/bin/env python3
# Static offsets for CS2 bhop
# Source: https://github.com/a2x/cs2-dumper

import os

output_file = os.path.join(os.path.dirname(__file__), '..', 'include', 'offsets_values.h')

with open(output_file, 'w') as f:
    f.write("""#pragma once

// CS2 offsets
inline const struct {
    uintptr_t dwLocalPlayer = 0x17C0F08;
    uintptr_t dwForceJump = 0x1721A70;
    uintptr_t m_fFlags = 0x3C;
    uintptr_t m_iHealth = 0x32C;
} client_offsets;
""")

print("✓ Offsets written to {}".format(output_file))