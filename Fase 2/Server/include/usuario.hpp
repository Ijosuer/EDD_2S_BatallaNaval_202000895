#include <iostream>
#include <map>
using namespace std;
class Usuario
{
public:
    string id;
    string nick;
    string password;
    string monedas;
    string edad;
    Usuario() {}
    Usuario(string id, string nick, string password, string monedas, string edad) : id(id),nick(nick), password(password), monedas(monedas), edad(edad) {}
    map<string, string> to_map()
    {
        return {{"ID:", id},{"nick", nick}, {"monedas", monedas}, {"edad", edad}};
    }
};