#!/usr/bin/env python3
# Static offsets for CS2 bhop
# Source: https://github.com/a2x/cs2-dumper

import os

output_file = os.path.join(os.path.dirname(__file__), '..', 'include', 'offsets_values.h')

with open(output_file, 'w') as f:
    f.write("""#pragma once

// CS2 Button offsets
inline const struct {
    uintptr_t attack = 0x2066760;
    uintptr_t attack2 = 0x20667F0;
    uintptr_t back = 0x2066A30;
    uintptr_t duck = 0x2066D00;
    uintptr_t forward = 0x20669A0;
    uintptr_t jump = 0x2066C70;
    uintptr_t left = 0x2066AC0;
    uintptr_t lookatweapon = 0x231E250;
    uintptr_t reload = 0x20666D0;
    uintptr_t right = 0x2066B50;
    uintptr_t showscores = 0x231E130;
    uintptr_t sprint = 0x2066640;
    uintptr_t turnleft = 0x2066880;
    uintptr_t turnright = 0x2066910;
    uintptr_t use = 0x2066BE0;
    uintptr_t zoom = 0x231E1C0;
} client_offsets;
""")

print("✓ Offsets written to {}".format(output_file))