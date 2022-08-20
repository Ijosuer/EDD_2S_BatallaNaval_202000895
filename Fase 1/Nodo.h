#include <stddef.h>
#include <string> 
using namespace std;

class Nodo{
    public:
    string x;
    string y;
    Nodo* siguiente= NULL;
    Nodo* anterior= NULL;

    // Constructor
    Nodo(string _x , string _y){
        x = _x;
        y = _y;
        siguiente = NULL;
        anterior = NULL;
    }
    private:
};