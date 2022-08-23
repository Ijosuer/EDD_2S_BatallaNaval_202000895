#pragma once
#include <stddef.h>
#include <string> 
#include "Articulo.h"
using namespace std;

class Categoria{
    //Atributos y metodos
    public:
    string categoria;
    Categoria* siguiente;
    Articulo* abajo;
    //Constructor
    Categoria(string _categoria){
        categoria = _categoria;
        siguiente = NULL;
        abajo = NULL;
    }
    private:
    
};