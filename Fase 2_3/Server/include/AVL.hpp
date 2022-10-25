#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <map>
//Esta clase deberia de estar en el src

// #include "../lib/crow_all.h"
using namespace std;

class Compra{
    
    public:
        string categoria,nombre;
        int cantidad,idCompra;
        
        Compra* izquierda;
        Compra* derecha;
int altura;
        Compra(int _id,string _name,int _cant){
            idCompra = _id;
            nombre = _name;
            cantidad = _cant;
            izquierda = NULL;
            derecha = NULL;
        }
    private:
};

int correlativo = 1;

class AVL {
public:
    // int altura;
    

    Compra* raiz;

    AVL() {
        raiz = NULL;
    }
    void hablar();
    int MAXIMO(int valor1, int valor2);
    int altura(Compra* nodo);
    void insertar(Compra compra);
    Compra* add(Compra compra, Compra* nodo);
    Compra* rotacionizquierda(Compra* nodo);
    Compra* rotacionderecha(Compra* nodo);
    Compra* rotaciondoblederecha(Compra* nodo);
    Compra* rotaciondobleizquierda(Compra* nodo);
    Compra* buscar(Compra* nodo , int _id);
    void mostrarOrdenDescendente(Compra* asd);
    Compra* in_orden(Compra* nodo);
    void graficar();
    string getCodigoInterno(Compra* nodo);
private:
};
  
int AVL::MAXIMO(int valor1, int valor2){
    if(valor1>valor2){
        return valor1;
    }else{
        return valor2;
    }
}

int AVL::altura(Compra* nodo){
    if(nodo == NULL){
        return -1;
    }else{
        return nodo->altura;
    }
}

void AVL::insertar(Compra compra){
    raiz = add(compra, raiz); 
}

Compra* AVL::add(Compra compra, Compra* nodo){
    if(nodo == NULL){
        return new Compra(compra);
    }else{
        if(compra.idCompra < nodo->idCompra){
            nodo->izquierda = add(compra, nodo->izquierda);
            if(altura(nodo->derecha)-altura(nodo->izquierda)== -2){
                if(compra.idCompra < nodo->izquierda->idCompra){
                    nodo = rotacionizquierda(nodo);
                }else{
                    nodo = rotaciondobleizquierda(nodo);
                }
            }
        }else if(compra.idCompra > nodo->idCompra){
            nodo->derecha = add(compra, nodo->derecha);
            if(altura(nodo->derecha)-altura(nodo->izquierda)== 2){
                if(compra.idCompra > nodo->derecha->idCompra){
                    nodo = rotacionderecha(nodo);
                }else{
                    nodo = rotaciondoblederecha(nodo);
                }
            }
        }else{
            std::cout << "No se puede agregar";
        }
    }
    nodo->altura = MAXIMO(altura(nodo->izquierda),altura(nodo->derecha))+1;
    return nodo;
}

Compra* AVL::rotacionizquierda(Compra *nodo){
    Compra* aux = nodo->izquierda;
    nodo->izquierda = aux->derecha;
    aux->derecha = nodo;

    nodo->altura = MAXIMO(altura(nodo->derecha),altura(nodo->izquierda))+1;
    aux->altura = MAXIMO(altura(nodo->izquierda), nodo->altura)+1;
    return aux;
}

Compra* AVL::rotacionderecha(Compra* nodo){
    Compra* aux = nodo->derecha;
    nodo->derecha = aux->izquierda;
    aux->izquierda = nodo;

    nodo->altura = MAXIMO(altura(nodo->derecha),altura(nodo->izquierda))+1;
    aux->altura = MAXIMO(altura(nodo->derecha), nodo->altura)+1;
    return aux;
}

Compra* AVL::rotaciondoblederecha(Compra* nodo){
    nodo->derecha = rotacionizquierda(nodo->derecha);
    return rotacionderecha(nodo);
}

Compra* AVL::rotaciondobleizquierda(Compra* nodo){
    nodo->izquierda = rotacionderecha(nodo->izquierda);
    return rotacionizquierda(nodo);
}
void AVL::mostrarOrdenDescendente(Compra* pivote){
    if(pivote!=nullptr){
        mostrarOrdenDescendente(pivote->izquierda);
        cout<<pivote->idCompra <<endl;
        mostrarOrdenDescendente(pivote->derecha);
    }

}
Compra* AVL::buscar(Compra *pivote , int _id){
    if(pivote!=nullptr){
        buscar(pivote->izquierda,_id);
        if(pivote->idCompra == _id){
            return pivote;
        }else{
        buscar(pivote->derecha, _id);
        }
    }

}
void AVL::graficar(){
    string codigodot = "";
    codigodot += "digraph G{label = \"Arbol AVL\" fontname=\"Arial Black\" fontsize=\"25pt\";\nnode [shape = circle, style=filled, fillcolor=seashell2];\n"+ getCodigoInterno(raiz)+"\n}"; 
        
    //cout << codigodot;
    //------->escribir archivo
    ofstream file;
    file.open("/home/ijosuer/Escritorio/EDD_2S_BatallaNaval_202000895/archivos/AVL.dot");
    file << codigodot;
    file.close();
    //------->generar png
    system(("dot -Tpng /home/ijosuer/Escritorio/EDD_2S_BatallaNaval_202000895/archivos/AVL.dot -o  /home/ijosuer/Escritorio/EDD_2S_BatallaNaval_202000895/archivos/AVL.png"));

    //------>abrir archivo
    // system(("/home/ijosuer/Escritorio/EDD_2S_BatallaNaval_202000895/archivos/AVL.png"));
    // mostrarOrdenDescendente(raiz);
}

string AVL::getCodigoInterno(Compra* nodo){
    string codigodot = "";
        
    if((nodo->izquierda== NULL) && (nodo->derecha == NULL)){
        codigodot += "nodo" + std::to_string(nodo->idCompra)+ "[ label = \""+ to_string(nodo->idCompra) +"\n"+ nodo->nombre +"\n"+ to_string(nodo->cantidad)+"\""+ "];\n";
    }else{
        codigodot += "nodo" +std::to_string(nodo->idCompra)+"[ label = \""+  to_string(nodo->idCompra) +"\n"+ nodo->nombre +"\n"+ to_string(nodo->cantidad)+"\""+"];\n";
    }
    if(nodo->izquierda!=NULL){
        codigodot+= getCodigoInterno(nodo->izquierda) +"nodo"+std::to_string(nodo->idCompra) + ":C0->nodo" + std::to_string(nodo->izquierda->idCompra)+"\n";
    }
    if(nodo->derecha!=NULL){
        codigodot+= getCodigoInterno(nodo->derecha)+"nodo"+std::to_string(nodo->idCompra)+":C1->nodo"+std::to_string(nodo->derecha->idCompra)+"\n";                    
    }
    return codigodot;
}
