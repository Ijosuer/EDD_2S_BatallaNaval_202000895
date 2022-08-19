#include <iostream>
#include <fstream>
#include <jsoncpp/json/json.h>
#include <jsoncpp/json/value.h>
// #include <SHA256.h>

#include "Lista_Circular_Doble.cpp"
#include "Cola.cpp"
#include "Stack.cpp"
using namespace std;

//      --- COLORES ---
string RED = "\u001b[31m",GREEN ="\u001b[32m",YELLOW = "\u001b[33m",BLUE = "\u001b[34m";
string MAGENTA = "\u001b[35m",CYAN = "\u001b[36m",WHITE = "\u001b[37m",RESET = "\u001b[0m";
string BGblack = "\u001b[40;1m", BGr = "\u001b[0m";
//      --- ---- ---

Lista_Circular_Doble lista;
Cola cola;
Stack pila;
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

int main(){
    menu();
    string op;
    string nickname, edad,pwd ="";
    bool flag = false;
    cout<<"Ingrese una opcion"<<endl;
    cin >> op;
    while(op != "5" ){
        if(op == "1"){//Carga Masiva
            cargaMasiva("archivos/archivo.json");
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

            //Llamar al metodo buscar en mis usuarios
            bool ans = lista.whereis(nickname,pwd);
            if (ans == true){
                flag = true;
                edad = lista.dataEdad(nickname);
                cout<<RESET<<endl;
                cout<<BGblack<<BLUE+"✅ Bienvenido al sistema "+GREEN+nickname<<BGr+"\n"<<endl;
                menu();
                cout<<GREEN+"Ingrese una opcion"+RESET<<endl;
                cin >> op;
            }else{
                cout<<RED+"\nCREDENCIALES INCORRECTAS! 💢\n"<<endl;
                menu();
                cout<<GREEN+"Ingrese una opcion"+RESET<<endl;
                cin >> op;
            }
            
        }else if(op == "3"){ //Login
            if(flag == true){
                login();
                cout<<GREEN+"Ingrese una opcion"+RESET<<endl;
                cin >> op;
                while(op != "6"){
                    if(op == "1"){
                        string newNickname,newPwd,newEdad = "";
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
                        cout<<BGblack<<"* "<<BLUE<<" Nickname: "<<WHITE<<nickname<<BGr<<endl;
                        cout<<BGblack<<"* "<<BLUE<<" Edad: "<<WHITE<<edad<<BGr<<endl;
                        cout<<BGblack<<"* "<<BLUE<<" Password: "<<WHITE<<pwd<<BGr<<endl;
                        cout<<BGblack<<YELLOW<<"*************************"<<RESET<<BGr<<endl;
                        bool ans =lista.editar(nickname,pwd,edad);
                        if (ans == true){
                            cout<<BGblack<<BLUE+"✅ Cambio exitoso "+GREEN+nickname<<BGr+"\n"<<endl;
                            menu();
                            cout<<GREEN+"Ingrese una opcion"+RESET<<endl;
                            cin >> op;
                        }else{
                            cout<<RED+"ERROR al cambiar los datos! 💢\n"<<endl;
                            login();
                            cout<<GREEN+"Ingrese una opcion"+RESET<<endl;
                            cin >> op;
                        }

                    }else if(op == "2"){
                        cout<<"Desplegar menu eliminar"<<endl;
                    }else if(op == "3"){
                        cout<<"Desplegar ver tutorial"<<endl;
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
                cout<<RED+"\n🔒Por favor inicia sesion❗\n"<<endl;
                menu();
                cout<<GREEN+"Ingrese una opcion"+RESET<<endl;
                cin >> op;
            }
        }else{
            cout<<RED+"\nIngrese un comando valido! 💢\n"<<endl;
            menu();
            cout<<GREEN+"Ingrese una opcion"+RESET<<endl;
            cin >> op;
        }
    }

    return 1;
}