#include "Memory.hpp"
std::vector<std::vector<bool>> Memory::getMatrix()
{
    return memory;
}
std::vector<bool> Memory::toBinary(unsigned short number)
{
    std::vector<bool> bin;
    while(number!=0)
    {
        bin.insert(bin.begin(),number%2);
        number/=2;
    }
    while(bin.size()!=16)
    {
        bin.insert(bin.begin(),0);
    }
    return bin;
}
void Memory::insert(unsigned short& number)
{
    memory.push_back(toBinary(number));
}
void Memory::sort(bool typeOfSort) //0 - less, 1 - greater
{
    for (int i = 0; i < memory.size(); i++) {
        for (int j = 0; j < memory.size() - i - 1; j++) {
            if (memory[j] > memory[j + 1] | typeOfSort) {
                std::vector<bool> temp_word = memory[j];
                memory[j] = memory[j + 1];
                memory[j + 1] = temp_word;
            }
        }
    }
}
std::vector<std::vector<bool>> Memory::getElementsInInterval(unsigned short& lowerLimit, unsigned short& upperLimit)
{
    std::vector<std::vector<bool>> target_words;
    std::vector<bool> lowerLimitWord = toBinary(lowerLimit);
    std::vector<bool> upperLimitWord = toBinary(upperLimit);
    for (int i = 0; i < memory.size(); i++)
    {
        if (lowerLimitWord<memory[i] && memory[i]<upperLimitWord)
        {
            target_words.push_back(memory[i]);   
        }
    }
    return target_words;
}