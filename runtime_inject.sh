#!/bin/bash
# CS2 Runtime Injector using GDB

# Find CS2 process
CS2_PID=$(pgrep -f "cs2" | head -1)

if [ -z "$CS2_PID" ]; then
    echo "CS2 process not found. Start CS2 first."
    exit 1
fi

echo "Found CS2 PID: $CS2_PID"

# Library path
LIB_PATH="/home/shk/git/troonhook/build/libtroonhook.so"

if [ ! -f "$LIB_PATH" ]; then
    echo "Library not found: $LIB_PATH"
    exit 1
fi

# Create GDB script
cat > /tmp/inject.gdb << EOF
set \$dlopen = (void*(*)(char*, int)) dlopen
set \$lib = \$dlopen("$LIB_PATH", 2)
printf "Injected: %p\\n", \$lib
detach
quit
EOF

echo "Injecting library..."
gdb -p $CS2_PID -x /tmp/inject.gdb --batch

echo "Injection complete. Check /tmp/troonhook.log for status."