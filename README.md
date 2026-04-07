# troonhook

Internal CS2 bhop hack for Linux.

## Building

```bash
mkdir build && cd build && cmake .. && make
```

## Injection

### Method 1: Steam Launch Options (recommended)

1. In Steam, right-click Counter-Strike 2 > Properties
2. Go to General > Launch Options
3. Add: `LD_PRELOAD="/path/to/troonhook/build/libtroonhook.so"`
4. Replace `/path/to/troonhook` with your actual troonhook directory path
5. Launch CS2 from Steam

This injects the library into the actual game process.

### Method 2: Using the inject script (advanced)

From the project root directory:

```bash
chmod +x inject.sh
./inject.sh
```

**Note:** This method may not work due to Steam's runtime environment. Use Method 1 for best results.

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