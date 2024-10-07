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


int main() {
	
	
	//crear objeto, FORMA 1 (larga)
	Pokemon pokemon1 = Pokemon("Chikorita",0.75);
	pokemon1.Saludo();
	
	//crear objeto, FORMA 2 (corta)
	Pokemon pokemon2("Charmander",0.93);
	pokemon2.Saludo();
    return 0;
}

