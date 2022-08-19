#include "Cola.h"
#include <iostream>
#include <fstream>
using namespace std;

void Cola::Enqueue(string _x, string _y){
    Nodo* tmp = new Nodo(_x,_y);
    if(primero == NULL){
        ultimo = tmp;
        primero = ultimo;
        cout<<"LLEGO EL PAVO"<<endl;
        len+=1;
    }else{
        ultimo->siguiente = tmp;
        ultimo = ultimo->siguiente;
        cout<<"LA TORTUGA LLEGA TARDE OTRA VEZ"<<ultimo->x<<endl;
        len+=1;
    }
}

void Cola::Dequeue(){
    if(len == 0){
        cout<<"NADA PARA BORRAR"<<endl;
    }else{
        if(len == 1){
            len -= 1;
            ultimo == ultimo->siguiente;
            cout<<"El 'X' es este: "+ultimo->x<<endl;
        }else if(len >= 2){
        Nodo* tmp = primero;
        primero = primero->siguiente;
        cout<<"El 'X' es este: "+tmp->x<<endl;
        len -=1;
        }
    }
}

void Cola::report(){
    Nodo* tmp = primero;
    int size = len;
    string text = "";
    text+="rankdir=LR; \n node[shape=egg,style=filled,color=khaki,fontname=\"Century Gothic\"]; graph [fontname = \"Century Gothic\"];\n";
    text+="labelloc = \"t;\"label = \"Tutoriales\";\n";
    if (size == 0){
        text += "VACIO";
        texto_grafica = text;
        return;
    }
    while(tmp != NULL){
       text += "x"+(tmp->x)+"[dir=both label = \"X = "+tmp->x+"\\nY = "+tmp->y+"\"]";
        if (primero == ultimo){
            texto_grafica = text;
            break;
        }
       text += "x"+(tmp->siguiente->x)+"-> x"+(tmp->x)+"\n";
       tmp = tmp->siguiente;
       if(tmp != primero){
        text += "x"+(tmp->x)+"[dir=both label = \"X = "+tmp->x+"\\nY = "+tmp->y+"\"]";
        cout<<text<<endl;
       }
       if(tmp == ultimo){
           text +="x"+ (tmp->x)+"\n";
           texto_grafica = text;
           break;
       }
    }
}

void Cola::crearGrafica(){
    report();
    string contenido = "digraph G {\n\n";
    string filename("texto_cola.txt");
    fstream file_out;
    file_out.open(filename, std::ios_base::out);
    if (!file_out.is_open()) {
        cout << "failed to open " << filename << '\n';
    } else {
        contenido += texto_grafica;
        contenido +="}\n";
        file_out <<contenido<< endl;
        cout << "Done Writing ur Queue!" << endl;
    }
}