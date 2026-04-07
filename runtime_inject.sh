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
INJECT_PATH="/tmp/libtroonhook_inject.so"

if [ ! -f "$LIB_PATH" ]; then
    echo "Library not found: $LIB_PATH"
    exit 1
fi

# Copy library to /tmp for injection
cp "$LIB_PATH" "$INJECT_PATH"
chmod 644 "$INJECT_PATH"

# Create GDB script
cat > /tmp/inject.gdb << EOF
set \$dlopen = (void*(*)(char*, int)) dlopen
set \$lib = \$dlopen("$INJECT_PATH", 2)
printf "Injected: %p\\n", \$lib
if \$lib != 0
    printf "Injection successful!\\n"
else
    printf "Injection failed\\n"
end
detach
quit
EOF

echo "Injecting library..."
gdb -p $CS2_PID -x /tmp/inject.gdb --batch

echo "Injection complete. Check /tmp/troonhook.log for status."