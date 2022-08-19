#include <stddef.h>
#include <string> 
using namespace std;

class Articulo{
    //Atributos y metodos
    public:
    string categoria;
    string id;
    string nombre;
    string precio;
    string src;
    Articulo* siguiente;
    Articulo* anterior;
    //Constructor
    Articulo(string _categoria,string _id,string _name,string _precio, string _src){
        categoria = _categoria;
        id = _id;
        nombre = _name;
        precio = _precio;
        src = _src;
        siguiente = NULL;
        anterior = NULL;
    }
    private:
    
};