#include <iostream>
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

int main(){
    crearSimple();
    // menu();
}