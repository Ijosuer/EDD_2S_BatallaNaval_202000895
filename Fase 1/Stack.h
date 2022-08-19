#include "Nodo_tutorial.h"
#include <string>
using namespace std;

class Stack{
    public:
    string texto_grafica;
    Nodo_tutorial* primero;
    Nodo_tutorial* ultimo;
    int len;

    Stack(){
        primero = NULL;
        ultimo = NULL;
        texto_grafica = "";
        len = 0;
    }

    void push(string _data,string _data2);
    void peek();
    void pop();

    private:
};