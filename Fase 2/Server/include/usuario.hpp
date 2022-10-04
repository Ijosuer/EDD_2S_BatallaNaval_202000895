#include <iostream>
using namespace std;
class Usuario
{
public:
    string id;
    string nick;
    string password;
    string monedas;
    string edad;
    Usuario* sig;
    Usuario(string _id, string _nick, string _password, string _monedas, string _edad){
        id = _id;
        nick = _nick;
        password = _password;
        monedas = _monedas;
        edad = _edad;
        sig = NULL;
    }
};