//Second variant
//f2 (Completed)
//f7 (Completed)
//f8 (Completed)
//f13 (Completed)
//find values in interval (Completed)
//sum Aj and Bj in words Sj, which has similiar Vj to V=000-111 (Completed)
#include "Memory.hpp"
#include <ctime>

int main()
{
    Memory memory;
    std::vector<bool> V = {0,1,1};
    std::srand(std::time(0));
    for (int i = 0; i < 16; i++)
    {
        memory.Write(memory.getRandomWord(), i);  
    }
    std::cout << "Memory:\n" << memory << DIVIDER;
    std::cout << "Address 0x04 Word:  " << memory.Read(0x04) << DIVIDER;
    std::cout << "Normal matrix of memory:\n" << memory.getNormalMatrix() << DIVIDER;
    std::cout << "Diagonal matrix of memory from normal matrix:\n" << memory.getDiagonalMatrix(memory.getNormalMatrix()) << DIVIDER;
    memory.sum(V);
    std::cout << "Memory after sum(Diagonal view)"<< "(For V=)" << V << memory << DIVIDER;
    std::cout << "Memory after sum in normal view:\n" << memory.getNormalMatrix() << DIVIDER;
    std::cout << "Function #2(Reading addresses: 0x00,0x01 Address for writing 0x02):\n" << memory.function_2(0x00,0x01,0x02) << DIVIDER;
    std::cout << "Function #7(Reading addresses: 0x03,0x04 Address for writing 0x05):\n" << memory.function_2(0x03,0x04,0x05) << DIVIDER;
    std::cout << "Function #8(Reading addresses: 0x06,0x07 Address for writing 0x08):\n" << memory.function_2(0x06,0x07,0x08) << DIVIDER;
    std::cout << "Function #13(Reading addresses: 0x09,0x0A Address for writing 0x0B):\n" << memory.function_2(0x09,0x0A,0x0B) << DIVIDER;
    std::cout << "Memory after functions:\n" << memory.getNormalMatrix() << DIVIDER;
    return 0;
}