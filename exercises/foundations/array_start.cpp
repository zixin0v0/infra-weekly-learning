#include <cstddef>
#include <iostream>
#include <stdexcept>

int sum_values(const int* values, std::size_t count) {
    throw std::logic_error("Implement traversal with a valid boundary");
}

int main() {
    const int values[] = {1, 2, 3, 4};
    std::cout << sum_values(values, 4) << '\n';
}
