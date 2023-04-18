#include <stdlib.h>
#include "Memory.hpp"
Memory::Memory()
{
    std::vector<std::vector<bool>> memory(SIZE, std::vector<bool>(SIZE,0));
    this->memory = memory;
}
std::vector<std::vector<bool>> Memory::getNormalMatrix()
{
    std::vector<std::vector<bool>> memory;
    for (int i = 0; i < SIZE; i++)
    {
        memory.push_back(this->Read(i));
    }
    return memory;
}
std::vector<std::vector<bool>> Memory::getDiagonalMatrix(std::vector<std::vector<bool>> matrix)
{
    for (int i = 0; i < matrix.size(); i++)
    {
        this->Write(matrix[i],i);
    }
    return this->memory;
}
std::vector<std::vector<bool>> Memory::getMatrix()
{
    return memory;
}
std::vector<std::vector<bool>> Memory::getElementsInInterval(std::vector<bool>& lowerLimitWord,std::vector<bool>& upperLimitWord)
{
    std::vector<std::vector<bool>> target_words;
    for (int i = 0; i < memory.size(); i++)
    {
        if (lowerLimitWord<this->Read(i) && upperLimitWord>this->Read(i))
        {
            target_words.push_back(this->Read(i)); 
        }
    }
    return target_words;
}
std::vector<bool> Memory::getRandomWord()
{
    std::vector<bool> word;
    for (int i = 0; i < SIZE; i++)
    {
        word.push_back(rand()%2);   
    }
    return word;
}
void Memory::Write(std::vector<bool> word, int address)
{
    for (int i = address; i < SIZE; i++)
    {
        memory[i][address] = word[i-address];
    }
    for (int j = 0; j < address; j++)
    {
        memory[j][address] = word[SIZE-address+j];
    }
}
std::vector<bool> Memory::Read(int address)
{
    std::vector<bool> word;
    for (int i = address; i < SIZE; i++)
    {
        word.push_back(memory[i][address]);
    }
    for (int i = 0; i < address; i++)
    {
        word.push_back(memory[i][address]);
    }
    return word;    
}
void Memory::sum(std::vector<bool> V)
{
    for (int i = 0; i < SIZE; i++)
    {
        std::vector<bool> Vj;
        std::vector<bool> word = this->Read(i);
        for (int j = 0; j < 3; j++)
        {
            Vj.push_back(word[j]);
        }
        if (Vj==V)
        {
            std::cout << Vj << V << DIVIDER;
            std::cout << std::hex << i << '\n';
            std::vector<bool> Aj;
            std::vector<bool> Bj;
            for (int k = 3; k < 7; k++)
            {
                Aj.push_back(word[k]);
            }
            for (int k = 7; k < 11; k++)
            {
                Bj.push_back(word[k]);
            }
            std::vector<bool> Sj = this->sumBinaries(Aj,Bj);
            for (int k = 11; k < 16; k++)
            {
                word[k] = Sj[k-11];
            }
            this->Write(word,i);
        }
    }
}
std::vector<bool> Memory::sumBinaries(std::vector<bool> A, std::vector<bool> B)
{
    std::vector<bool> S;
    bool carry = false;
    for (int i = 3; i >=0; i--)
    {
        int a = A[i];
        int b = B[i];
        int c = carry;
        if(a+b+c == 3)
        {
            S.insert(S.begin(),1);
        }
        else if(a+b+c == 2)
        {
            S.insert(S.begin(),0);
            carry = 1;
        }
        else if(a+b+c == 1)
        {
            carry = 0;
            S.insert(S.begin(),1);
        }
        else
        {
            S.insert(S.begin(),0);
        }
    }
    S.insert(S.begin(),carry);
    return S;
}
std::vector<bool> Memory::function_2(int address_1, int address_2, int address_3)
{
    std::vector<bool> word_1 = this->Read(address_1);
    std::vector<bool> word_2 = this->Read(address_2);
    std::vector<bool> result_word;
    for (int i = 0; i < SIZE; i++)
    {
        result_word.push_back(word_1[i]*!word_2[i]);
    }
    this->Write(result_word, address_3);
    return result_word; 
}
std::vector<bool> Memory::function_7(int address_1, int address_2, int address_3)
{
    std::vector<bool> word_1 = this->Read(address_1);
    std::vector<bool> word_2 = this->Read(address_2);
    std::vector<bool> result_word;
    for (int i = 0; i < SIZE; i++)
    {
        result_word.push_back(word_1[i]+word_2[i]);
    }
    this->Write(result_word, address_3);
    return result_word; 
}
std::vector<bool> Memory::function_8(int address_1, int address_2, int address_3)
{
    std::vector<bool> word_1 = this->Read(address_1);
    std::vector<bool> word_2 = this->Read(address_2);
    std::vector<bool> result_word;
    for (int i = 0; i < SIZE; i++)
    {
        result_word.push_back(!(word_1[i]+word_2[i]));
    }
    this->Write(result_word, address_3);
    return result_word; 
}
std::vector<bool> Memory::function_13(int address_1, int address_2, int address_3)
{
    std::vector<bool> word_1 = this->Read(address_1);
    std::vector<bool> word_2 = this->Read(address_2);
    std::vector<bool> result_word;
    for (int i = 0; i < SIZE; i++)
    {
        result_word.push_back(!word_1[i]+word_2[i]);
    }
    this->Write(result_word, address_3);
    return result_word; 
}