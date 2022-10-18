#include <iostream>
#include <string>
#include <vector>
#include <map>


#include "../lib/crow_all.h"
using namespace std;


class NodeUser
{
public:
    string data;
    int edad;
    NodeUser* next;
    NodeUser (string data_, int _edad) : data(data_),edad(_edad), next(NULL) {}
};

class ListaS
{
public:
    NodeUser* head ;
    void ingresarUsuario(string data, int _edad)
    {
        NodeUser* tmp = new NodeUser(data,_edad);
        tmp->next = head;
        head = tmp;
    }

    void show()
    {
        NodeUser* tmp = head;
            std::cout<<"\u001b[40;1m\u001b[37m*\u001b[32m*******************************\u001b[37m*"<<std::endl;
        while (tmp != 0)
        {
            std::cout<<"\u001b[37m|\u001b[35mNombre: \u001b[37m" << tmp->data<<"\u001b[33m-->\u001b[36m"<<tmp->edad<< std::endl;
            tmp = tmp->next;
        }
             std::cout<<"\u001b[37m|\u001b[34m-------------------------------\u001b[37m" <<std::endl;
    }

    void ordenarBurbuja()
{
    NodeUser* actual;
    NodeUser*  siguiente; 
    int t;
     
    actual = head;
     while(actual->next != NULL)
     {
          siguiente = actual->next;
          
          while(siguiente!=NULL)
          {
               if(actual->edad < siguiente->edad)
               {
                    t = siguiente->edad;
                    siguiente->edad = actual->edad;
                    actual->edad = t;          
               }
               siguiente = siguiente->next;                    
          }    
          actual = actual->next;
          siguiente = actual->next;
           
     }
     
    //  cout<<"\n\n\tLista ordenada..."<<endl;

}
    void ordenarBurbujaAs()
{
    NodeUser* actual;
    NodeUser*  siguiente; 
    int t;
     
    actual = head;
     while(actual->next != NULL)
     {
          siguiente = actual->next;
          
          while(siguiente!=NULL)
          {
               if(actual->edad > siguiente->edad)
               {
                    t = siguiente->edad;
                    siguiente->edad = actual->edad;
                    actual->edad = t;          
               }
               siguiente = siguiente->next;                    
          }    
          actual = actual->next;
          siguiente = actual->next;
           
     }
     
    //  cout<<"\n\n\tLista ordenada..."<<endl;

}

vector<crow::json::wvalue> to_vector()
{
    std::vector<crow::json::wvalue> datos;
    if (head == NULL)
    {
        cout << "No hay elementos en la lista." << endl;
    }
    else
    {
        NodeUser *aux = head;

        while (aux != NULL)
        {   
            crow::json::wvalue x;
            x["nick"] = aux->data;
            x["edad"] = aux->edad;
            datos.push_back(x);
            aux = aux->next;
        }
    }
    return datos;
}

};




