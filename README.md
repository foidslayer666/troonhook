# troonhook

Internal CS2 bhop hack for Linux.

## Building

```bash
mkdir build && cd build && cmake .. && make
```

## Injection

### Method 1: Runtime Injector (recommended)

This injects the library into a running CS2 process.

1. Start CS2 normally
2. Run: `chmod +x runtime_inject.sh && ./runtime_inject.sh`
3. The library will be injected and bhop will work

### Method 2: Launch Wrapper Script

1. Make executable: `chmod +x launch_wrapper.sh`
2. Edit `TROONHOOK_LIB` path in the script
3. In Steam launch options: `/path/to/launch_wrapper.sh %command%`

### Method 3: Direct LD_PRELOAD

In Steam launch options: `LD_PRELOAD="/path/to/libtroonhook.so"`

## Offsets

Updated to use standard CS2 offsets (dwForceJump, dwLocalPlayer, etc.) for proper bhop functionality. Offsets may need updating for new game versions.

## Disclaimer

This may be detected by anti-cheat. Use at your own risk.