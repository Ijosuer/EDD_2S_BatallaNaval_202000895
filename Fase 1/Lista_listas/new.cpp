#include <iostream>
#include "Lista_listas.cpp"

using namespace std;
Lista_listas listaS;

int main(){
    listaS.insertarCategoria("Raro");
    listaS.insertarCategoria("Epico");
    listaS.insertarCategoria("Legendario");
    listaS.insertarArticulo("Raro","1","raro1","600","");
    listaS.insertarArticulo("Raro","2","raro2","700","");
    listaS.insertarArticulo("Epico","3","epicgames1","800","");
    listaS.insertarArticulo("Epico","4","epicgames2","900","");
    listaS.insertarArticulo("Legendario","5","leyenda","1000","");
    // listaS.showCategorias();
    // listaS.showArticulos("Legendario");
    // listaS.show();
    listaS.crearGrafica();
    return 1;
}