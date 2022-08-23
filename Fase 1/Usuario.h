#include <stddef.h>
#include <string> 
using namespace std;

class Usuario{
    //Atributos y metodos
    public:
    string name;
    string pwd;
    string coins;
    string edad;
    string barco;
    Usuario* siguiente;
    Usuario* anterior;
    //Constructor
    Usuario(string _name,string _pwd,string _coins,string _edad){
        name = _name;
        pwd = _pwd;
        coins = _coins;
        edad = _edad;
        barco = "";
        siguiente = NULL;
        anterior = NULL;
    }
    private:
    
};