#include "Nodo.h"
#include <string>
#include "../lib/crow_all.h"
using namespace std;

class Cola{
    public:
    string texto_grafica;
    Nodo* primero;
    Nodo* ultimo;
    int len;

    Cola(){
        primero = NULL;
        ultimo = NULL;
        texto_grafica = "";
        len = 0;
    }
    //Metodo insertar
    void Enqueue(int _id, string _x, string _y);
    void Dequeue();
    void show();
    void report();
    void crearGrafica();
    vector<crow::json::wvalue> to_vector();
    private:
};