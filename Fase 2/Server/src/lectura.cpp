#include <iostream>
#include <fstream>
#include <unistd.h>
#include "/home/ijosuer/Escritorio/EDD_2S_BatallaNaval_202000895/Fase 1/jsoncpp.cpp"

using namespace std;

class Compra{
    
    public:
        string idCompra,nombre;
        int cantidad;
        Compra(string,string,int);
        Compra() = default;
        ~Compra();
    private:
};

Compra::Compra(string _idCompra, string _nombre, int _cantidad){
    idCompra = _idCompra;
    nombre = _nombre;
    cantidad = _cantidad; 
}

Compra::~Compra(){

}

int correlativo = 1;
class NodoAVL{
public:
   
    Compra compra;
    int id;
    int altura;
    
    NodoAVL* izquierda;
    NodoAVL* derecha;
    

    NodoAVL(Compra _compra) {
        compra = _compra;
        izquierda = NULL;
        derecha = NULL;
        altura = 0;
        id = correlativo++;
    }
private:
};

class AVL {
public:
    NodoAVL* raiz;

    AVL() {
        raiz = NULL;
    }
    
    int MAXIMO(int valor1, int valor2);
    int altura(NodoAVL* nodo);
    void insertar(Compra compra);
    NodoAVL* add(Compra compra, NodoAVL* nodo);
    NodoAVL* rotacionizquierda(NodoAVL* nodo);
    NodoAVL* rotacionderecha(NodoAVL* nodo);
    NodoAVL* rotaciondoblederecha(NodoAVL* nodo);
    NodoAVL* rotaciondobleizquierda(NodoAVL* nodo);
    void mostrarOrdenDescendente();
    NodoAVL* in_orden(NodoAVL* nodo);
    void graficar();
    string getCodigoInterno(NodoAVL* nodo);
private:
};
  
int AVL::MAXIMO(int valor1, int valor2){
    if(valor1>valor2){
        return valor1;
    }else{
        return valor2;
    }
}

int AVL::altura(NodoAVL* nodo){
    if(nodo == NULL){
        return -1;
    }else{
        return nodo->altura;
    }
}

void AVL::insertar(Compra compra){
    raiz = add(compra, raiz); 
}

NodoAVL* AVL::add(Compra compra, NodoAVL* nodo){
    if(nodo == NULL){
        return new NodoAVL(compra);
    }else{
        if(compra.idCompra < nodo->compra.idCompra){
            nodo->izquierda = add(compra, nodo->izquierda);
            if(altura(nodo->derecha)-altura(nodo->izquierda)== -2){
                if(compra.idCompra < nodo->izquierda->compra.idCompra){
                    nodo = rotacionizquierda(nodo);
                }else{
                    nodo = rotaciondobleizquierda(nodo);
                }
            }
        }else if(compra.idCompra > nodo->compra.idCompra){
            nodo->derecha = add(compra, nodo->derecha);
            if(altura(nodo->derecha)-altura(nodo->izquierda)== 2){
                if(compra.idCompra > nodo->derecha->compra.idCompra){
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

NodoAVL* AVL::rotacionizquierda(NodoAVL *nodo){
    NodoAVL* aux = nodo->izquierda;
    nodo->izquierda = aux->derecha;
    aux->derecha = nodo;

    nodo->altura = MAXIMO(altura(nodo->derecha),altura(nodo->izquierda))+1;
    aux->altura = MAXIMO(altura(nodo->izquierda), nodo->altura)+1;
    return aux;
}

NodoAVL* AVL::rotacionderecha(NodoAVL* nodo){
    NodoAVL* aux = nodo->derecha;
    nodo->derecha = aux->izquierda;
    aux->izquierda = nodo;

    nodo->altura = MAXIMO(altura(nodo->derecha),altura(nodo->izquierda))+1;
    aux->altura = MAXIMO(altura(nodo->derecha), nodo->altura)+1;
    return aux;
}

NodoAVL* AVL::rotaciondoblederecha(NodoAVL* nodo){
    nodo->derecha = rotacionizquierda(nodo->derecha);
    return rotacionderecha(nodo);
}

NodoAVL* AVL::rotaciondobleizquierda(NodoAVL* nodo){
    nodo->izquierda = rotacionderecha(nodo->izquierda);
    return rotacionizquierda(nodo);
}

void AVL::graficar(){
    string codigodot = "";
    codigodot += "digraph G{label = \"Arbol AVL\" fontname=\"Arial Black\" fontsize=\"25pt\";\nnode [shape = circle, style=filled, fillcolor=seashell2];\n"+ getCodigoInterno(raiz)+"\n}"; 
        
    //cout << codigodot;
    //------->escribir archivo
    ofstream file;
    file.open("../archivos/AVL.dot");
    file << codigodot;
    file.close();
    //------->generar png
    system(("dot -Tpng AVL.dot -o  ../archivos/AVL.png"));

    //------>abrir archivo
    system(("../archivos/AVL.png"));
}

string AVL::getCodigoInterno(NodoAVL* nodo){
    string codigodot = "";
        
    if((nodo->izquierda== NULL) && (nodo->derecha == NULL)){
        codigodot += "nodo" + std::to_string(nodo->id)+ "[ label = \""+ nodo->compra.idCompra +"\n"+ nodo->compra.nombre +"\n"+ to_string(nodo->compra.cantidad)+"\""+ "];\n";
    }else{
        codigodot += "nodo" +std::to_string(nodo->id)+"[ label = \""+  nodo->compra.idCompra +"\n"+ nodo->compra.nombre +"\n"+ to_string(nodo->compra.cantidad)+"\""+"];\n";
    }
    if(nodo->izquierda!=NULL){
        codigodot+= getCodigoInterno(nodo->izquierda) +"nodo"+std::to_string(nodo->id) + ":C0->nodo" + std::to_string(nodo->izquierda->id)+"\n";
    }
    if(nodo->derecha!=NULL){
        codigodot+= getCodigoInterno(nodo->derecha)+"nodo"+std::to_string(nodo->id)+":C1->nodo"+std::to_string(nodo->derecha->id)+"\n";                    
    }
    return codigodot;
}

// ------------------------------------//
AVL pruebas;
Compra compra;
void cargaMasiva(string _ruta){
    // Let's parse it
    Json::Value root;
    Json::Reader reader;
    ifstream file(_ruta);
    bool parsedSuccess = reader.parse(file,root,false);

    if (not parsedSuccess) {
        // Report failures and their locations
        // in the document.
        std::cout << "Failed to parse JSON" << endl;
    }
    Json::Value::Members mem = root.getMemberNames();
    int contador = 0;
    for (int j = 0; j < root.size(); j++){
    Json::Value child = root[mem[j]];
        for(auto& element : child){
            if (mem[j]=="articulos"){
                string id, categoria,precio,nombre,src = "";
                for (int i = 0; i < element.size(); i++){
                Json::Value::Members mem2 = element.getMemberNames();
                Json::Value child2 = element[mem2[i]];
                // cout << "name: " << mem2[i] << ", child: " << child2 << endl;
                // cout  << mem2[i] <<endl;
                    if(mem2[i] == "id"){
                        id = child2.asString();
                    }else if (mem2[i] == "categoria"){
                        categoria = child2.asString();
                        // lista_listas.insertarCategoria(categoria);
                    }else if (mem2[i] == "precio"){
                        precio = child2.asString();
                    }else if (mem2[i] == "nombre"){
                        nombre= child2.asString();
                    }else if (mem2[i] == "src"){
                        contador+=1;
                        std::cout<<contador<<endl;
                        src = child2.asString();
                        int id_ok = stoi(id);
                        int precio_ok = stoi(precio);
                        compra = Compra(id,nombre,precio_ok);
                        pruebas.insertar(compra);
                        // lista_listas.insertarArticulo(categoria,id_ok,nombre,precio_ok,src);

                    };
                }   
            }else if(mem[j] == "usuarios"){
                string edad,monedas,nick,password;

                for (int i = 0; i < element.size(); i++){
                Json::Value::Members mem2 = element.getMemberNames();
                Json::Value child2 = element[mem2[i]];
                    if(mem2[i] == "edad"){
                    edad = child2.asString();
                    }else if (mem2[i] == "monedas"){
                    monedas = child2.asString();
                    }else if (mem2[i] == "nick"){
                    nick = child2.asString();
                    }else if (mem2[i] == "password"){
                    password = child2.asString();

                        //Creando primer usuario
                        int edad_ok = std::stoi(edad);
                        int monedas_ok =  std::stoi(monedas);
                        // lista_aux->insertarInicio(nick,password,monedas_ok,edad_ok);
                        // listaUsuariosaux.ingresarUsuario(nick,edad_ok);
                        
                    };
                }
            }else if(mem[j] == "tutorial"){
                string ancho,alto,x,y = "";
                int iterator=1;
                    Json::Value::Members mem2 = child.getMemberNames();
                for (int i = 0; i < child.size(); i++){
                    Json::Value child2 = child[mem2[i]];
                        if(mem2[i] == "ancho"){
                            ancho = child2.asString(); //ancho
                        }else if(mem2[i] == "alto"){
                            alto = child2.asString(); //alto
                        }else if(mem2[i] == "movimientos"){
                            // cola.Enqueue(iterator,ancho,alto);
                            iterator++;
                            for(auto& element : child2){
                                for (int i = 0; i < element.size(); i++){
                                    Json::Value::Members mem2 = element.getMemberNames();
                                    Json::Value child3 = element[mem2[i]];
                                    if(mem2[i] == "x"){
                                    x = child3.asString(); //coordenada X
                                    std::cout<<x<<endl;
                                    }else if(mem2[i] == "y"){
                                    y = child3.asString(); //coordenada Y
                                    std::cout<<y<<endl;
                                    // cola.Enqueue(iterator,x,y);
                                    iterator++;
                                    }
                                }
                            }
                        }
                }
                break;

            }
        }
    }
    pruebas.graficar();
}


int main(){
    cargaMasiva("/home/ijosuer/Escritorio/EDD_2S_BatallaNaval_202000895/Fase 1/archivos/ArchivoPrueba.json");
//     compra = Compra("1","hola",2);
//     pruebas.insertar(compra);
//     compra = Compra("2","adios",58);
//     pruebas.insertar(compra);
//     compra = Compra("3","kk",96);
//     pruebas.insertar(compra);
//     compra = Compra("4","a",0);
//     pruebas.insertar(compra);
//     compra = Compra("5","fas",88);
//     pruebas.insertar(compra);
//     compra = Compra("6","kru",7777);
//     pruebas.insertar(compra);
//     compra = Compra("7","r7777",222);
//     pruebas.insertar(compra);
//     compra = Compra("8","y",50);
//     pruebas.insertar(compra);
//     compra = Compra("9","arriba",50);
//     pruebas.insertar(compra);
//     compra = Compra("10","derecha",50);
//     pruebas.insertar(compra);
//     compra = Compra("11","idk",50);
//     pruebas.insertar(compra);
//     compra = Compra("12","a",50);
//     pruebas.insertar(compra);
//     compra = Compra("13","af",50);
//     pruebas.insertar(compra);
//     pruebas.graficar();
    
    return 1;
}