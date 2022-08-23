#include <iostream>
#include <fstream>
#include <string>
#include "json/json.h"
#include "jsoncpp.cpp"
// #include <SHA256.h>
#include <unistd.h>

#include "Lista_Circular_Doble.cpp"
#include "Lista_listas.cpp"
#include "Cola.cpp"
#include "Stack.cpp"
using namespace std;

//      --- COLORES ---
string RED = "\u001b[31m",GREEN ="\u001b[32m",YELLOW = "\u001b[33m",BLUE = "\u001b[34m";
string MAGENTA = "\u001b[35m",CYAN = "\u001b[36m",WHITE = "\u001b[37m",RESET = "\u001b[0m";
string BGblack = "\u001b[40;1m", BGr = "\u001b[0m";
//      --- ---- ---

//Instancias de estructuras
Lista_Circular_Doble lista;
Lista_listas lista_listas;
Cola cola;
Stack pila;
// ****------****

void menu(){
    cout<<BGblack<<GREEN<<"*********"<<YELLOW<<"🎮 MENU 💣"<<GREEN<<"**********"<<WHITE<<BGr<<endl;
    cout<<BGblack<<"*                           *"<<BGr<<endl;
    cout<<BGblack<<"* 1."<<MAGENTA<<" Carga Masiva"<<WHITE<<"           *"<<BGr<<endl;
    cout<<BGblack<<"* 2."<<MAGENTA <<" Registrar Usuarios"<<WHITE<<"     *"<<BGr<<endl;
    cout<<BGblack<<"* 3."<<MAGENTA <<" Login             "<<WHITE<<"     *"<<BGr<<endl;
    cout<<BGblack<<"* 4."<<MAGENTA <<" Reportes          "<<WHITE<<"     *"<<BGr<<endl;
    cout<<BGblack<<"*"<<CYAN<<" 5.  Salir del juego       "<<WHITE<<"*"<<BGr<<endl;
    cout<<BGblack<<GREEN<<"*****************************"<<RESET<<BGr<<endl;
}

void reportes_menu(){
    cout<<BGblack<<WHITE<<"********"<<YELLOW<<"📝 Reportes "<<WHITE<<"********"<<WHITE<<BGr<<endl;
    cout<<BGblack<<"*                             *"<<BGr<<endl;
    cout<<BGblack<<"* 1."<<BLUE<<" Visualizar Graphviz"<<WHITE<<"       *"<<BGr<<endl;
    cout<<BGblack<<"* 2."<<BLUE <<" Listado de Usuarios [edad]"<<WHITE<<"          *"<<BGr<<endl;
    cout<<BGblack<<"* 3."<<BLUE <<" Listado de Articulos [precios]"<<WHITE<<"          *"<<BGr<<endl;
    cout<<BGblack<<"* 4."<<CYAN<<" Regresar                 "<<WHITE<<"*"<<BGr<<endl;
    cout<<BGblack<<YELLOW<<"*******************************"<<RESET<<BGr<<endl;

}

void login(){
    cout<<BGblack<<YELLOW<<"*------"<<MAGENTA<<" 💥BATTLESHIP💥 "<<YELLOW<<"-------*"<<WHITE<<BGr<<endl;
    cout<<BGblack<<"*                             *"<<BGr<<endl;
    cout<<BGblack<<"* 1."<<BLUE<<" Editar informacion"<<WHITE<<"       *"<<BGr<<endl;
    cout<<BGblack<<"* 2."<<BLUE <<" Eliminar cuenta"<<WHITE<<"          *"<<BGr<<endl;
    cout<<BGblack<<"* 3."<<BLUE <<" Ver el tutorial      "<<WHITE<<"    *"<<BGr<<endl;
    cout<<BGblack<<"* 4."<<BLUE <<" Ir a la Tienda      "<<WHITE<<"     *"<<BGr<<endl;
    cout<<BGblack<<"* 5."<<BLUE<<" Realizar movimientos     "<<WHITE<<"*"<<BGr<<endl;
    cout<<BGblack<<"*"<<CYAN<<" 6. Regresar                 "<<WHITE<<"*"<<BGr<<endl;
    cout<<BGblack<<YELLOW<<"*******************************"<<RESET<<BGr<<endl;
}

void tutorial_menu(){
Nodo* tmp = cola.primero;
cout<<BGblack<<YELLOW<<"********"<<MAGENTA<<"👾 Tutorial "<<YELLOW<<"********"<<WHITE<<BGr<<endl;
    cout<<" "<<CYAN<<"Tablero:"<<WHITE<<endl;
    cout<<"    "<<BLUE<<"Ancho:"<<WHITE+" "+tmp->x<<endl;
    cout<<"    "<<BLUE<<"Alto:"<<WHITE+" "+tmp->y<<endl;
    cout<<" "<<CYAN<<"Movimientos:"<<WHITE<<endl;
    cola.show();
    cout<<BGblack<<YELLOW<<"*******************************\n"<<RESET<<BGr<<endl;
}

void cargaMasiva(string _ruta){
 Lista_Circular_Doble * lista_aux = NULL; //Con este crearemos usuarios
    lista_aux = &lista;

    // Let's parse it
    Json::Value root;
    Json::Reader reader;
    ifstream file(_ruta);
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
                        lista_listas.insertarCategoria(categoria);
                    }else if (mem2[i] == "precio"){
                        precio = child2.asString();
                    }else if (mem2[i] == "nombre"){
                        nombre= child2.asString();
                    }else if (mem2[i] == "src"){
                        src = child2.asString();
                        lista_listas.insertarArticulo(categoria,id,nombre,precio,src);
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
                string ancho,alto,x,y = "";

                cout<<"-> Entramos en tutorial"<<child.size()<<endl;
                    Json::Value::Members mem2 = child.getMemberNames();
                for (int i = 0; i < child.size(); i++){
                    Json::Value child2 = child[mem2[i]];
                        if(mem2[i] == "ancho"){
                            cout<<" "+child2.asString()<<endl;
                            ancho = child2.asString(); //ancho
                        }else if(mem2[i] == "alto"){
                            cout<<" "+child2.asString()<<endl;
                            alto = child2.asString(); //alto
                        }else if(mem2[i] == "movimientos"){
                            cola.Enqueue(ancho,alto);
                            cout<<"Entramos en moves"<<endl;
                            cout<<child2.size()<<endl;
                            for(auto& element : child2){
                                for (int i = 0; i < element.size(); i++){
                                    Json::Value::Members mem2 = element.getMemberNames();
                                    Json::Value child3 = element[mem2[i]];
                                    if(mem2[i] == "x"){
                                    cout<<"X: "+child3.asString();
                                    x = child3.asString(); //coordenada X
                                    }else if(mem2[i] == "y"){
                                    cout<<"Y: "+child3.asString()<<endl;;
                                    y = child3.asString(); //coordenada Y
                                    cola.Enqueue(x,y);
                                    }
                                }
                            }
                        }
                }
                break;

            }
        }
    }
    
}

//eliminar despues
void llamadas(){
cargaMasiva("archivos/archivo.json");
    //Creamos mas nodos apuntando a la lista circular global
    Lista_Circular_Doble * lista2 = NULL;
    lista2 = &lista; 
    lista.insertarInicio("aux","123","1","20");
    lista2->insertarInicio("mike","ipc","3","0");
    lista.crearGrafica();
    cola.crearGrafica();
    cout<<"SHJOOOOOOOOO"<<endl;
    pila.push("10","10");
    pila.push("20","2");
    pila.push("30","30");
    pila.pop();
    pila.pop();
    pila.peek();
}

void iniciarJuego(){
menu();
    string op;//maneja menu
    string nickname, edad,pwd ="";//new usuario
    string newNickname,newPwd,newEdad = "";//editar info

    bool flag = false;
    cout<<"Ingrese una opcion"<<endl;
    cin >> op;
    while(op != "5" ){
        if(op == "1"){//Carga Masiva
            cargaMasiva("archivos/ArchivoPrueba.json");
            menu();
            cout<<GREEN+"Ingrese una opcion"+RESET<<endl;
            cin >> op;
        }else if(op == "2"){//Registro de usuario
            // menuRegistro();
            cout<<BGblack<<GREEN<<"*****"<<YELLOW<<" Registar Usuario "<<GREEN<<"******"<<WHITE<<BGr<<endl;
            cout<<"\n";
            cout<<WHITE<<"->"<<"Ingrese Nickname: "+CYAN;
            cin >> nickname;
            cout<<WHITE<<"->"<<"Ingrese Pwd: "+CYAN;
            cin >> pwd;
            cout<<WHITE<<"->"<<"Ingrese Edad: "+CYAN;
            cin >> edad;

            //Llamar al metodo agrega usuarios
            lista.insertarInicio(nickname,pwd,"0",edad);
            cout<<BGblack<<BLUE+"\n✅ Usuario "+GREEN+nickname+BLUE+" agregado con exito!"<<BGr<<"\n"<<endl;
            menu();
            cout<<GREEN+"Ingrese una opcion"+RESET<<endl;
            cin >> op;

        }else if(op == "3"){ //Loginssss
            cout<<BGblack<<GREEN<<"*****"<<YELLOW<<" Iniciar Sesion "<<GREEN<<"******"<<WHITE<<BGr<<endl;
            cout<<"\n";
            cout<<WHITE<<"->"<<"Ingrese Nickname: "+CYAN;
            cin >> nickname;
            cout<<WHITE<<"->"<<"Ingrese Pwd: "+CYAN;
            cin >> pwd;
            
            //Llamar al metodo busca usuarios
            flag = lista.whereis(nickname,pwd);
        
            if(flag == true){
                cout<<BGblack<<BLUE+"\n✅ Bienvenido al sistema "+GREEN+nickname<<BGr+"\n"<<endl;
                login();
                cout<<GREEN+"Ingrese una opcion"+RESET<<endl;
                cin >> op;
                while(op != "6"){
                    if(op == "1"){
                        edad = lista.dataEdad(nickname);
                        cout<<BGblack<<WHITE<<"*****"<<YELLOW<<" Editar Datos "<<WHITE<<"******"<<WHITE<<BGr<<endl;
                        cout<<BGblack<<"* "<<BLUE<<" Nickname: "<<WHITE<<nickname<<BGr<<endl;
                        cout<<BGblack<<"* "<<BLUE<<" Edad: "<<WHITE<<edad<<BGr<<endl;
                        cout<<BGblack<<"* "<<BLUE<<" Password: "<<WHITE<<pwd<<BGr<<endl;
                        cout<<BGblack<<YELLOW<<"*************************"<<RESET<<BGr<<endl;
                        cout<<WHITE<<"->"<<"Ingrese nuevo Nickname: "+CYAN;
                        cin >> newNickname;
                        cout<<WHITE<<"->"<<"Ingrese nueva Edad: "+CYAN;
                        cin >> newEdad;
                        cout<<WHITE<<"->"<<"Ingrese nueva Password: "+CYAN;
                        cin >> newPwd;
                        cout<<BGblack<<WHITE<<"\n*****"<<YELLOW<<" Editar Datos "<<WHITE<<"******"<<WHITE<<BGr<<endl;
                        cout<<BGblack<<"* "<<BLUE<<" Nickname: "<<WHITE<<newNickname<<BGr<<endl;
                        cout<<BGblack<<"* "<<BLUE<<" Edad: "<<WHITE<<newEdad<<BGr<<endl;
                        cout<<BGblack<<"* "<<BLUE<<" Password: "<<WHITE<<newPwd<<BGr<<endl;
                        cout<<BGblack<<YELLOW<<"*************************"<<RESET<<BGr<<endl;
                        bool ans =lista.editar(nickname,newNickname,newPwd,newEdad);
                        if (ans == true){
                            nickname = newNickname;
                            edad = newEdad;
                            pwd = newPwd;
                            cout<<BGblack<<BLUE+"✅ Cambio exitoso "+GREEN+nickname<<BGr+"\n"<<endl;
                            login();
                            cout<<GREEN+"Ingrese una opcion"+RESET<<endl;
                            cin >> op;
                        }else{
                            cout<<RED+"ERROR al cambiar los datos! 💢\n"<<endl;
                            login();
                            cout<<GREEN+"Ingrese una opcion"+RESET<<endl;
                            cin >> op;
                        }

                    }else if(op == "2"){
                        string ans = "";
                        cout<<RED+"\n🚩Desea eliminar su cuenta de manera permanente "+WHITE+"["+RED+"s"+WHITE+"/"+RED+"n"+WHITE+"] : ";
                        cin>>ans;
                        if(ans == "s"){
                            ans = "";
                            lista.eliminarUsuario(nickname);
                            break;
                            menu();
                            cout<<GREEN+"Ingrese una opcion"+RESET<<endl;
                            cin >> op;

                        }else if(ans == "n"){
                            ans = "";
                            cout<<BGblack<<BLUE+"\n😎 OK tu cuenta no sera eliminada "<<BGr+"\n"<<endl;
                            login();
                            cout<<GREEN+"Ingrese una opcion"+RESET<<endl;
                            cin >> op;
                        }else{
                            ans = "";
                            cout<<RED+"\nIngrese un comando valido! 💢\n"<<endl;
                            cout<<RED+"\n🚩⚠️Desea eliminar su cuenta de manera permanente "+WHITE+"["+RED+"s"+WHITE+"/"+RED+"n"+WHITE+"] : ";
                            cin>>ans;
                        }
                    }else if(op == "3"){
                        cout<<">Desplegar ver tutorial"<<endl;
                        tutorial_menu();
                        cout<<GREEN+"Ingrese una opcion"+RESET<<endl;
                        cin >> op;
                    }else if(op == "4"){
                        string monedas = "";
                        monedas= lista.cuantasFichas(nickname);
                        if (monedas != ""){
                            lista_listas.show(monedas);
                            login();
                            cout<<GREEN+"Ingrese una opcion"+RESET<<endl;
                            cin >> op;
                        }else{
                            cout<<RED+"\nNO puede ingresar a la tienda 💢\n"<<endl;
                            login();
                            cout<<GREEN+"Ingrese una opcion"+RESET<<endl;
                            cin >> op;
                        }
                    }else if(op == "5"){
                        cout<<">Hacer movimientos"<<endl;
                        login();
                        cout<<GREEN+"Ingrese una opcion"+RESET<<endl;
                        cin >> op;
                    }else{
                        cout<<RED+"Ingrese un comando valido! 💢\n"<<endl;
                        login();
                        cout<<GREEN+"Ingrese una opcion"+RESET<<endl;
                        cin >> op;
                    }
                }
                menu();
                cout<<GREEN+"Ingrese una opcion"+RESET<<endl;
                cin >> op;
            }else{
                cout<<RED+"\n🔒Credenciales incorrectas❗\n"<<endl;
                menu();
                cout<<GREEN+"Ingrese una opcion"+RESET<<endl;
                cin >> op;
            }
        }else if(op == "4"){ //Reportes
            reportes_menu();
            cout<<GREEN+"Ingrese una opcion"+RESET<<endl;
            cin >> op;
            while(op != "4"){
                if(op == "1"){
                    cout<<BGblack<<BLUE+"✅ Cambio exitoso "+GREEN+nickname<<BGr+"\n"<<endl;

                    reportes_menu();
                    cout<<GREEN+"Ingrese una opcion"+RESET<<endl;
                    cin >> op;
                }else if(op == "2"){
                    cout<<BGblack<<BLUE+"Listando Usuarios por edad ⬆️ "+GREEN+nickname<<BGr+"\n"<<endl;
                    reportes_menu();
                    cout<<GREEN+"Ingrese una opcion"+RESET<<endl;
                    cin >> op;
                }else if(op == "3"){
                    cout<<BGblack<<BLUE+"Listando Articulos por precio ⬆️ "+GREEN+nickname<<BGr+"\n"<<endl;
                    reportes_menu();
                    cout<<GREEN+"Ingrese una opcion"+RESET<<endl;
                    cin >> op;
                
                }else{
                    cout<<RED+"\nIngrese un comando valido! 💢\n"<<endl;
                    reportes_menu();
                    cout<<GREEN+"Ingrese una opcion"+RESET<<endl;
                    cin >> op;
                }
            }
                menu();
                cout<<GREEN+"Ingrese una opcion"+RESET<<endl;
                cin >> op;
        }else{
            cout<<RED+"\nIngrese un comando valido! 💢\n"<<endl;
            menu();
            cout<<GREEN+"Ingrese una opcion"+RESET<<endl;
            cin >> op;
        }
    }
}

int main(){
    iniciarJuego();
    // cargaMasiva("archivos/ArchivoPrueba.json");
    // lista_listas.show("45");
    // cola.Enqueue("100","50");
    // cola.Enqueue("2","2");
    // cola.Enqueue("3","3");
    // cola.Enqueue("4","4");
    // cola.Enqueue("5","5");
    // cola.Enqueue("6","6");
    // cola.show();
    // lista_listas.crearGrafica();
    // cola.crearGrafica();
    // lista_listas.show();
    // tutorial_menu();
    return 1;
}