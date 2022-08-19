#include "Stack.h"
#include <iostream>
#include <fstream>

void Stack::push(string _x , string _y){
    Nodo_tutorial* tmp = new Nodo_tutorial(_x,_y);
    tmp->siguiente = primero;
    primero = tmp;
    cout<<"Nodo agregado"<<endl;
}

void Stack::pop(){
    Nodo_tutorial* tmp = NULL;
    if(primero != NULL){
        tmp = new Nodo_tutorial(primero->x, primero->y);
        primero = primero->siguiente;
    }
    cout<<"Sacando a ["+tmp->x<<","+tmp->y+"]"<<endl;
}

void Stack::peek(){
    Nodo_tutorial* tmp = primero;
    cout<<"Este es el nodo en el top ["+tmp->x<<","+tmp->y+"]"<<endl;
}