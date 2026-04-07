#!/bin/bash
# CS2 Launch Wrapper for Injection

# Set the library path here
TROONHOOK_LIB="/home/shk/git/troonhook/build/libtroonhook.so"

if [ ! -f "$TROONHOOK_LIB" ]; then
    echo "Error: $TROONHOOK_LIB not found"
    exit 1
fi

echo "Injecting troonhook..."
export LD_PRELOAD="$TROONHOOK_LIB"

# Execute the actual game command
exec "$@"