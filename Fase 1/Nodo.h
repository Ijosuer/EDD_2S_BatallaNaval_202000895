#include <stddef.h>
#include <string> 
using namespace std;

class Nodo{
    public:
    string x;
    string y;
    int id;
    Nodo* siguiente;
    Nodo* anterior;

    // Constructor
    Nodo(int _id, string _x , string _y){
        id = _id;
        x = _x;
        y = _y;
        siguiente = NULL;
        anterior = NULL;
    }
    private:
};