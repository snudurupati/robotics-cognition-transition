#pragma once
#include <vector>
#include <optional>
template<typename T>
class RingBuffer {
public:
    explicit RingBuffer(size_t capacity);
    bool enqueue(const T& value);
    std::optional<T> dequeue();
    bool empty() const noexcept;
    bool full() const noexcept;
    size_t size() const noexcept;
    size_t capacity() const noexcept;
private:
    std::vector<T> data_;
    size_t head_{0}, tail_{0}, count_{0};
};
