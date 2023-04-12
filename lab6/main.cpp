#include "HashTable.hpp"

int main()
{
    HashTable table;
    std::string keys[] = {"John", "Mary", "Alex", "William", "Emila", "Olivia", "James", "Sophia", "Ethan", "Isabella", "Michael", "Emma", "Benjamin", "Ava", "Daniel", "Mia", "Matthew", "Charlotte", "David", "Amelia", "Andrew", "Abigail", "Lucas", "Harper", "Joseph", "Evelyn", "Samuel", "Emily", "Christopher", "Ella", "Jacob", "Grace", "Willy", "Sophie", "Ryan", "Chloe", "Gabriel", "Victoria", "Nicholas", "Zoe", "Luke", "Lily", "Nathan", "Lila", "Anthony", "Layla", "Max", "Aria", "Kevin", "Avery", "Eric", "Eleanor", "Mark", "Audrey", "Philip", "Hannah", "Peter", "Aurora", "Simon", "Bella", "Sean", "Brooklyn", "Henry", "Eva", "Adam", "Caroline", "Thomas"};
    std::string values[] = {
        "Teacher", "Doctor", "Lawyer", "Engineer", "Programmer", "Writer",
        "Nurse", "Scientist", "Accountant", "Chef", "Mechanic", "Musician",
        "Actor", "Athlete", "Dentist", "Pharmacist", "Architect", "Farmer",
        "Salesperson", "Journalist", "Electrician", "Plumber", "Carpenter",
        "Painter", "Truck driver", "Police officer", "Firefighter",
        "Paramedic", "Flight attendant", "Tour guide", "Librarian",
        "Construction worker", "Waitress", "Hairdresser",
        "Cleaner", "Administrative assistant",
        "Graphic designer", "Web developer", "Data analyst",
        "Marketing specialist", "Human resources specialist", "Consultant",
        "Social worker", "Psychologist", "Professor",
        "Researcher", "Military service member", "Judge", "Real estate agent",
        "Interior designer", "Event planner", "Photographer", "Artist",
        "Fashion designer", "Bartender", "Singer", "Dancer", "Magician",
        "Stock trader", "Entrepreneur", "Gardener", "Coach", "Fitness trainer"
    };
    for (int i = 0; i < 63; i++)
    {
        table.addElement(keys[i],values[i]);
    }
    std::string aboba = "James";
    std::cout << table << '\n';
    std::cout << table.getNumberElements() << '\n';
    std::cout << table.getElement(aboba) << '\n';   
    table.rmElement(aboba);
    std::cout << table << '\n';
    std::cout << table.getNumberElements() << '\n';
    return 0;
}