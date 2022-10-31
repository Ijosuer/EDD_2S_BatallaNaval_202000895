#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class hashi
{
private:
  /* data */
public:

  int n,m,min,max;
  // vector<int>lista;
  int iterar = 0;

  hashi(int _m , int _min , int _max ){
    m = _m;
    min = _min;
    max = _max;
    init();
  }
  int lista[5];
  void init(){
    n = 0;
    // lista[m];
    for (int i = 0; i < m; i++)
    {
      lista[i] =-1;
    }
    iterar = 0;
  }

  void insert(int k){
    int i = division(k);
    int r = 0;
    if(lista[i] == -1){
      lista[i] = k;
    }else{
      iterar +=1;
      r = linear(k);
      lista[r] = k;
    }
    // int i = division(k);
    // int r =0;
    // while (lista[i] != -1)
    // {
    //   iterar +=1;
    //   i =  linear(i);
    // }
    // lista[i] = k;
    n++;
    rehashing();
    // print();
  }

  void rehashing(){
    int len = (n*100)/m;
    if (len >= max)
    {
      // Array copy
      // int temp[sizeof(lista)/lista[0]];
      int temp[m];
      for (int i = 0; i < sizeof(lista)/sizeof(lista[0]); i++)
      {
        temp[i] = lista[i];
      }
      
      print();

      // Rehashing
      int mprev = m;
      m = n*100/min;
      init();
      cout<<sizeof(lista)/sizeof(lista[0])<<endl;
      for (int i = 0; i < mprev; i++)
      {
        if (temp[i] != -1)
        {
          insert(temp[i]);
        }
      }
      cout<<sizeof(lista)/sizeof(lista[0])<<endl;
    }else{
        print();
      }
  }

  void print(){
    cout<<"[";
    for (int i = 0; i < m; i++)
    {
      cout<<" "<<lista[i];
    }
      cout<<" ] "<<n*100/m<<"%"<<endl;
  }

  int division(int k){
    return k%m;
  }

  int linear(int k){
    return ((k%3)+1)*iterar;
    // return ((k+1)%m);
  }
};


// int main(){
//   hashi hash(5,20,80);
  // int lista[11];
  // cout<<sizeof(lista)/sizeof(lista[0])<<endl;
  // try
  // {
  // hash.insert(0);
  // hash.insert(1);
  // hash.insert(2);
  // hash.insert(3);
  // hash.insert(5);
  // hash.insert(4);
  // hash.insert(5);
  // hash.insert(6);
  // hash.insert(7);
  // hash.insert(8);
  // hash.insert(9);
  // hash.insert(10);
  // hash.insert(11);
  // hash.insert(12);
  // hash.insert(13);
  // hash.insert(26);
  // hash.insert(39);
  // hash.insert(52);
  // hash.insert(65);
  // hash.insert(23);
  // hash.insert(9);
  // hash.insert(8);
  // hash.insert(50);

  // hash.insert(5);
  // hash.insert(10);
  // hash.insert(15);
  // hash.insert(20);
  // hash.insert(25);
  // hash.insert(30);
//   }
//   catch(const std::exception& e)
//   {
//     std::cerr << e.what() << '\n';
//   }
//   return 1;
// }
