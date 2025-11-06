#include <chrono>
#include <iostream>
#include <thread>
int main(){
    using namespace std::chrono_literals;
    std::cout << "telemetry_sim starting..." << std::endl;
    std::this_thread::sleep_for(200ms);
    std::cout << "done." << std::endl;
    return 0;
}
