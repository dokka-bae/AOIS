#include "HashTable.hpp"
HashTable::HashTable()
{
    size_ = SIZE;
    number_elements_ = 0;
    percentage_of_rehash_ = PERCENTAGE_OF_REHASH;
    data_ = new Data[size_];
}
HashTable::~HashTable()
{
    free(data_);
}
void HashTable::ReHash()
{
    std::string* buffer_keys = new std::string[number_elements_];
    std::string* buffer_data = new std::string[number_elements_];
    unsigned long j = 0;
    for (unsigned long i = 0; i < size_; i++)
    {
        if (!data_[i].is_empty)
        {
            buffer_keys[j] = data_[i].key;
            buffer_data[j] = data_[i].data;
            ++j;
        }
    }
    delete[] data_;
    size_*=2;
    data_ = new Data[size_];
    unsigned long number_elements = number_elements_;
    number_elements_ = 0;
    for (unsigned long i = 0; i < number_elements; i++)
    {
        addElement(buffer_keys[i], buffer_data[i]);
    }
    delete[] buffer_keys;
    delete[] buffer_data;
}
void HashTable::addElement(std::string& key, std::string& data)
{
    if(float(number_elements_)/float(size_)*100 >= percentage_of_rehash_)
    {
        std::cout << "Rehashing... " << size_  << '\t' << number_elements_ <<'\n';
        ReHash();
        std::cout << "Rehashed" << '\n';
    }
    number_elements_++;
    unsigned long hash = getHash(key);
    unsigned long id = getId(hash);
    if (data_[id].is_empty)
    {
        data_[id].key = key;
        data_[id].data = data;
        data_[id].is_empty = false;
        return;
    }
    if (data_[id].key == key)
    {
        data_[id].data = data;
        return;
    }
    addElementCollisionHandling(id, key, data);
}
void HashTable::addElementCollisionHandling(unsigned long& id, std::string& key, std::string& data)
{
    for(unsigned long i = id+SHIFT; i < size_; i+=SHIFT) //Ищем пустые ячейки после id
    {
        if(data_[i].is_empty)
        {
            data_[i].is_empty = false;
            data_[i].key = key;
            data_[i].data = data;
            return;
        }
    }
    for(unsigned long i = 0; i < id; i+=SHIFT) //Ищем пустые ячейки с начала массива, если конец оказался занятым
    {
        if(data_[i].is_empty)
        {
            data_[i].is_empty = false;
            data_[i].key = key;
            data_[i].data = data;
            return;
        }
    }
}
std::string HashTable::getElement(std::string& key)
{
    unsigned long hash = getHash(key);
    unsigned long id = getId(hash);
    if(data_[id].is_empty) return NULL;
    if(data_[id].key != key) return getElementCollisionHandling(key, id); 
    return data_[id].data; 
}
std::string HashTable::getElementCollisionHandling(std::string& key, unsigned long& id)
{
    for (unsigned long i = id+SHIFT; i < size_; i+=SHIFT)
    {
        if (data_[i].key == key)
        {
            return data_[i].data;
        }
    }
    for (unsigned long i = 0; i < id; i+=SHIFT)
    {
        if (data_[i].key == key)
        {
            return data_[i].data;
        }
    }
    return NULL;
}
void HashTable::rmElement(std::string& key)
{
    unsigned long hash = getHash(key);
    unsigned long id = getId(hash);
    if(data_[id].is_empty) return;
    if(data_[id].key != key) {rmElementCollisionHandling(key, id) ? number_elements_--:number_elements_; return;}
    number_elements_--;
    data_[id].is_empty = true;
}
bool HashTable::rmElementCollisionHandling(std::string& key, unsigned long& id)
{
    for (unsigned long i = id+SHIFT; i < size_; i+=SHIFT)
    {
        if (data_[i].key == key)
        {
            data_[i].is_empty = true;
            return 1;
        }
    }
    for (unsigned long i = 0; i<id; i+=SHIFT)
    {
        if (data_[i].key==key)
        {
            data_[i].is_empty = true;
            return 1;
        }  
    }
    return 0;
}
unsigned long HashTable::getHash(std::string& key) //Генерируем хеш
{
    //Хеш-функция djb2
    unsigned long hash = 5381; 
    int c;
    for (auto c : key)
        hash = ((hash << 5) + hash) + c;
    return hash;
}
unsigned long HashTable::getId(unsigned long& hash) //Генерируем ключ имея хеш
{
    return hash%size_;
}
unsigned long HashTable::getSize()
{
    return this->size_;
}
unsigned long HashTable::getNumberElements()
{
    return this->number_elements_;
}
Data* HashTable::getData()
{
    return this->data_;
}