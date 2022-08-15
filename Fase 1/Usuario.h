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
    Usuario* siguiente;

    //Constructor
    Usuario(string _name,string _pwd,string _coins,string _edad){
        name = _name;
        pwd = _pwd;
        coins = _coins;
        edad = _edad;
        siguiente = NULL;
    }
    private:
    
};