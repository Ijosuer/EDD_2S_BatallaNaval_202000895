#include <stddef.h>
#include <string> 
using namespace std;

class Nodo_tutorial{
    public:
    string x;
    string y;
    Nodo_tutorial* siguiente;
    Nodo_tutorial* anterior;

    // Constructor
    Nodo_tutorial(string _x , string _y){
        x = _x;
        y = _y;
        siguiente = NULL;
        anterior = NULL;
    }
    private:
};