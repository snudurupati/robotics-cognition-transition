# Robot Brain Renaissance — Project (Nov 2025 kick-off)

**November = C++ fundamentals + ROS2 handshake.** No simulator. No new tools. One 2h deep-work block per weekday.

## November Objectives
1) `cpp-foundations/`: C++ toolchain, ownership, tests, concurrency with sanitizers.
2) `ros2-signal-pipeline/`: ROS2 pub/sub (rclpy), params, launch, rosbag record & analyze.

## Weekly Breakdown
- **W1:** CMake/Ninja/clang setup; RAII; 10 tests passing.
- **W2:** `unique_ptr`/rule of 0/5; ring buffer + CSV parser (+ tests).
- **W3:** threads/mutex/condvar; producer–consumer; sanitizer-clean run.
- **W4:** ROS2 install; sine publisher + RMS subscriber; launch; bag + analyzer.

## Success Criteria (Nov 30)
- `cpp-foundations/` builds, tests green, sanitizer-clean.
- `ros2-signal-pipeline/` runs launch, bag recorded, analyzer prints stats.
- Two short demo clips and tight READMEs.

## GitHub
```
git init && git add .
git commit -m "Kick-off: November C++ + ROS2 plan and scaffolds"
git branch -M main
git remote add origin <YOUR_REPO_URL>
git push -u origin main
```
