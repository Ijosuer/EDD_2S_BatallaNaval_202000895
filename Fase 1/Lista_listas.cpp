// #include <string>
#include <iostream>
#include <fstream>

#include "Lista_listas.h"

using namespace std;

//Programar los metodos

void Lista_listas::insertarCategoria(string _nameCategoria){
    bool flag;
    flag = whereIs(_nameCategoria);
    if(flag == true){
        return;
    }else{
    Categoria*  tmp = new Categoria(_nameCategoria);
    tmp->siguiente = cabecera;
    cabecera = tmp;
    }
}

void Lista_listas::insertarArticulo(string _categoria,int _id,string _name,int _precio, string _src){
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
    string rank = "";
    int i = 0;
    text+="node[shape=house,style=filled,color=peru,fontname=\"Century Gothic\"]; graph [fontname = \"Century Gothic\"];\n";
    text+="labelloc = \"t;\"label = \"Tienda BATTLESHIP\";\n";
    while(aux != NULL){
        text+="\nx"+aux->categoria+"[dir=both label = \"Categoria = "+(aux->categoria)+ "\",fontcolor=white]";
        text+="x"+(aux->categoria)+"-> x"+(aux->siguiente->categoria)+"\n";
        cout<<text<<endl;
            while(tmp != NULL){
                text+="\nx"+to_string(tmp->id)+"[dir=both label = \"Barco = "+(tmp->nombre)+ "\",  color=cyan4, shape=hexagon]";
                text+="x"+to_string(tmp->id)+"-> x"+to_string(tmp->abajo->id)+"\n";
        cout<<text<<endl;
                if(i == 0){
                    text+="x"+(aux->categoria)+"-> x"+to_string(tmp->id)+"\n";
                    rank+="x"+aux->categoria+";";
                    // cout<<"\n\n\n"+text<<endl;
                    i++;
                }
                    tmp = tmp->abajo;

                if(tmp->abajo == NULL){
                    text+="\nx"+to_string(tmp->id)+"[dir=both label = \"Barco = "+(tmp->nombre)+ "\",  color=cyan4, shape=hexagon]";
                    aux = aux->siguiente;
                    tmp = aux->abajo;
                    i=0;
                // cout<<"\n\n\n"+text<<endl;
                    break;
                }
        }

        if(aux->siguiente == NULL){
            text+="\nx"+aux->categoria+"[dir=both label = \"Categoria = "+(aux->categoria)+ "\",fontcolor=white]";
                // cout<<"\n\n\n"+text<<endl;
            
                while(tmp != NULL){
                    // tmp = aux->abajo;
                if(tmp->abajo == NULL){
                    text+="\nx"+to_string(tmp->id)+"[dir=both label = \"Barco = "+(tmp->nombre)+ "\",  color=cyan4, shape=hexagon]";
                    // cout<<"\n\n\n"+text<<endl;
                    break;
                }else{
                    text+="x"+to_string(tmp->id)+"[dir=both label = \"Barco = "+(tmp->nombre)+ "\",  color=cyan4, shape=hexagon]";
                    text+="x"+to_string(tmp->id)+"-> x"+to_string(tmp->abajo->id)+"\n";
                 if(i == 0){
                    text+="x"+(aux->categoria)+"-> x"+to_string(tmp->id)+"\n";
                    rank+="x"+aux->categoria+";";
                    // cout<<"\n\n\n"+text<<endl;
                    i++;
                }
                    tmp = tmp->abajo;

                }
            }
            text+=";\n{rank=same;"+rank+"};";
            texto_grafica = text;
            break;
        }
    }
    
}

bool Lista_listas::whereIs(string _name){
    Categoria* tmp = cabecera;
    if(tmp == NULL){
        return false;
    }
    while(tmp != NULL){
        if(tmp->categoria == _name){
            break;
            return true;
        }else{
            tmp = tmp->siguiente;
            if(tmp == cabecera){
                break;
                return false;
            }
        }
    }
}

void Lista_listas::crearGrafica(){
    report();
    string contenido = "digraph G {\n\n";
    string filename("archivos/Tienda.dot");
    fstream file_out;
    file_out.open(filename, std::ios_base::out);
    if (!file_out.is_open()) {
        cout << "failed to open " << filename << '\n';
    } else {
        contenido += texto_grafica;
        contenido +="\n}";
        file_out <<contenido<< endl;
        cout << "Done Writing!" << endl;
        system("dot -Tpng archivos/Tienda.dot -o archivos/Tienda.png");
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

void Lista_listas::show(int _tokens){
    Categoria* tmp = cabecera;
    cout<<"\t\t\t\t|\u001b[35mTOTAL TOKENS: \u001b[32m"<<_tokens<<"| \u001b[0m"<<endl;//7 tabs
    cout<<"\u001b[40;1m\u001b[33mTienda\u001b[37m"<<endl;
    cout<<"-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*-*-*-*-*-*-*-*-*-*-"<<endl;
    cout<<"| \u001b[36mId \t    \u001b[36m     Nombre \t\t\u001b[36mCategoria \t\u001b[36mPrecio\u001b[37m |"<<endl;
    cout<<"-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*-*-*-*-*-*-*-*-*-*-"<<endl;
    int i = 1;
    while (tmp != NULL){
        // cout<<"**********CATEGORIAS "+tmp->categoria+"**********"<<endl;
        Articulo* tmp2 = tmp->abajo;
        while(tmp2 != NULL){
            // cout<<"----Articulo"+tmp2->nombre<<endl;
            // cout<<"| "<<i+1<<"\t"<<tmp2->nombre<<"\t\t\t "<<tmp->categoria<<"\t\t"<<tmp2->precio<<"\t|"<<endl;
            // cout<<"| "<<i+1<<"\t"<<tmp2->nombre;
            cout<<"\u001b[40;1m|\u001b[33m  "<<tmp2->id<<" ";
            cout<<"\u001b[37m          "+tmp2->nombre;
            cout<<"\t\t\u001b[37m"+tmp->categoria;
            cout<<"\t\t \u001b[37m"<<tmp2->precio<<"    |"<<"\u001b[0m"<<endl;
            tmp2 = tmp2->abajo;
            i++;
        }
        tmp = tmp->siguiente;
    }
}

bool Lista_listas::comprar(int _id, int _monedas){
    Categoria* tmp = cabecera;
    Articulo* tmp2 = tmp->abajo;
    if(tmp == NULL){
        return false;
    }
    while(tmp2 != NULL){
        if(tmp2->id == _id){
            if(tmp2->precio > _monedas){
                return false;
            }else{
            return true;

            }
        }else{
            if(tmp2->abajo == NULL){
            tmp = tmp->siguiente;
                if(tmp == NULL){
                    return false;
                }else{

                tmp2 = tmp->abajo;
               }
            }else{
            tmp2 = tmp2->abajo;

            }

           
        }
    }
}
