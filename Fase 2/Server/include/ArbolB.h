#include <vector>
#include <map>
#include "/home/ijosuer/Escritorio/EDD_2S_BatallaNaval_202000895/Fase 2/Server/include/NodoB.h"
#include <iostream>
#include "../lib/crow_all.h"

class ArbolB
{
    public:
        int orden_arbol = 4;
        NodoB* raiz;
        ArbolB();
        void insertar(int id, string nick, string password, string monedas, string edad);
        pair<NodoB*, pair<bool, bool>> insertarCrearRama(NodoB* nodo, NodoB* rama);
        NodoB* dividir(NodoB* rama);
        pair<NodoB*, bool>  insertarEnRama(NodoB* primero, NodoB* nuevo);
        bool esHoja(NodoB* primero);
        int contador(NodoB* primero);
        void Grafo();
        string GrafoArbolAbb(NodoB*rama);
        string GrafoRamas(NodoB*rama);
        string GrafoConexionRamas(NodoB*rama);
        string editar(string nick, string password, string nicknew, string passwordnew, string edadnew);
        string editar2(NodoB*rama, string nick, string password, string nicknew, string passwordnew, string edadnew);
        string editar3(NodoB*rama, string nick, string password, string nicknew, string passwordnew, string edadnew);
        string buscar(string nick, string password);
        string buscarRamas(NodoB*rama, string nick, string password);
        string buscarConexionesRamas(NodoB*rama, string nick, string password);
        vector<crow::json::wvalue> to_vector();
    private:
};
