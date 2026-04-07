#include <iostream>
#include <thread>
#include <chrono>
#include <fstream>
#include <string>
#include <X11/Xlib.h>
#include <X11/keysym.h>
#include "offsets.h"

uintptr_t getBaseAddress(const char* moduleName) {
    std::ifstream maps("/proc/self/maps");
    std::string line;
    while (std::getline(maps, line)) {
        if (line.find(moduleName) != std::string::npos) {
            size_t pos = line.find('-');
            if (pos != std::string::npos) {
                std::string addr = line.substr(0, pos);
                return std::stoull(addr, nullptr, 16);
            }
        }
    }
    return 0;
}

bool isSpacePressed() {
    Display* display = XOpenDisplay(NULL);
    if (!display) return false;
    KeyCode keycode = XKeysymToKeycode(display, XK_space);
    char keys[32];
    XQueryKeymap(display, keys);
    XCloseDisplay(display);
    return keys[keycode / 8] & (1 << (keycode % 8));
}

void bhop() {
    uintptr_t base = getBaseAddress("client_client.so");
    if (!base) {
        std::cout << "Failed to find client_client.so base" << std::endl;
        return;
    }
    while (true) {
        if (isSpacePressed()) {
            // Trigger jump using the jump offset
            *(int*)(base + client_offsets.jump) = 5;
            std::this_thread::sleep_for(std::chrono::milliseconds(10));
            *(int*)(base + client_offsets.jump) = 4;
        }
        std::this_thread::sleep_for(std::chrono::milliseconds(1));
    }
}

__attribute__((constructor)) void init() {
    std::thread t(bhop);
    t.detach();
}