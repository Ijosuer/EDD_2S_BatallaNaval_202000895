#include <iostream>
#include <fstream>
#include <jsoncpp/json/json.h>
#include <jsoncpp/json/value.h>
// #include <SHA256.h>

#include "Lista_Circular_Doble.cpp"
using namespace std;

//      --- COLORES ---
string RED = "\u001b[34;1m",GREEN ="\u001b[32m",YELLOW = "\u001b[33m",BLUE = "\u001b[34m";
string MAGENTA = "\u001b[35m",CYAN = "\u001b[36m",WHITE = "\u001b[37m",RESET = "\u001b[0m";
string BGblack = "\u001b[40;1m", BGr = "\u001b[0m";
//      --- ---- ---
 Lista_Circular_Doble lista;
void menu(){
    cout<<BGblack<<GREEN<<"***********"<<YELLOW<<" MENU "<<GREEN<<"************"<<WHITE<<BGr<<endl;
    cout<<BGblack<<"*                           *"<<BGr<<endl;
    cout<<BGblack<<"* 1."<<MAGENTA<<" Carga Masiva"<<WHITE<<"           *"<<BGr<<endl;
    cout<<BGblack<<"* 2."<<MAGENTA <<" Registrar Usuarios"<<WHITE<<"     *"<<BGr<<endl;
    cout<<BGblack<<"* 3."<<MAGENTA <<" Login             "<<WHITE<<"     *"<<BGr<<endl;
    cout<<BGblack<<"* 4."<<MAGENTA <<" Reportes          "<<WHITE<<"     *"<<BGr<<endl;
    cout<<BGblack<<"*"<<CYAN<<" -> Salir del juego        "<<WHITE<<"*"<<BGr<<endl;
    cout<<BGblack<<GREEN<<"*****************************"<<RESET<<BGr<<endl;
}

void crearSimple(){
    Lista_Circular_Doble lista;
    lista.insertarInicio("aux","123","1","20");
    lista.insertarInicio("Josue","EDD","2","21");
    lista.insertarInicio("Mike","mike123","3","18");
    lista.insertarInicio("Dany","dann3","4","30");
    lista.insertarInicio("Alexby","alex","5","5");
    lista.insertarInicio("Auronm","playas","6","150");
    // lista.verLista();
    lista.isPrimero();
    lista.isUltimo();
    // bool ans = lista.whereis("Josue");
    // lista.eliminarUltimo();
    // lista.eliminarUltimo();
    cout<<""<<endl;
    // lista.isPrimero();
    // lista.isUltimo();
    lista.crearGrafica();

}

void cargaMasiva(){
 Lista_Circular_Doble * lista_aux = NULL; //Con este crearemos usuarios
    lista_aux = &lista;

    // Let's parse it
    Json::Value root;
    Json::Reader reader;
    ifstream file("./archivo.json");
    bool parsedSuccess = reader.parse(file,root,false);

    if (not parsedSuccess) {
        // Report failures and their locations
        // in the document.
        cout << "Failed to parse JSON" << endl;
    }
    Json::Value::Members mem = root.getMemberNames();
    for (int j = 0; j < root.size(); j++){
    Json::Value child = root[mem[j]];
    cout<<mem[j]<<endl;
        for(auto& element : child){
            if (mem[j]=="articulos"){
                for (int i = 0; i < element.size(); i++){
                Json::Value::Members mem2 = element.getMemberNames();
                Json::Value child2 = element[mem2[i]];
                // cout << "name: " << mem2[i] << ", child: " << child2 << endl;
                // cout  << mem2[i] <<endl;
                    if(mem2[i] == "id"){
                        cout<<child2.asString();
                    }else if (mem2[i] == "categoria"){
                        cout<<" "+child2.asString();
                    }else if (mem2[i] == "precio"){
                        cout<<" "+child2.asString();
                    }else if (mem2[i] == "nombre"){
                        cout<<" "+child2.asString()<<endl;
                    }else if (mem2[i] == "src"){
                        cout<<" "+child2.asString()<<endl;
                    };
                }   
            }else if(mem[j] == "usuarios"){
                cout<<"\nENTRAMOS EN USUARIOS"<<endl;
                string edad,monedas,nick,password;

                for (int i = 0; i < element.size(); i++){
                Json::Value::Members mem2 = element.getMemberNames();
                Json::Value child2 = element[mem2[i]];
                    if(mem2[i] == "edad"){
                    cout<<child2.asString();
                    edad = child2.asString();
                    }else if (mem2[i] == "monedas"){
                        cout<<" "+child2.asString();
                    monedas = child2.asString();
                    }else if (mem2[i] == "nick"){
                        cout<<" "+child2.asString();
                    nick = child2.asString();
                    }else if (mem2[i] == "password"){
                        cout<<" "+child2.asString()<<endl;
                    password = child2.asString();

                        //Creando primer usuario
                        lista_aux->insertarInicio(nick,password,monedas,edad);
                        
                    };
                }
            }else if(mem[j] == "tutorial"){
                cout<<"-> Entramos en tutorial"<<child.size()<<endl;
                    Json::Value::Members mem2 = child.getMemberNames();
                for (int i = 0; i < child.size(); i++){
                    Json::Value child2 = child[mem2[i]];
                        if(mem2[i] == "ancho"){
                            cout<<" "+child2.asString()<<endl;
                        }else if(mem2[i] == "alto"){
                            cout<<" "+child2.asString()<<endl;
                        }else if(mem2[i] == "movimientos"){
                            cout<<"Entramos en moves"<<endl;
                            cout<<child2.size()<<endl;
                            for(auto& element : child2){
                                for (int i = 0; i < element.size(); i++){
                                    Json::Value::Members mem2 = element.getMemberNames();
                                    Json::Value child3 = element[mem2[i]];
                                    if(mem2[i] == "x"){
                                    cout<<"X: "+child3.asString();
                                    }else if(mem2[i] == "y"){
                                    cout<<"Y: "+child3.asString()<<endl;;
                                    }
                                }
                            }
                        }
                }
                break;

            }
        }
    }
    
    // cout << "name: " << mem[2] << ", child: " << child << endl;
    // cout<<"\n"<<endl;
    
//    cout << element << endl;
}

// void crearQueue(){}

int main(){
    // crearSimple();
    // menu();
    cargaMasiva();
    //Creamos mas nodos apuntando a la lista circular global
    Lista_Circular_Doble * lista2 = NULL;
    lista2 = &lista; 
    lista.insertarInicio("aux","123","1","20");
    lista2->insertarInicio("mike","ipc","3","0");
    lista.crearGrafica();
    return 1;
}