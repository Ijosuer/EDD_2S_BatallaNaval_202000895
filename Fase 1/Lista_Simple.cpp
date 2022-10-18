#include <iostream>
#include "Pila.cpp"
#include "string"
#include <fstream>

class Node
{
public:
    NodoPila* accesoPila;
    int len = 0;
    Node* next;
    Node (Stack* _p ) : next(NULL) {}
};

class LinkedList
{
public:
    int lenaux=0;
    int lenTotal = 0;
    string texto_grafica;
    Node *head ;
    Node* ultimo;
    Stack pila ;

    void addStart()                         
    {                 
    Stack* pila2 =NULL;
        pila2 = &pila;                 
       Node* tmp = new Node(pila2);
       tmp->len = lenaux;
        tmp->accesoPila = pila2->primero;
        tmp->next = head;
        head = tmp;
        lenaux = 0;
        lenTotal +=1;
    }

    void show()
    {
    std::cout<<"Estos son nodos de lista"<<std::endl;
        Node* tmp = head;
        while (tmp != NULL)
        {
            std::cout << tmp->accesoPila << std::endl;
            tmp = tmp->next;
        }
    }

    void addNodoPila(int _id, int _x, int _y){
        lenaux+=1;
        pila.push(_id ,_x,_y);
    //    std::cout<<pila.primero->x<<std::endl;
    }

    void report()
    {
    Node* aux = head;
    Node* tmp= head;
    Node* auxTmp= head;
    string text = "";
    string shots,shotsFinal = "";
    text+="rankdir=LR; \n ";
    text+="labelloc = \"t;\"label = \"Lista de Movimientos\";\n";

        while(true){

            while(true){
                if(tmp == NULL){
                    break;
                }
                for (int i = 0; i <tmp->len; i++)
                {
                   if (i+1 == tmp-> len){
                    shots += to_string(tmp->accesoPila->x)+","+to_string(tmp->accesoPila->y);
                    break;
                   }else{

                    if(tmp->accesoPila == NULL){
                        break;
                    }else{

                    shots += to_string(tmp->accesoPila->x)+","+to_string(tmp->accesoPila->y)+"|";
                    tmp->accesoPila = tmp->accesoPila->next;
                    }
                   }
                }
                if (aux->next->accesoPila->id == lenTotal){
                text += "x"+to_string(aux->next->accesoPila->id)+"[shape = \"record\", label=\""+shots+"\"]";
                    break;
                }else{
                text += "x"+to_string(aux->next->accesoPila->id)+"[shape = \"record\", label=\""+shots+"\"]";
                if(head->next == NULL){
                    break;
                }else{
                text+= "x"+to_string(aux->next->accesoPila->id)+"->x"+to_string(aux->next->accesoPila->next->id)+"\n";    

                }

                }
                

            aux->next->accesoPila = aux->next->accesoPila->next;     
                if( head->next == NULL){
                    break;
                }else{

                tmp->len = head->next->len;
                }
                if(head->accesoPila->next == NULL){
                tmp->accesoPila= head->accesoPila;

                }else{
                tmp->accesoPila= tmp->accesoPila->next;
                head = head->next;
                shots="";
                }
        }

            texto_grafica = text;
            break;
        }   

    }

   void crearGrafica(){
    report();
    string contenido = "digraph G {\n\n";
    string filename("archivos/Lista_Pilas.dot");
    fstream file_out;
    file_out.open(filename, std::ios_base::out);
    if (!file_out.is_open()) {
        cout << "failed to open " << filename << '\n';
    } else {
        contenido += texto_grafica;
        contenido +="\n}";
        file_out <<contenido<< endl;
        system("dot -Tpng archivos/Lista_Pilas.dot -o archivos/Lista_Pilas.png");
    }
}

};
// int main()
// {
    LinkedList *list1 = new LinkedList();
    //Primera Pila
                                // list1->addNodoPila(1,1,1);
                                // list1->addNodoPila(2,2,2);
                                // list1->addNodoPila(3,2,0);
                                // list1->addStart();
        // list1->addNodoPila(3,1,1);
        // list1->addNodoPila(6,1,1);
        // list1->addNodoPila(7,2,2);
        // list1->addNodoPila(8,3,3);
        // list1->addNodoPila(9,4,4);
        // list1->addStart();
        
    // //Segunda Pila
                                    // list1->addNodoPila(4,5,5);
                                    // list1->addNodoPila(5,6,6);
                                    // list1->addNodoPila(6,6,6);
                                    //     list1->addStart();
                                    // list1->addNodoPila(7,1,0);
                                    // list1->addNodoPila(8,6,6);
                                    // list1->addNodoPila(9,6,4);
                                    //     list1->addStart();
                                    // list1->addNodoPila(10,2,8);
                                    // list1->addNodoPila(11,3,3);
                                    // list1->addNodoPila(12,0,7);
                                    //     list1->addStart();
   
    // //Tercera Pila
    // list1->addNodoPila(6,7,7);
    // list1->addNodoPila(7,8,8);
    // list1->addNodoPila(8,9,9);
    // list1->addStart();
    
    // //Cuarta Pila
    // list1->addNodoPila(9,10,10);
    // list1->addNodoPila(10,11,11);
    // list1->addNodoPila(11,12,12);
    // list1->addStart();
  
    // //Quinra Pila
    // list1->addNodoPila(12,13,13);
    // list1->addStart();
    // list1->show();
    // std::cout<<"Este es el primero de mi lista"<<list1->head->accesoPila->id<<endl;
    // std::cout<<"Este es el primero->sig "<<list1->head->next->accesoPila->next->id<<endl;
    // list1->crearGrafica();
    // string x = list1->toReport();
    // std::cout<<x;

//     return 0;
// }