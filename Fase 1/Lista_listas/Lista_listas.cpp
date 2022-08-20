#include <string>
#include <iostream>
#include <fstream>

#include "Lista_listas.h"

using namespace std;

//Programar los metodos

void Lista_listas::insertarCategoria(string _nameCategoria){
    Categoria* tmp = new Categoria(_nameCategoria);
    tmp->siguiente = cabecera;
    cabecera = tmp;

}

void Lista_listas::insertarArticulo(string _categoria,string _id,string _name,string _precio, string _src){
    Categoria* tmp_categoria = cabecera;
    while(tmp_categoria != NULL){
        if(tmp_categoria->categoria == _categoria ){
            Articulo* nuevoArticulo = new Articulo(_id,_name,_precio,_src);
            Articulo* inicioArticulos = tmp_categoria->abajo;
            tmp_categoria->abajo =  nuevoArticulo;
            nuevoArticulo->abajo = inicioArticulos;
            break;
        }
        tmp_categoria = tmp_categoria->siguiente;
    }
}

void Lista_listas::report(){
    Categoria* aux = cabecera;
    Articulo* tmp = aux->abajo;
    string text = "";
    text+="rankdir=LR; \n node[shape=egg,style=filled,color=khaki,fontname=\"Century Gothic\"]; graph [fontname = \"Century Gothic\"];\n";
    text+="labelloc = \"t;\"label = \"Articulos\";\n";
    while(aux != NULL){
        text+="x"+aux->categoria+"[dir=both label = \"Categoria = "+(aux->categoria)+ "\"]";
        text+="x"+(aux->categoria)+"-> x"+(aux->siguiente->categoria)+"\n";
        aux = aux->siguiente;
        if(aux->siguiente == NULL){
            text+="x"+aux->categoria+"[dir=both label = \"Categoria = "+(aux->categoria)+ "\"]";
            texto_grafica = text;
            break;
        }
    }
    
}

void Lista_listas::crearGrafica(){
    report();
    string contenido = "digraph G {\n\n";
    string filename("Articulos_texto.txt");
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


void Lista_listas::showCategorias(){
    Categoria* tmp = cabecera;
    cout<<"**********CATEGORIAS**********"<<endl;
    while(tmp != NULL){
        cout<<tmp->categoria<<endl;
        tmp = tmp->siguiente;
    }
}

void Lista_listas::showArticulos(string _nameCategoria){
    Categoria* tmp = cabecera;
    while (tmp != NULL){
        if(tmp->categoria == _nameCategoria){
            cout<<"**********CATEGORIAS "+_nameCategoria+"**********"<<endl;
            Articulo* tmpArticulos = tmp->abajo;
            while(tmpArticulos != NULL){
                cout<<tmpArticulos->nombre<<endl;
                tmpArticulos = tmpArticulos->abajo;
            }
            break;
        }
        tmp = tmp->siguiente;
    }
}

void Lista_listas::show(){
    Categoria* tmp = cabecera;
    while (tmp != NULL){
        cout<<"**********CATEGORIAS "+tmp->categoria+"**********"<<endl;
        Articulo* tmp2 = tmp->abajo;
        while(tmp2 != NULL){
        cout<<"----Articulo"+tmp2->nombre<<endl;
        tmp2 = tmp2->abajo;
        }
        tmp = tmp->siguiente;
    }
}