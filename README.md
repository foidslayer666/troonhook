# troonhook

Internal CS2 bhop hack for Linux.

## Building

```bash
mkdir build && cd build && cmake .. && make
```

## Injection

### Method 1: Launch Wrapper Script (recommended)

1. Make the wrapper executable: `chmod +x launch_wrapper.sh`
2. Edit `launch_wrapper.sh` and update `TROONHOOK_LIB` to your libtroonhook.so path
3. In Steam, right-click CS2 > Properties > General > Launch Options
4. Add: `/home/shk/git/troonhook/launch_wrapper.sh %command%`
5. Launch CS2 from Steam

This ensures LD_PRELOAD is set in the game's environment.

### Method 2: Direct LD_PRELOAD (may not work)

In Steam launch options: `LD_PRELOAD="/path/to/libtroonhook.so"`

### Method 3: Inject script (advanced)

```bash
chmod +x inject.sh
./inject.sh
```

**Note:** Methods 2 & 3 may fail due to Steam's runtime.

## Offsets

Static CS2 offsets. Update `scripts/update_offsets.py` and rebuild if offsets change.

## Disclaimer

This may be detected by anti-cheat. Use at your own risk.