#include <vector>
#include <iostream>
#define SIZE 16
class Memory
{   
private:
    std::vector<std::vector<bool>> memory;
protected:
    unsigned short& toDecimal(std::vector<bool>);
public:
    void insert(unsigned short&);
    void sort(bool); //0 - less, 1 - greater
    std::vector<bool> toBinary(unsigned short);
    std::vector<std::vector<bool>> getElementsInInterval(unsigned short&,unsigned short&);
    std::vector<std::vector<bool>> getMatrix();
};
inline std::ostream& operator<<(std::ostream& os, const Memory& memory)
{
    Memory mem = memory;
    std::vector<std::vector<bool>> matrix = mem.getMatrix();
    for (int i = 0; i < matrix.size(); i++)
    {
        for (int j = 0; j < matrix[i].size()-1; j++)
        {
            os << matrix[i][j] << ',';       
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
            os << matrix[i][j] << ',';       
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
    return os << word[word.size()-1];
}
inline bool operator >(std::vector<bool>& word_1,std::vector<bool>& word_2)
{
    for (int i = 0; i < word_1.size(); i++)
    {
        if (word_1[i] == 1 && word_2[i] == 0)
        {
            return true;
        }   
        else if (word_2[i] == 1 && word_1[i] == 0)
        {
            return false;
        }   
    }
    return false;
}
inline bool operator <(std::vector<bool>& word_1,std::vector<bool>& word_2)
{
    for (int i = 0; i < word_1.size(); i++)
    {
        if (word_1[i] == 1 && word_2[i] == 0)
        {
            return false;
        }   
        else if (word_2[i] == 1 && word_1[i] == 0)
        {
            return true;
        }   
    }
    return false;
}
inline bool operator ==(std::vector<bool>& word_1,std::vector<bool>& word_2)
{
    for (int i = 0; i < word_1.size(); i++)
    {
        if (word_1[i] != word_2[i])
        {
            return false;
        }
         
    }
    return true;
}