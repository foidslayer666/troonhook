# troonhook

Internal CS2 bhop hack for Linux.

## Building

1. From the project root, update offsets: `python3 scripts/update_offsets.py`

2. Build: `mkdir build && cd build && cmake .. && make`

## Offsets

Offsets are auto-fetched from https://github.com/a2x/cs2-dumper. If the online file is unavailable, the script clones the repo, generates offsets locally using hazedumper, and uses those. Requires git, pip, and internet access. If all fails, dummy offsets are created. Manually update `include/offsets_values.h` if needed.

## Injection

To inject, use LD_PRELOAD.

Create a script:

```bash
#!/bin/bash
export LD_PRELOAD=/path/to/libtroonhook.so
/path/to/cs2.sh
```

Or modify steam launch options to include LD_PRELOAD.

Note: This may be detected by anti-cheat. Use at your own risk.
```

Or modify steam launch options to include LD_PRELOAD.

Note: This may be detected by anti-cheat. Use at your own risk.

## Offsets

Offsets are auto-fetched from https://github.com/a2x/cs2-dumper