#include <iostream>
#include <conio.h>
#include <cmath>  // Necesario para pow()
#include <clocale>


using namespace std;

int main() {
	int tamanio = 0, a=0, suma=0;

	
	cout<<"Ingresa el numero de notas a registrar: ";
	cin>>tamanio;
	
	int notas[tamanio];
	
	for (int x = 0 ; x<tamanio; x++){
		cout<<"Ingresa la nota #"<<x+1<<": ";
		cin>>a;
		notas[x]=a;
		suma+=notas[x];
		
	}
	cout<<" Tu promedio es: "<<(float)suma/tamanio;
    return 0;
}

