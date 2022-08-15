#include <iostream>
#include "Lista_Simple.cpp"
using namespace std;

void menu(){
    cout<<"HOLA:D"<<endl;
}

void crearSimple(){
    Lista_Simple lista;
    lista.insertarInicio("aux","aux","34","20");
    lista.insertarInicio("Josue","EDD","100","21");
    lista.insertarInicio("Mike","mike123","25","18");
    lista.insertarInicio("Dany","dann3","11","30");
    // lista.verLista();
    lista.verLista2();
    lista.isPrimero();
    lista.isUltimo();
    bool ans = lista.whereis("Josue");
    cout<<ans<<endl;
}

int main(){
    crearSimple();
    menu();
}