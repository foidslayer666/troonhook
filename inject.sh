#!/bin/bash

# CS2 Bhop Injector for Linux
# Handles paths with spaces correctly

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LIBRARY_PATH="$SCRIPT_DIR/build/libtroonhook.so"
CS2_PATH="/home/shk/.local/share/Steam/steamapps/common/Counter-Strike Global Offensive/game/cs2.sh"

# Check if library exists
if [[ ! -f "$LIBRARY_PATH" ]]; then
    echo "Error: libtroonhook.so not found at $LIBRARY_PATH"
    echo "Build the project first: mkdir build && cd build && cmake .. && make"
    exit 1
fi

# Check if CS2 script exists
if [[ ! -f "$CS2_PATH" ]]; then
    echo "Error: cs2.sh not found at $CS2_PATH"
    echo "Update CS2_PATH in this script to your CS2 installation"
    exit 1
fi

echo "Injection settings:"
echo "  Library: $LIBRARY_PATH"
echo "  CS2: $CS2_PATH"
echo ""
echo "Launching CS2 with bhop..."

# Export LD_PRELOAD and run CS2
export LD_PRELOAD="$LIBRARY_PATH"
exec "$CS2_PATH" "$@"
