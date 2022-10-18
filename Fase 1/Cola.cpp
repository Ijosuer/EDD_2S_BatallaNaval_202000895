#include "Cola.h"
#include <iostream>
#include <fstream>
using namespace std;

void Cola::Enqueue(int _id, string _x, string _y){
    Nodo* tmp = new Nodo(_id,_x,_y);
    if(primero == NULL){
        ultimo = tmp;
        primero = ultimo;
        len+=1;
    }else{
        ultimo->siguiente = tmp;
        ultimo = ultimo->siguiente;
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
        }else if(len >= 2){
        Nodo* tmp = primero;
        primero = primero->siguiente;
        len -=1;
        }
    }
}

void Cola::show(){
    string WHITE = "\u001b[37m";
    string BLUE = "\u001b[34m";
    string text = "";
    Nodo* tmp = primero;
    while (tmp != NULL)
    {
        if (tmp != primero)
        {
            if (tmp == ultimo)
            {
                text += "("+BLUE+tmp->x+","+tmp->y+WHITE+")";
                cout<<text<<endl;
                break;
            }else{
            text += WHITE+"  ("+BLUE+tmp->x+","+tmp->y+WHITE+")"+"->";
            tmp = tmp->siguiente;
                
            }
        }else{
        tmp = tmp->siguiente;
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
       text += "x"+to_string(tmp->id)+"[dir=both label = \"X = "+tmp->x+"\\nY = "+tmp->y+"\"]";
        if (primero == ultimo){
            texto_grafica = text;
            break;
        }
       text += "x"+to_string(tmp->siguiente->id)+"-> x"+to_string(tmp->id)+"\n";
       tmp = tmp->siguiente;
       if(tmp != primero){
        text += "x"+to_string(tmp->id)+"[dir=both label = \"X = "+tmp->x+"\\nY = "+tmp->y+"\"]";
       }
       if(tmp == ultimo){
           text +="x"+ to_string(tmp->id)+"\n";
           texto_grafica = text;
           break;
       }
    }
}

void Cola::crearGrafica(){
    report();
    string contenido = "digraph G {\n\n";
    string filename("archivos/Tutorial.dot");
    fstream file_out;
    file_out.open(filename, std::ios_base::out);
    if (!file_out.is_open()) {
        cout << "failed to open " << filename << '\n';
    } else {
        contenido += texto_grafica;
        contenido +="}\n";
        file_out <<contenido<< endl;
        system("dot -Tpng archivos/Tutorial.dot -o archivos/Tutorial.png");

    }
}