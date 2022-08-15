#include "Lista_Simple.h"
#include <iostream>
using namespace std;

//Programar los metodos

void Lista_Simple::insertarInicio(string _name,string _pwd,string _coins,string _edad){
    Usuario* tmp = new Usuario(_name,_pwd,_coins,_edad);
    //Si la lista esta vacia
    if(primero == NULL){
        primero = tmp;
        ultimo = primero;
        len +=1;
    }else{
        ultimo->siguiente = tmp;
        ultimo = tmp;
        ultimo->siguiente = primero;
        len += 1;
    }
}

void Lista_Simple::verLista(){
    Usuario* tmp = primero;
    cout<<"Esta es la lista de usuarios"<<endl;
    while(tmp != NULL){
        cout<<tmp->coins<<endl;
        tmp = tmp->siguiente;
    }
}

void Lista_Simple::verLista2(){
    Usuario* tmp = primero;
    cout<<"---VIENDO LA LISTA CON FOR--"<<endl;
    for (int i = 0; i < len; i++)
    {
        cout<<"No. "<<i+1 <<" Dato: "<<tmp->name
                                     <<"-"<<tmp->pwd
                                     <<"-"<<tmp->coins
                                     <<"-"<<tmp->edad<<endl;
        tmp = tmp->siguiente;
    }
}

void Lista_Simple::isPrimero(){
    cout<<"Este es el primer NODO: "<<primero->name<<endl;
    cout<<"Este es el primer NODO.sig: "<<primero->siguiente->name<<endl;
}

void Lista_Simple::isUltimo(){
    cout<<"Este es el ultimo NODO: "<<ultimo->name<<endl;
    cout<<"Este es el ultimo NODO.sig: "<<ultimo->siguiente->name<<endl;
}

bool Lista_Simple::whereis(string _name){
    cout<<"Encuentras el nodo "<<_name<<"?"<<endl;
    Usuario* tmp = primero;
    for (int i = 0; i < len; i++){
        if(tmp->name == _name){
            cout<<"Simon aki esta"<<endl;
            return true;
        }else{
            tmp = tmp->siguiente;
        }
    }
    return false;
}