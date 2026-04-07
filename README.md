# troonhook

Internal CS2 bhop hack for Linux.

## Building

1. Offsets are kept up-to-date automatically via CI, but you can manually update: `python3 scripts/update_offsets.py`

2. Build: `mkdir build && cd build && cmake .. && make`

## Offsets

Offsets are **automatically updated** via GitHub Actions (runs every 6 hours). The update process tries:

1. **Hazedumper API** (fast, online service)
2. **cs2-dumper generation locally** (clones repo, runs generate.py)
3. **Local cache** (fallback if network fails)
4. **Dummy offsets** (only if everything fails)

To manually update locally: `python3 scripts/update_offsets.py`

The workflow automatically commits updates to `include/offsets_values.h` when offsets change.

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