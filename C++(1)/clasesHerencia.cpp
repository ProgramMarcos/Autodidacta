#include <iostream>
#include <conio.h>
#include <cmath>  // Necesario para pow()
#include <clocale>


using namespace std;


//declaro la clase
class Pokemon{
	//Atributos (variables)
	public:
		string nombre;
		float peso;
	//Metodos (funciones) y constructor
	public:
		Pokemon(string, float); //constructor <---------
		void Saludo(); 
	
};

//inicializo el constructor
Pokemon::Pokemon(string _nombre, float _peso){
	nombre = _nombre; //inicializo las variables 
	peso = _peso;
}


void Pokemon::Saludo(){
	cout<<"El pokemon que te saluda es: "<<nombre<<", que pesa "<<peso<<" Kg.\n";
}

//CLASE HIJA ---> HEREDA DE CLASE PADRE
class Pokemones_fuego : public Pokemon{ //no tengo que declarar nombre y peso, los heredo de la clase anterior
	public:
		int vida;
		char genero;
	public:
		Pokemones_fuego(string , float, int, char); //hay que poner primero los tipos de dato de la clase padre
		void Mostrar_Pokemon();
	
};

Pokemones_fuego::Pokemones_fuego(string _nombre, float _peso, int _vida, char _genero) : Pokemon(_nombre, _peso){
	vida = _vida;
	genero = _genero;
}

void Pokemones_fuego::Mostrar_Pokemon(){
	Saludo();
	cout<<"El pokemon tiene  "<<vida<<" PS, y su genero es "<<genero;
}

int main() {
	
	Pokemones_fuego pokemon1("Chocholuis", 0.95, 60, 'm');
	pokemon1.Mostrar_Pokemon();
    return 0;
}

