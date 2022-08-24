#pragma once
#include <stddef.h>
#include <string> 
using namespace std;

class Articulo{
    //Atributos y metodos
    public:
    int id;
    string nombre;
    int precio;
    string src;
    Articulo* abajo;
    //Constructor
    Articulo(int _id,string _name,int _precio, string _src){
        id = _id;
        nombre = _name;
        precio = _precio;
        src = _src;
        abajo = NULL;
    }
    private:
    
};