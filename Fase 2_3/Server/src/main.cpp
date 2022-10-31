#include <iostream>
#include <fstream>
#include <map>
#include "./listaS.cpp"
// #include "./AVL.hpp"
// #include "./Cola.hpp"

// #include "/home/ijosuer/Escritorio/EDD_2S_BatallaNaval_202000895/Fase 2_3/Server/include/ArbolB.h"
#include "/home/ijosuer/Escritorio/EDD_2S_BatallaNaval_202000895/Fase 2_3/Server/include/simple.hpp"

#include "/home/ijosuer/Escritorio/EDD_2S_BatallaNaval_202000895/Fase 2_3/Server/lib/crow_all.h"
#include "/home/ijosuer/Escritorio/EDD_2S_BatallaNaval_202000895/Fase 2_3/Server/lib/json.hpp"
#include "/home/ijosuer/Escritorio/EDD_2S_BatallaNaval_202000895/Fase 1/jsoncpp.cpp"

using namespace std;
using json = nlohmann::json;

ListaSimple lista;
ListaS list_ordenar;
ListaSimple listaArtic;
// ArbolB arbolB;
// Cola cola;

void cargaMasiva(string _ruta){
    // Let's parse it
    Json::Value root;
    Json::Reader reader;
    ifstream file(_ruta);
    bool parsedSuccess = reader.parse(file,root,false);

    if (not parsedSuccess) {
        // Report failures and their locations
        // in the document.
        std::cout << "Failed to parse JSON" << endl;
    }
    Json::Value::Members mem = root.getMemberNames();
    int contador = 0;
    for (int j = 0; j < root.size(); j++){
    Json::Value child = root[mem[j]];
        for(auto& element : child){
            if (mem[j]=="articulos"){
                string id, categoria,precio,nombre,src = "";
                for (int i = 0; i < element.size(); i++){
                Json::Value::Members mem2 = element.getMemberNames();
                Json::Value child2 = element[mem2[i]];
                // cout << "name: " << mem2[i] << ", child: " << child2 << endl;
                // cout  << mem2[i] <<endl;
                    if(mem2[i] == "id"){
                        id = child2.asString();
                    }else if (mem2[i] == "categoria"){
                        categoria = child2.asString();
                        // lista_listas.insertarCategoria(categoria);
                    }else if (mem2[i] == "precio"){
                        precio = child2.asString();
                    }else if (mem2[i] == "nombre"){
                        nombre= child2.asString();
                    }else if (mem2[i] == "src"){
                        src = child2.asString();
                        // contador+=1;
                        // std::cout<<contador<<endl;
                        src = child2.asString();
                        int id_ok = stoi(id);
                        int precio_ok = stoi(precio);
                        listaArtic.insertarAlFrente(Usuario(id,nombre,categoria,precio,src));
                        // avl.insertar(Compra(id_ok,nombre,precio_ok));

                    };
                }   
            }else if(mem[j] == "usuarios"){
                string edad,monedas,nick,password;
                string id;

                for (int i = 0; i < element.size(); i++){
                Json::Value::Members mem2 = element.getMemberNames();
                Json::Value child2 = element[mem2[i]];
                    if(mem2[i] == "edad"){
                    edad = child2.asString();
                    }else if (mem2[i] == "id"){
                    id = child2.asString();
                    }else if (mem2[i] == "monedas"){
                    monedas = child2.asString();
                    }else if (mem2[i] == "nick"){
                    nick = child2.asString();
                    }else if (mem2[i] == "password"){
                    password = child2.asString();

                        //Creando primer usuario
                        int edad_ok = std::stoi(edad);
                        int monedas_ok =  std::stoi(monedas);
                        int idOk = std::stoi(id);
                        list_ordenar.ingresarUsuario(nick,edad_ok);
                        // arbolB.insertar(idOk,nick,password,monedas,edad);
                        lista.insertarAlFrente(Usuario(id,nick,password,monedas,edad));
                        // lista_aux->insertarInicio(nick,password,monedas_ok,edad_ok);
                        // listaUsuariosaux.ingresarUsuario(nick,edad_ok);
                        // ls.insertarAlFrente()
                        
                    };
                }
            }else if(mem[j] == "tutorial"){
                string ancho,alto,x,y = "";
                int iterator=1;
                    Json::Value::Members mem2 = child.getMemberNames();
                for (int i = 0; i < child.size(); i++){
                    Json::Value child2 = child[mem2[i]];
                        if(mem2[i] == "ancho"){
                            ancho = child2.asString(); //ancho
                        }else if(mem2[i] == "alto"){
                            alto = child2.asString(); //alto
                        }else if(mem2[i] == "movimientos"){
                            // cola.Enqueue(iterator,ancho,alto);
                            iterator++;
                            for(auto& element : child2){
                                for (int i = 0; i < element.size(); i++){
                                    Json::Value::Members mem2 = element.getMemberNames();
                                    Json::Value child3 = element[mem2[i]];
                                    if(mem2[i] == "x"){
                                    x = child3.asString(); //coordenada X
                                    // std::cout<<x<<endl;
                                    }else if(mem2[i] == "y"){
                                    y = child3.asString(); //coordenada Y
                                    // std::cout<<y<<endl;
                                    // cola.Enqueue(iterator,x,y);
                                    iterator++;
                                    }
                                }
                            }
                        }
                }
                break;
            }
        }
    }
}

void to_json(json &JSON, const Usuario &us)
{
	JSON = {{"id", us.id},{"nickname", us.nick}, {"password", us.password}, {"monedas", us.monedas}, {"edad", us.edad}};
}

void from_json(const json &JSON, Usuario &us)
{
	int id = JSON.at("id").get<int>();
	us.id = to_string(id);
	us.nick = JSON.at("nick").get<string>();
	us.password = JSON.at("password").get<string>();
	int monedas = JSON.at("monedas").get<int>();
	us.monedas = to_string(monedas);
	int edad = JSON.at("edad").get<int>();
  us.edad = to_string(edad);
}


int main()
{
	cargaMasiva("/home/ijosuer/Escritorio/EDD_2S_BatallaNaval_202000895/Fase 2_3/Server/Entradafinal.json");
	// ---------------------------
	ListaSimple *lsArt = NULL;
	ListaSimple *listar = NULL;
    lsArt = &listaArtic;
    listar = &lista;
    // -----------------------
	ListaS *ls = NULL;
	ls = &list_ordenar;
	// -----------------------
    // ArbolB *arbolito = NULL;
	// arbolito = &arbolB;
    // // ------------------------
    // AVL avl;
    // Cola *colita = NULL;
    // colita = &cola;
	
	crow::SimpleApp app;
	CROW_ROUTE(app, "/")
	([]
	 {
        crow::json::wvalue x({{"status", "OK!"}});
        return x; });

	CROW_ROUTE(app, "/usuarios")
	([listar]()
	 { 
		std::vector<crow::json::wvalue> temp = listar->to_vector();
		crow::json::wvalue final = std::move(temp);
		return crow::response(std::move(final)); });

	CROW_ROUTE(app, "/articulos")
	([&lsArt]()
	 { 
		std::vector<crow::json::wvalue> temp = lsArt->to_vectorArt();
		crow::json::wvalue final = std::move(temp);
		return crow::response(std::move(final)); });

// TUTORIAL

	// CROW_ROUTE(app, "/tutorial")
	// ([colita]()
	//  { 
	// 	std::vector<crow::json::wvalue> temp = colita->to_vector();
	// 	crow::json::wvalue final = std::move(temp);
	// 	return crow::response(std::move(final)); });

// METODO LOGIN // 

	CROW_ROUTE(app, "/login")
	([listar](const crow::request &req)
	 {
        auto x = crow::json::load(req.body);
        if (!x)
            return crow::response(400);
		string nick=x["nick"].s();
		string pass=x["password"].s();

		Usuario *usuario=listar->buscar(nick);
		
		if(usuario==nullptr){
			crow::json::wvalue cuerpo({{"error", "usuario no encontrado"}});
			crow::response send(std::move(cuerpo));
			send.code=404;
			return send;
		}

		if(usuario->password==pass){
			// cout<<"---------"<<endl;
			// cout<<"nick: "<<usuario->nick<<endl;
			// cout<<"nick: "<<usuario->password<<endl;
			// crow::json::wvalue cuerpo(&usuario);
			crow::json::wvalue cuerpo({{"nick",usuario->nick},{"monedas",usuario->monedas},{"id",usuario->id},{"pwd",usuario->password}});
			crow::response send(std::move(cuerpo));
			send.code =200;
        	return send;
		}

        crow::json::wvalue response({{"error", "Contraseña incorrecta"}});
        crow::response variable(std::move(response)); 
		variable.code = 404;
		return variable;
		});
		
// METODOS DE ORDENAMIENTO //

	CROW_ROUTE(app, "/ordenarDes")
	([&ls]()
	 { 
		ls->ordenarBurbuja();
		std::vector<crow::json::wvalue> temp = ls->to_vector();
		crow::json::wvalue final = std::move(temp);
		return crow::response(std::move(final)); });
	CROW_ROUTE(app, "/ordenarAs")
	([&ls]()
	 { 
		ls->ordenarBurbujaAs();
		std::vector<crow::json::wvalue> temp = ls->to_vector();
		crow::json::wvalue final = std::move(temp);
		return crow::response(std::move(final)); });

// METODO GRAFICA AVL
	// CROW_ROUTE(app, "/graficaAVL")
	// ([&avl]()
	//  { 
	// 	avl.graficar();
	// 	return crow::response(200); });

// METODO REGISTRAR USUARIO
	// CROW_ROUTE(app, "/guardar_usuario")
	// 		.methods("POST"_method)([listar,arbolito](const crow::request &req)
	// 							{
	// 	auto x = crow::json::load(req.body);
	// 		if (!x)
	// 			return crow::response(400);
	// 		// string id=x["id"].s();
	// 		// int idOk = stoi(id);
	// 		string nick=x["nick"].s();
	// 		string pass=x["password"].s();
	// 		string monedas=x["monedas"].s();
	// 		// int moneda = stoi(monedas);
	// 		string edad=x["edad"].s();
	// 		int eda = stoi(edad);
    //         arbolito->insertar(eda+12,nick,pass,monedas,edad);
	// 		listar->insertarAlFrente(Usuario("10",nick,pass,monedas,edad));
    //         crow::json::wvalue response({{"yo", "biach"}});
    //         crow::response variable(std::move(response));
    //         variable.code = 200;
	// 	    return variable;  });

// METODO COMPRAR BARCO
	CROW_ROUTE(app, "/comprarBarco")
			.methods("POST"_method)([&lsArt](const crow::request &req)
								{
		auto x = crow::json::load(req.body);
			if (!x)
				return crow::response(400);
			
			// string name=x["nombre"].s();
			// string precio=x["precio"].s();
			// int moneda = stoi(monedas);
			string id=x["id"].s();
			string moneda=x["monedas"].s();
			int precio = stoi(moneda);
            Usuario* us = lsArt->buscarArt(id);
            // cout<<us->monedas<<" - "<<precio<<endl;
            if (us != nullptr && precio - stoi(us->monedas) >= 0){
                crow::json::wvalue response({{"monedas", precio - stoi(us->monedas)},{"id",us->id},{"name",us->nick},
                {"categoria",us->password},{"precio",us->monedas},{"src",us->edad}});
                crow::response variable(std::move(response));
                variable.code = 200;
                return variable;  
            }else{
				return crow::response(400);

            }});
// METODO EDITAR USUARIO
	CROW_ROUTE(app, "/editarUser")
			.methods("POST"_method)([listar](const crow::request &req)
								{
		auto x = crow::json::load(req.body);
			if (!x)
				return crow::response(400);
			
			string id=x["old"].s();
			string nick=x["new"].s();
			string pwd=x["pwd"].s();
			string edad=x["edad"].s();

            listar->editar(id);
                crow::json::wvalue response({{"nuevo", "done"}});
                crow::response variable(std::move(response));
                variable.code = 200;
                return variable;  });


	app.port(5000).multithreaded().run();
	return 0;
}