#include "Memory.hpp"

int main()
{
    Memory mem;
    std::vector<unsigned short> numbers = {255,6212,2341,23421,7593,20,1234,8139,50000,1};
    for (uint8_t i = 0; i < numbers.size(); i++)
    {
        mem.insert(numbers[i]);
    }
    unsigned short lowerLimit = 500;
    unsigned short upperLimit = 50000;
    std::cout << "Memory:\n" << mem << '\n';
    std::cout << "Words between " << mem.toBinary(lowerLimit) << " and " << mem.toBinary(upperLimit) << '\n';
    std::cout << mem.getElementsInInterval(lowerLimit,upperLimit) << '\n';
    mem.sort(0);
    std::cout << "Descending sort:\n" << mem << '\n';
    mem.sort(1);
    std::cout << "Sorted ascending:\n" << mem;
    return 0;
}