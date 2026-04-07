# troonhook

Internal CS2 bhop hack for Linux.

## Building

```bash
mkdir build && cd build && cmake .. && make
```

## Injection

### Method 1: Using the inject script (recommended)

```bash
chmod +x inject.sh
./inject.sh
```

The script handles paths with spaces correctly and automatically finds the compiled library.

### Method 2: Manual LD_PRELOAD

```bash
export LD_PRELOAD="$(pwd)/build/libtroonhook.so"
/path/to/cs2.sh
```

### Method 3: Steam launch options

Add to CS2 launch options in Steam:
```
LD_PRELOAD="$(pwd)/build/libtroonhook.so" %command%
```

**Note:** Update `CS2_PATH` in `inject.sh` if your installation is in a different location.

## Offsets

Static CS2 offsets. Update `scripts/update_offsets.py` and rebuild if offsets change.

## Disclaimer

This may be detected by anti-cheat. Use at your own risk.