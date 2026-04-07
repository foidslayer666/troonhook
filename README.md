# troonhook

Internal for linux

## Building

1. Update offsets: `python3 scripts/update_offsets.py`

2. Build: `mkdir build && cd build && cmake .. && make`

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

## Offsets

Offsets are auto-fetched from https://github.com/a2x/cs2-dumper