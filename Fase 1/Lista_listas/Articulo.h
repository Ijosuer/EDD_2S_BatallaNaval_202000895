#pragma once
#include <stddef.h>
#include <string> 
using namespace std;

class Articulo{
    //Atributos y metodos
    public:
    string id;
    string nombre;
    string precio;
    string src;
    Articulo* abajo;
    //Constructor
    Articulo(string _id,string _name,string _precio, string _src){
        id = _id;
        nombre = _name;
        precio = _precio;
        src = _src;
        abajo = NULL;
    }
    private:
    
};