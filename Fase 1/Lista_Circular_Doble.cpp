#include "Lista_Circular_Doble.h"
#include <iostream>
#include <fstream>
using namespace std;

//Programar los metodos

void Lista_Circular_Doble::insertarInicio(string _name,string _pwd,string _coins,string _edad){
    Usuario* tmp = new Usuario(_name,_pwd,_coins,_edad);
    //Si la lista esta vacia
    if(primero == NULL){
        primero = tmp;
        ultimo = primero;
        len +=1;
    }else{
        Usuario * aux = ultimo;
        ultimo = aux->siguiente = tmp;
        ultimo->anterior = aux;
        len += 1;
    }
    unirNodos();
}

void Lista_Circular_Doble::eliminarUltimo(){
    if(primero == NULL){
        cout<<"NO hay nodos D:"<<endl;
    }else if(primero == ultimo){
        primero = ultimo = NULL;
    }else{
        ultimo = ultimo->anterior;
    }
    unirNodos();
}

void Lista_Circular_Doble::unirNodos(){
    if (primero != NULL){
        primero->anterior = ultimo;
        ultimo->siguiente = primero;
    }
}

void Lista_Circular_Doble::report(){
    Usuario* aux = primero;
    string text = "";
    text+="rankdir=LR; \n node[shape=egg,style=filled,color=khaki,fontname=\"Century Gothic\"]; graph [fontname = \"Century Gothic\"];\n";
    text+="labelloc = \"t;\"label = \"Cursos\";\n";

    try
    {
        while(aux != NULL){
        text+="x"+aux->coins+"[dir=both label = \"Codigo = "+(aux->coins)+"\\nNombre = "+(aux->name)+"\\n Creditos = "+(aux->pwd)+ "\"]";
            // cout<<text<<endl;
            text+="x"+(aux->coins)+"-> x"+(aux->siguiente->coins)+"\n";
            // cout<<text<<endl;
            text+="x"+(aux->coins)+"-> x"+(aux->anterior->coins)+"\n";
            // cout<<text<<endl;
            aux=aux->siguiente;
        if (aux!=primero){
                text+="x"+(aux->coins)+"[dir=both label = \"Codigo = "+(aux->coins)+"\\nNombre = "+aux->name+"\\n Creditos = "+(aux->pwd)+ "\"]";
                // cout<<text<<endl;
        }    
        if (aux==ultimo){
            text+="x"+(aux->coins)+"-> x"+(aux->siguiente->coins)+"\n";
            text+="x"+(aux->coins)+"-> x"+(aux->anterior->coins)+"\n";
            // cout<<text<<endl;
            texto_grafica = text;
            break;
        }
    }
    }
    catch(const std::exception& e)
    {
        cerr << e.what() << '\n';
    }
}

void Lista_Circular_Doble::crearGrafica(){
    report();
    string contenido = "digraph G {\n\n";
    string filename("texto.txt");
    fstream file_out;
    file_out.open(filename, std::ios_base::out);
    if (!file_out.is_open()) {
        cout << "failed to open " << filename << '\n';
    } else {
        contenido += texto_grafica;
        contenido +="}\n";
        file_out <<contenido<< endl;
        cout << "Done Writing!" << endl;
    }
}

void Lista_Circular_Doble::verLista(){
    Usuario* tmp = primero;
    cout<<"Esta es la lista de usuarios"<<endl;
    while(tmp != NULL){
        cout<<tmp->coins<<endl;
        tmp = tmp->siguiente;
    }
}

void Lista_Circular_Doble::isPrimero(){
    cout<<"Este es el primer NODO: "<<primero->name<<endl;
    cout<<"Este es el primer NODO.ant: "<<primero->anterior->name<<endl;
}

void Lista_Circular_Doble::isUltimo(){
    cout<<"Este es el ultimo NODO: "<<ultimo->name<<endl;
    cout<<"Este es el ultimo NODO.sig: "<<ultimo->siguiente->name<<endl;
}

bool Lista_Circular_Doble::whereis(string _name){
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