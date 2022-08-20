#include "Categoria.h"
#include "Articulo.h"
#include <string>
using namespace std;

class Lista_listas{
    //metodos y atributos
    public:
    string texto_grafica;
    Categoria* cabecera = NULL;

//Constructor
    Lista_listas(){
        cabecera = NULL;
        texto_grafica = "";
    }
    //Metodo insertar
    void insertarCategoria(string _nameCategoria);
    void insertarArticulo(string _categoria,string _id,string _name,string _precio, string _src);
    void showCategorias();
    void showArticulos(string _nameCategoria);
    void show();
    void report();
    void crearGrafica();
    private:
};
