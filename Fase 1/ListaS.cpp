// #include <iostream>
// #include <string>
// using namespace std;

// class NodeUser
// {
// public:
//     string data;
//     string edad;
//     NodeUser* next;
//     NodeUser (string data_, string _edad) : data(data_),edad(_edad), next(NULL) {}
// };

// class ListaS
// {
// public:
//     NodeUser* head ;
//     void ingresarUsuario(string data, string _edad)
//     {
//         NodeUser* tmp = new NodeUser(data,_edad);
//         tmp->next = head;
//         head = tmp;
//     }

//     void show()
//     {
//         NodeUser* tmp = head;
//             std::cout<<"\u001b[40;1m\u001b[37m*\u001b[32m*******************************\u001b[37m*"<<std::endl;
//         while (tmp != 0)
//         {
//             std::cout<<"\u001b[37m|\u001b[35mNombre: \u001b[37m" << tmp->data<<"\u001b[33m-->\u001b[36m"<<tmp->edad<< std::endl;
//             tmp = tmp->next;
//         }
//              std::cout<<"\u001b[37m|\u001b[34m-------------------------------\u001b[37m" <<std::endl;
//     }

//     void ordenarBurbuja()
// {
//     NodeUser* actual;
//     NodeUser*  siguiente; 
//     string t;
     
//     actual = head;
//      while(actual->next != NULL)
//      {
//           siguiente = actual->next;
          
//           while(siguiente!=NULL)
//           {
//                if(stoi(actual->edad) < stoi(siguiente->edad))
//                {
//                     t = siguiente->edad;
//                     siguiente->edad =actual->edad;
//                     actual->edad = t;          
//                }
//                siguiente = siguiente->next;                    
//           }    
//           actual = actual->next;
//           siguiente = actual->next;
           
//      }
     

// }
// };

// int main()
// {
//     ListaS *list1 = new ListaS();
//     list1->ingresarUsuario("zack","100");
//     list1->ingresarUsuario("JOSUE","12");
//     list1->ingresarUsuario("mike","31");
//     list1->ingresarUsuario("sdany","4");
//     list1->show();
//     cout<<list1->head->edad<<endl;
//     list1->ordenarBurbuja();
//     cout<<list1->head->edad<<endl;
//     list1->show();
//     return 0;
// }





