#include <String>
#include <iostream>
#define SIZE 4
#define PERCENTAGE_OF_REHASH 75
#define SHIFT 2

struct Data
{
    bool is_empty = true;
    std::string key;
    std::string data;
};

class HashTable{
    private:
        Data* data_;
        unsigned long size_;
        unsigned long number_elements_;
        double percentage_of_rehash_;
    protected: 
        void ReHash();
        void addElementCollisionHandling(unsigned long&, std::string&, std::string&);
        bool rmElementCollisionHandling(std::string&, unsigned long&);
        std::string getElementCollisionHandling(std::string&, unsigned long&);
        unsigned long getHash(std::string&);
        unsigned long getId(unsigned long&);
    public:
        HashTable();
        ~HashTable();
        void addElement(std::string&, std::string&);
        void rmElement(std::string&);
        std::string getElement(std::string&);
        unsigned long getSize();
        unsigned long getNumberElements();
        Data* getData();
};
inline std::ostream& operator << (std::ostream &os, const HashTable &hash_table)
{
    HashTable ht = hash_table;
    Data* data = ht.getData();
    os << "id\tkey\tdata\n";
    for (unsigned long i = 0; i < ht.getSize(); i++)
    {
        if(!data[i].is_empty)
        {
            os << i << "\t" << data[i].key << "\t" << data[i].data << "\n";
        }
    }
    return os;
}
