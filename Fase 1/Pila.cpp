#include <iostream>
#include <string>	
#include "Nodo_Pila.h"
using namespace std;


class Stack{
    public:
    NodoPila* primero = NULL;
    int len = 0;

   void push(int _id, int x, int y){
    NodoPila* tmp = new NodoPila(_id ,x,y);
    tmp->next = primero;
    primero = tmp;
    len+=1;
    }                                                               

    NodoPila* pop(){
    NodoPila* tmp = NULL;
    if(primero != NULL ){
        tmp = new NodoPila(primero->id,primero->x,primero->y);
        primero = primero->next;
    }
    return tmp;
    }
};

// int main(){
//     Stack* pila = new Stack();
//     pila->push(1,1,3);
//     pila->push(2,2,2);
//     pila->push(3,3,3);
    
//     cout<<pila->pop()->x<<endl;
// }

