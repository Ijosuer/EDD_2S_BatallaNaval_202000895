#include <stddef.h>
#include <string> 
using namespace std;

class Nodo{
    public:
    string x;
    string y;
    Nodo* siguiente;
    Nodo* anterior;

    // Constructor
    Nodo(string _x , string _y){
        x = _x;
        y = _y;
        siguiente = NULL;
        anterior = NULL;
    }
    private:
};