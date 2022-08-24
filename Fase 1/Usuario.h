#include <stddef.h>
#include <string> 
using namespace std;

class Usuario{
    //Atributos y metodos
    public:
    string name;
    string pwd;
    int coins;
    int edad;
    string barco;
    Usuario* siguiente;
    Usuario* anterior;
    //Constructor
    Usuario(string _name,string _pwd,int _coins,int _edad){
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