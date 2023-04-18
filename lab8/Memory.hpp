#include <vector>
#include <iostream>
#define SIZE 16
#define DIVIDER "--------------------------------------\n"
class Memory
{   
private:
    std::vector<std::vector<bool>> memory;
public:
    Memory();
    void Write(std::vector<bool>, int);
    std::vector<std::vector<bool>> getNormalMatrix();
    std::vector<std::vector<bool>> getDiagonalMatrix(std::vector<std::vector<bool>>);
    std::vector<bool> Read(int);
    std::vector<bool> getRandomWord();
    std::vector<std::vector<bool>> getElementsInInterval(std::vector<bool>&,std::vector<bool>&);
    std::vector<std::vector<bool>> getMatrix();
    std::vector<bool> function_2(int, int, int);
    std::vector<bool> function_7(int, int, int);
    std::vector<bool> function_8(int, int, int);
    std::vector<bool> function_13(int, int, int);
    void sum(std::vector<bool>);
    std::vector<bool> sumBinaries(std::vector<bool>,std::vector<bool>);
};
inline std::ostream& operator<<(std::ostream& os, const Memory& memory)
{
    Memory mem = memory;
    std::vector<std::vector<bool>> matrix = mem.getMatrix();
    for (int i = 0; i < matrix.size(); i++)
    {
        for (int j = 0; j < matrix[i].size()-1; j++)
        {
            os << matrix[i][j] << '|';       
        }
        os << matrix[i][matrix[i].size()-1] << '\n';
    }
    return os;
}
inline std::ostream& operator<<(std::ostream& os, std::vector<std::vector<bool>> matrix)
{
    for (int i = 0; i < matrix.size(); i++)
    {
        for (int j = 0; j < matrix[i].size()-1; j++)
        {
            os << matrix[i][j] << '|';       
        }
        os << matrix[i][matrix[i].size()-1] << '\n';
    }
    return os;
}
inline std::ostream& operator<<(std::ostream& os, std::vector<bool> word)
{
    for (int i = 0; i < word.size()-1; i++)
    {
        os << word[i] << ',';
    }
    return os << word[word.size()-1] << '\n';
}
inline bool operator <(std::vector<bool>& word_1,std::vector<bool>& word_2)
{
    bool g = false;
    bool l = false;
    for (int i = 0; i < word_1.size(); i++)
    {
        g = g | (!word_2[i] & word_1[i] & !l);
        l = l | (word_2[i] & !word_1[i] & !g);
    }
    if (g == 0 && l == 1)
    {
        return true;
    }
    return false;
}
inline bool operator >(std::vector<bool>& word_1,std::vector<bool>& word_2)
{
    bool g = false;
    bool l = false;
    for (int i = 0; i < word_1.size(); i++)
    {
        g = g | (!word_2[i] & word_1[i] & !l);
        l = l | (word_2[i] & !word_1[i] & !g);
    }
    if (g == 1 && l == 0)
    {
        return true;
    }
    return false;
}