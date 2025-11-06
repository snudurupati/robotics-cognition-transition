# cpp-foundations
Modern C++ practice for November. Tooling: clang + CMake + Ninja (WSL2). Tests: Catch2 or GoogleTest.

## Build & Test
```
cmake -S . -B build -G Ninja -DCMAKE_CXX_COMPILER=clang++ -DCMAKE_BUILD_TYPE=Debug
cmake --build build
ctest --test-dir build --output-on-failure
```

## Sanitizers (Week 3)
Add to CMake CXX flags: `-fsanitize=address,undefined -fno-omit-frame-pointer -O1 -g`

## Install deps
- Catch2: `sudo apt install catch2`
- GoogleTest: `sudo apt install libgtest-dev` (or FetchContent)

## Layout
- include/ — headers
- src/ — libs
- apps/telemetry_sim — Week 3 example
- tests/ — unit tests
