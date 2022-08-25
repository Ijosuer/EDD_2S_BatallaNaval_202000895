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

//      --- COLORES ---
string RED = "\u001b[31m",GREEN ="\u001b[32m",YELLOW = "\u001b[33m",BLUE = "\u001b[34m";
string MAGENTA = "\u001b[35m",CYAN = "\u001b[36m",WHITE = "\u001b[37m",RESET = "\u001b[0m";
string BGblack = "\u001b[40;1m", BGr = "\u001b[0m";
//      --- ---- ---


    
    //Constructor
    Lista_Circular_Doble(){
        primero = NULL;
        ultimo = NULL;
        len = 0;
        texto_grafica = "";
    }
    //---Metodos---
    
    //Metodo insertar
    void insertarInicio(string _name,string _pwd,int _coins,int _edad);
    //Metodo registrar
    bool registrar(string _name,string _pwd,int _coins,int _edad);
    //Agregar compras
    void agregarBarco(string _name);
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
    //Metodo buscar Nick
    bool isNick(string _name);
    //Metodo buscar Usuario
    bool whereis(string _name, string _pwd);
    //Retornar edad
    int dataEdad(string _name);
    //Editar data de un usuario
    bool editar(string _anterior,string _name,string _pwd,int _edad);
    //Eliminar primer nodo;
    void eliminarPrimero();
    //Eliminar Usuario;
    void eliminarUsuario(string _name,string _pwd);
    //IInfo monedas
    int cuantasFichas(string _name);
    //Ordenar
    private:
};