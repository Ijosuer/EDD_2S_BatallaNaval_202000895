#include <iostream>
#include <map>
#include <vector>
#include "usuario.hpp"
#include "../lib/crow_all.h"
using namespace std;

class ListaSimple
{
private:

public:
    int tamanio;
    Usuario *primero;
    Usuario *ultimo;
    ListaSimple();
    bool vacio();
    void insertarAlFrente(Usuario elemento);
    void insertarAlFinal(Usuario elemento);
    void eliminarAlFrente();
    void eliminarAlFinal();
    void mostrarLista();
    void ordenarBurbujaDes();
    void ordenarBurbujaAs();
    vector<crow::json::wvalue> to_vector();
    vector<crow::json::wvalue> to_vectorArt();
    Usuario *buscar(string);
    Usuario *editar(string);
    Usuario *buscarArt(string);
};
