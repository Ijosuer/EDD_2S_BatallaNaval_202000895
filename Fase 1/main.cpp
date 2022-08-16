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

void leerJson(){
    // Let's parse it
    Json::Value root;
    Json::Reader reader;
    ifstream file("./prueba.json");
    bool parsedSuccess = reader.parse(file,root,false);

    if (not parsedSuccess) {
        // Report failures and their locations
        // in the document.
        cout << "Failed to parse JSON" << endl
             << reader.getFormatedErrorMessages()
             << endl;
    }
    Json::Value::Members mem = root.getMemberNames();
    for (int i = 0; i < root.size(); i++){
    Json::Value child = root[mem[i]];
        for(auto& element : child){
            for (int i = 0; i < element.size(); i++){
                /* code */
            Json::Value::Members mem2 = element.getMemberNames();
            Json::Value child2 = element[mem2[i]];
            // cout << "name: " << mem2[i] << ", child: " << child2 << endl;
            // cout  << mem2[i] << ": " << child2.asString() << endl;
                if(mem2[i] == "id"){
                    cout<<child2.asString();
                }else if (mem2[i] == "nombre"){
                    cout<<" "+child2.asString();
                }else if (mem2[i] == "categoria"){
                    cout<<" "+child2.asString();
                }else if (mem2[i] == "precio"){
                    cout<<" "+child2.asString();
                }else if (mem2[i] == "src"){
                    cout<<" "+child2.asString()<<endl;
                }else if (mem2[i] == "nick"){
                    cout<<" "+child2.asString();
                }else if (mem2[i] == "password"){
                    cout<<" "+child2.asString()<<endl;
                }else if (mem2[i] == "monedas"){
                    cout<<" "+child2.asString();
                }else if (mem2[i] == "edad"){
                    cout<<"\n"+child2.asString();
                }
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
    leerJson();
    return 1;
}