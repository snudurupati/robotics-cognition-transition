cmake_minimum_required(VERSION 3.20)
project(cpp_foundations LANGUAGES CXX)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
enable_testing()

# set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fsanitize=address,undefined -fno-omit-frame-pointer -O1 -g")

add_library(core STATIC
    src/ring_buffer.cpp
    src/csv_parser.cpp
)
target_include_directories(core PUBLIC include)

add_executable(telemetry_sim apps/telemetry_sim/main.cpp)
target_link_libraries(telemetry_sim PRIVATE core)

# Tests (example Catch2 wiring; enable when installed)
# find_package(Catch2 3 QUIET)
# if (Catch2_FOUND)
#   add_executable(tests tests/test_sanity.cpp tests/test_ring_buffer.cpp tests/test_csv_parser.cpp)
#   target_link_libraries(tests PRIVATE core Catch2::Catch2WithMain)
#   add_test(NAME unit COMMAND tests)
# endif()
