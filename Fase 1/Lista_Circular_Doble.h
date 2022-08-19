#include "Usuario.h"
#include <string>
using namespace std;

class Lista_Circular_Doble{
    //metodos y atributos
    public:
    string texto_grafica;
    Usuario* primero = NULL;
    Usuario* ultimo = NULL;
    int len;
    
    //Constructor
    Lista_Circular_Doble(){
        primero = NULL;
        ultimo = NULL;
        len = 0;
        texto_grafica = "";
    }
    //---Metodos---
    
    //Metodo insertar
    void insertarInicio(string _name,string _pwd,string _coins,string _edad);
    //Metodo unir NODOS
    void unirNodos();
    //Metodo eliminar ultimo nodo
    void eliminarUltimo();
    //Metodo mostar
    void verLista();
    //Graficar
    void report();
    void crearGrafica();
    //Metodo primer Usuario   
    void isPrimero();
    //Metodo ultimo Usuario   
    void isUltimo();
    //Metodo buscar Usuario
    bool whereis(string _name, string _pwd);
    //Retornar edad
    string dataEdad(string _name);
    //Editar data de un usuario
    bool editar(string _name,string _pwd,string _edad);
    private:
};