#include <iostream>
#include <string>
#include "../include/simple.hpp"



ListaSimple::ListaSimple()
{
    primero = ultimo = NULL;
}
bool ListaSimple::vacio()
{
    return (primero == NULL);
}

void ListaSimple::insertarAlFrente(Usuario elemento)
{
    Usuario *temp = new Usuario(elemento);
    if (vacio())
    {
        primero = ultimo = temp;
    }
    else
    {
        temp->sig = primero;
        primero = temp;
    }
}

void ListaSimple::insertarAlFinal(Usuario elemento)
{
    Usuario *temp = new Usuario(elemento);
    if (vacio())
    {
        primero = ultimo = temp;
    }
    else
    {
        ultimo = ultimo->sig = temp;
    }
}

void ListaSimple::eliminarAlFrente()
{
    if (vacio())
    {
        cout << "No se puede eliminar. Lista Vacia " << endl;
    }
    else
    {
        if (primero == ultimo)
        {
            primero = ultimo = NULL;
            cout << "Elemento eliminado." << endl;
        }
        else
        {
            Usuario *temp = primero;

            primero = primero->sig;
            delete temp;
            cout << "Elemento eliminado. " << endl;
        }
    }
}

void ListaSimple::eliminarAlFinal()
{
    if (vacio())
    {
        cout << "No se puede eliminar. Lista vacia" << endl;
    }
    else
    {
        if (primero == ultimo)
        {
            primero = ultimo = NULL;
            cout << "Elemento eliminado." << endl;
        }
        else
        {
            Usuario *aux = primero;

            while (aux != NULL)
            {
                if (aux->sig == ultimo)
                {
                    Usuario *temp = ultimo;
                    ultimo = aux;
                    aux->sig = NULL;

                    cout << "Elemento eliminado." << temp->nick << endl;
                    delete temp;
                }
                aux = aux->sig;
            }
        }
    }
}

void ListaSimple::mostrarLista()
{
    if (vacio() == true)
    {
        cout << "No hay elementos en la lista." << endl;
    }
    else
    {
        Usuario *aux = primero;
        int i = 1;
        cout << "Los datos en la lista son los siguientes" << endl;

        while (aux != NULL)
        {
            cout << "El elemento " << i << " de la lista es: " << aux->nick << endl;
            aux = aux->sig;
            i++;
        }
    }
}

vector<crow::json::wvalue> ListaSimple::to_vector()
{
    std::vector<crow::json::wvalue> datos;
    if (vacio() == true)
    {
        cout << "No hay elementos en la lista." << endl;
    }
    else
    {
        Usuario *aux = primero;

        while (aux != NULL)
        {   
            // std::cout<<aux->id<<aux->password<<std::endl;
            // int id_int = stoi(id);
            // int id += 1;
            int id = stoi(aux->id);
            int moneda = stoi(aux->monedas);
            int edad = stoi(aux->edad);
            
            crow::json::wvalue x;
            x["id"] = id;
            x["nick"] = aux->nick;
            x["monedas"] = moneda;
            x["edad"] = edad;
            datos.push_back(x);
            aux = aux->sig;
        }
    }
    return datos;
}
vector<crow::json::wvalue> ListaSimple::to_vectorArt()
{
    std::vector<crow::json::wvalue> datos;
    if (vacio() == true)
    {
        cout << "No hay elementos en la lista." << endl;
    }
    else
    {
        Usuario *aux = primero;

        while (aux != NULL)
        {   
            // std::cout<<aux->id<<aux->password<<std::endl;
            // int id_int = stoi(id);
            // int id += 1;
            int id = stoi(aux->id);
            int moneda = stoi(aux->monedas);
            
            crow::json::wvalue x;
            x["id"] = id;
            x["nombre"] = aux->nick;
            x["categoria"] = aux->password;
            x["precio"] = moneda;
            x["src"] = aux->edad;
            datos.push_back(x);
            aux = aux->sig;
        }
    }
    return datos;
}

Usuario *ListaSimple::buscar(string nick)
{
    if (!vacio())
    {
        Usuario *aux = primero;
        while (aux != NULL)
        {
            if (aux->nick == nick)
            {
                Usuario *us = new Usuario(aux->id,aux->nick, aux->password, aux->monedas, aux->edad);
                return us;
            }
            aux = aux->sig;
        }
    }
    return nullptr;
}
Usuario *ListaSimple::editar(string nick)
{
    if (!vacio())
    {
        Usuario *aux = primero;
        while (aux != NULL)
        {
            if (aux->nick == nick)
            {
                aux->nick = "YO CAMBIO XD";
                Usuario *us = new Usuario(aux->id,aux->nick, aux->password, aux->monedas, aux->edad);
                us->nick = "Cambiaaaaaaaaaaaaaar";
                us->edad = "12";
                return us;
            }
            aux = aux->sig;
        }
    }
    return NULL;
}

Usuario *ListaSimple::buscarArt(string _id)
{
    if (!vacio())
    {
        Usuario *aux = primero;
        while (aux != NULL)
        {
            if (aux->id == _id)
            {
                Usuario *us = new Usuario(aux->id,aux->nick, aux->password, aux->monedas, aux->edad);
                return us;
            }
            aux = aux->sig;
        }
    }
    return nullptr;
}

void ListaSimple::ordenarBurbujaDes()
{
    Usuario* actual;
    Usuario*  siguiente; 
    string t;
     
    actual = primero;
     while(actual->sig != NULL)
     {
          siguiente = actual->sig;
          
          while(siguiente!=NULL)
          {
               if(actual->edad < siguiente->edad)
               {
                    t = siguiente->edad;
                    cout<<t<<endl;
                    siguiente->edad = actual->edad;
                    actual->edad = t;          
               }
               siguiente = siguiente->sig;                    
          }    
          actual = actual->sig;
          siguiente = actual->sig;
     }
    mostrarLista();
}
void ListaSimple::ordenarBurbujaAs()
{
    mostrarLista();
    Usuario* actual;
    Usuario*  siguiente; 
    string t;
     
    actual = primero;
     while(actual->sig != NULL)
     {
          siguiente = actual->sig;
          
          while(siguiente!=NULL)
          {
               if(stoi(actual->edad) < stoi(siguiente->edad))
               {
                    t = siguiente->edad;
                    siguiente->edad =actual->edad;
                    actual->edad = t;          
               }
               siguiente = siguiente->sig;                    
          }    
          actual = actual->sig;
          siguiente = actual->sig;
           
     }
    mostrarLista();

}


// int main(){
//     ListaSimple ls;
//     ls.insertarAlFrente(Usuario("1","josue","","","12"));
//     ls.insertarAlFrente(Usuario("2","mike","","","12"));
//     ls.insertarAlFrente(Usuario("3","dan","","","12"));
//     ls.insertarAlFrente(Usuario("4","luca","","","12"));
//     ls.insertarAlFrente(Usuario("5","sha","","","12"));
//     ls.mostrarLista();
//     ls.editar("dan");
//     ls.mostrarLista();

//     return 0;
// }