cmake_minimum_required(VERSION 3.10)
project(troonhook)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_BUILD_TYPE Release)

add_custom_target(update_offsets COMMAND python3 ${CMAKE_SOURCE_DIR}/scripts/update_offsets.py)

add_library(troonhook SHARED src/bhop.cpp)

add_dependencies(troonhook update_offsets)

target_include_directories(troonhook PRIVATE include)

find_package(Threads REQUIRED)
target_link_libraries(troonhook Threads::Threads X11)