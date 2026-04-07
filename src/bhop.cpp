#include <iostream>
#include <thread>
#include <chrono>
#include <fstream>
#include <string>
#include <X11/Xlib.h>
#include <X11/keysym.h>
#include "offsets.h"

std::ofstream log_file("/tmp/troonhook.log", std::ios::app);

uintptr_t getBaseAddress(const char* moduleName) {
    log_file << "Looking for module: " << moduleName << std::endl;
    std::ifstream maps("/proc/self/maps");
    std::string line;
    while (std::getline(maps, line)) {
        if (line.find(moduleName) != std::string::npos && line.find("r-xp") != std::string::npos) {
            log_file << "Found line: " << line << std::endl;
            size_t pos = line.find('-');
            if (pos != std::string::npos) {
                std::string addr = line.substr(0, pos);
                uintptr_t base = std::stoull(addr, nullptr, 16);
                log_file << "Base address for " << moduleName << ": 0x" << std::hex << base << std::endl;
                return base;
            }
        }
    }
    log_file << "Module " << moduleName << " not found" << std::endl;
    return 0;
}

bool isSpacePressed() {
    Display* display = XOpenDisplay(NULL);
    if (!display) {
        log_file << "Failed to open X display" << std::endl;
        return false;
    }
    KeyCode keycode = XKeysymToKeycode(display, XK_space);
    char keys[32];
    XQueryKeymap(display, keys);
    XCloseDisplay(display);
    bool pressed = keys[keycode / 8] & (1 << (keycode % 8));
    if (pressed) log_file << "Space pressed" << std::endl;
    return pressed;
}

void bhop() {
    log_file << "Bhop thread started" << std::endl;
    uintptr_t base = getBaseAddress("libclient.so");
    if (!base) {
        base = getBaseAddress("client_client.so");
    }
    if (!base) {
        log_file << "Failed to find client library base" << std::endl;
        return;
    }
    
    log_file << "Using base: 0x" << std::hex << base << std::endl;
    log_file << "Jump offset: 0x" << std::hex << client_offsets.jump << std::endl;
    
    while (true) {
        if (isSpacePressed()) {
            *(int*)(base + client_offsets.jump) = 5;  // Hold jump
            log_file << "Jump held" << std::endl;
        } else {
            *(int*)(base + client_offsets.jump) = 4;  // Release jump
        }
        std::this_thread::sleep_for(std::chrono::milliseconds(1));
    }
}

__attribute__((constructor)) void init() {
    log_file << "Troonhook library loaded" << std::endl;
    std::thread t(bhop);
    t.detach();
}