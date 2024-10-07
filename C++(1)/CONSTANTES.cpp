#include <iostream>

//DECLARACION DE CTES FUERA DEL MAIN (zona de preprocesador)
#define PI 3.14159

using namespace std;

int main(){
	float altura = 1.96;
	cout<<altura<<"\n";
	
	const float GRAVEDAD = 9.81;  //Es etico escribir las ctes en mayusculas
								  // permite diferenciarlas en el código
								  
	cout<<GRAVEDAD<<"\n"; //LAS CTES NO SE PUEDEN MODIFICAR
	
	cout<<PI;
	
	return 0;
}

