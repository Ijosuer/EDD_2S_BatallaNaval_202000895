#include "Lista_Circular_Doble.h"
#include <iostream>
#include <fstream>
#include "sha256.h"
// using namespace std;
// SHA256 contra;
//Programar los metodos

void Lista_Circular_Doble::insertarInicio(string _name,string _pwd,int _coins,int _edad){
    Usuario* tmp = new Usuario(_name,_pwd,_coins,_edad);
    //Si la lista esta vacia
    if(primero == NULL){
        primero = tmp;
        ultimo = primero;
        len +=1;
    }else{
        Usuario * aux = ultimo;
        ultimo = aux->siguiente = tmp;
        ultimo->anterior = aux;
        len += 1;
    }
    unirNodos();
}

bool Lista_Circular_Doble::registrar(string _name,string _pwd,int _coins,int _edad){
    Usuario* tmp = new Usuario(_name,_pwd,_coins,_edad);
    //Si la lista esta vacia
    bool flag;
    if(primero == NULL){
        primero = tmp;
        ultimo = primero;
        len +=1;
    }else{
        flag = isNick(_name);
        if(flag == true){
            return false;
        }else{
            Usuario * aux = ultimo;
            ultimo = aux->siguiente = tmp;
            ultimo->anterior = aux;
            len += 1;
            unirNodos();
            return true;
        }
    }
}

bool Lista_Circular_Doble::isNick(string _name){
 Usuario* tmp = primero;
    for (int i = 0; i < len; i++){
        if(tmp->name == _name){
            return true;
        }else{
            tmp = tmp->siguiente;
        }
    }
    return false;
}

void Lista_Circular_Doble::eliminarUltimo(){
    if(primero == NULL){
        cout<<"\nERROR LISTA VACIA 💢\n"<<endl;
    }else if(primero == ultimo){
        primero = ultimo = NULL;
    }else{
        ultimo = ultimo->anterior;
    }
    unirNodos();
}

void Lista_Circular_Doble::unirNodos(){
    if (primero != NULL){
        primero->anterior = ultimo;
        ultimo->siguiente = primero;
    }
}

void Lista_Circular_Doble::report(){
    Usuario* aux = primero;
    string text = "";
    // char pass[] ="";
    string strPass = "";
    string newPass = "";
    text+="rankdir=LR; \n node[shape=egg,style=filled,color=khaki,fontname=\"Century Gothic\"]; graph [bgcolor = \"tan\", fontname = \"Century Gothic\"];\n";
    text+="labelloc = \"t;\"label = \"Usuarios\";\n";

    try
    {
        while(aux != NULL){
            string strrr = aux->pwd;
            
                // string str = ({aux->pwd});
            char arr[strrr.length() + 1]; 

            strcpy(arr, strrr.c_str()); 
            for (int i = 0; i < strrr.length(); i++) 
            newPass =SHA256(arr);



        text+="x"+to_string(aux->coins)+"[dir=both label = \"Monedas = "+to_string(aux->coins)+"\\nNombre = "+(aux->name)+"\\nEdad = "+to_string(aux->edad)+"\\n Pwd = "+(newPass)+ "\"]";
            // cout<<text<<endl;
            text+="x"+to_string(aux->coins)+"-> x"+to_string(aux->siguiente->coins)+"\n";
            // cout<<text<<endl;
            text+="x"+to_string(aux->coins)+"-> x"+to_string(aux->anterior->coins)+"\n";
            // cout<<text<<endl;
            aux=aux->siguiente;
        if (aux!=primero){
           string strrr = aux->pwd;
            
                // string str = ({aux->pwd});
            char arr[strrr.length() + 1]; 

            strcpy(arr, strrr.c_str()); 
            for (int i = 0; i < strrr.length(); i++) 
            newPass =SHA256(arr);
                text+="x"+to_string(aux->coins)+"[dir=both label = \"Monedas = "+to_string(aux->coins)+"\\nNombre = "+(aux->name)+"\\nEdad = "+to_string(aux->edad)+"\\n Pwd = "+(newPass)+ "\"]";
                // cout<<text<<endl;
        }    
        if (aux==ultimo){
            text+="x"+to_string(aux->coins)+"-> x"+to_string(aux->siguiente->coins)+"\n";
            text+="x"+to_string(aux->coins)+"-> x"+to_string(aux->anterior->coins)+"\n";
            // cout<<text<<endl;
            texto_grafica = text;
            break;
        }
    }
    }
    catch(const std::exception& e)
    {
        cerr << e.what() << '\n';
    }
}

void Lista_Circular_Doble::crearGrafica(){
    report();
    string contenido = "digraph G {\n\n";
    string filename("archivos/Usuarios.dot");
    fstream file_out;
    file_out.open(filename, std::ios_base::out);
    if (!file_out.is_open()) {
        cout << "failed to open " << filename << '\n';
    } else {
        contenido += texto_grafica;
        contenido +="}\n";
        file_out <<contenido<< endl;
        try
        {
        system("dot -Tpng archivos/Usuarios.dot -o archivos/Usuarios.png");
        system("exit");
        }
        catch(const std::exception& e)
        {
            std::cerr << e.what() << '\n';
        }
        cout << "Done Writing!" << endl;

    }
        return;
}

void Lista_Circular_Doble::verLista(){
    Usuario* tmp = primero;
    cout<<"Esta es la lista de usuarios"<<endl;
    // while(tmp != NULL){
    //     cout<<tmp->name<<endl;
    //     if(tmp = primero){
    //         break;
    //     }
    for (int i = 0; i <len; i++)
    {
        cout<<tmp->name<<tmp->edad<<endl;
        tmp = tmp->siguiente;
    }
    
    
}

void Lista_Circular_Doble::isPrimero(){
    cout<<"Este es el primer NODO: "<<primero->name<<endl;
    cout<<"Este es el primer NODO.ant: "<<primero->anterior->name<<endl;
}

void Lista_Circular_Doble::isUltimo(){
    cout<<"Este es el ultimo NODO: "<<ultimo->name<<endl;
    cout<<"Este es el ultimo NODO.sig: "<<ultimo->siguiente->name<<endl;
}

bool Lista_Circular_Doble::whereis(string _name, string _pwd){
    Usuario* tmp = primero;
    for (int i = 0; i < len; i++){
        if(tmp->name == _name && tmp->pwd == _pwd){
            return true;
        }else{
            tmp = tmp->siguiente;
        }
    }
    return false;
}

bool Lista_Circular_Doble::editar(string _anterior,string _name,string _pwd,int _edad){
    Usuario* tmp = primero;
    for (int i = 0; i < len; i++){
        if(tmp->name == _anterior){
            tmp->name = _name;
            tmp->pwd = _pwd;
            tmp->edad= _edad;
            return true;
        }else{
            tmp = tmp->siguiente;
        }
    }
    return false;
}

int Lista_Circular_Doble::dataEdad(string _name){
    Usuario* tmp = primero;
    for (int i = 0; i < len; i++){
        if(tmp->name == _name){
            return tmp->edad;
        }else{
            tmp = tmp->siguiente;
        }
    }
    return 0;
}

int Lista_Circular_Doble::cuantasFichas(string _name){
    Usuario* tmp = primero;
    for (int i = 0; i < len; i++){
        if(tmp->name == _name){
            return tmp->coins;
        }else{
            tmp = tmp->siguiente;
        }
    }
    return 0;
}

void Lista_Circular_Doble::eliminarPrimero(){
    if(len == 0){
        cout<<"\nERROR LISTA VACIA 💢\n"<<endl;
    }else if(primero == ultimo){
        primero = ultimo = NULL;
    }else{
        primero = primero->siguiente;
    }
    unirNodos();
}

void Lista_Circular_Doble::eliminarUsuario(string _name,string _pwd){
    Usuario* tmp = primero;
    for (int i = 0; i < len; i++){
        if(tmp->name == _name &&tmp->name == _pwd ){
            // return true;
            if(tmp == primero){
                eliminarPrimero();
                cout<<BGblack<<BLUE+"✅ Usuario "+GREEN+_name+" Eliminado con exito"<<BGr+"\n"<<endl;
                break;
            }else if(tmp == ultimo){
                eliminarUltimo();
                cout<<BGblack<<BLUE+"✅ Usuario "+GREEN+_name+" Eliminado con exito"<<BGr+"\n"<<endl;
                break;
            }else{
                tmp->anterior->siguiente = tmp->siguiente;
                tmp->siguiente->anterior = tmp->anterior;
                cout<<BGblack<<BLUE+"✅ Usuario "+GREEN+_name+" Eliminado con exito"<<BGr+"\n"<<endl;
                break;
            }
        }else{
            tmp = tmp->siguiente;
            if(tmp == primero){
                cout<<RED+"\nNO se puede eliminar este usuario! 💢\n"<<endl;
                break;
            }
        }
    }
    // return false;
}


// int main(){
// Lista_Circular_Doble lista;
// lista.insertarInicio("josue","jos",0,9);
// lista.insertarInicio("josue","jos",0,3);
// lista.insertarInicio("josue","jos",0,4);
// lista.insertarInicio("josue","jos",0,10);
// lista.insertarInicio("josue","jos",0,12);
// lista.insertarInicio("josue","jos",0,8);
// cout<<"PRIMERO"+lista.primero->edad<<endl;
// lista.verLista();
// lista.ordenarEdad(&lista.primero);
// lista.verLista();

//     return 1;
// }