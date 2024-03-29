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
    void insertarArticulo(string _categoria,int _id,string _name,int _precio, string _src);
    void showCategorias();
    void showArticulos(string _nameCategoria);
    void show(int _tokens);
    void report();
    bool whereIs(string _categoria);
    bool comprar(int id, int monedas);
    void crearGrafica();
    private:
};
