#include <iostream>
#include <conio.h>
#include <cmath>  // Necesario para pow()
#include <clocale>


using namespace std;

struct pokemon {
	char nombre[50];
	char tipo[50];
	float peso;
	char genero;
}pokemon1;//esto es una variable de tipo estructura

int main() {
	
	
	cout<<"Ingrese el nombre de su pokemon: "<<"\n";
	cin.getline(pokemon1.nombre,50,'\n');//variable, tamaño, lee hasta enter
    cout<<"Ingrese el tipo de su pokemon: "<<"\n";
	cin.getline(pokemon1.tipo,50,'\n');
	cout<<"Ingrese el peso de su pokemon: "<<"\n";
	cin>>pokemon1.peso;
	cout<<"Ingrese el genero de su pokemon: "<<"\n";
	cin>>pokemon1.genero;
	
	cout<<"Nombre: "<<pokemon1.nombre<<"\n";
	cout<<"Tipo: "<<pokemon1.tipo<<"\n";
	cout<<"peso: "<<pokemon1.peso<<"\n";
	cout<<"Genero: "<<pokemon1.genero<<"\n";
    return 0;
}

