#include "Usuario.h"
#include <string>
using namespace std;

class Lista_Simple{
    //metodos y atributos
    public:
    Usuario* primero = NULL;
    Usuario* ultimo = NULL;
    int len;
    
    //Constructor
    Lista_Simple(){
        primero = NULL;
        ultimo = NULL;
        len = 0;
    }
    //---Metodos---
    
    //Metodo insertar
    void insertarInicio(string _name,string _pwd,string _coins,string _edad);
    void verLista();
    //Metodo mostar
    void verLista2();
    //Metodo primer Usuario   
    void isPrimero();
    //Metodo ultimo Usuario   
    void isUltimo();
    //Metodo buscar Usuario
    bool whereis(string _name);
    private:
};