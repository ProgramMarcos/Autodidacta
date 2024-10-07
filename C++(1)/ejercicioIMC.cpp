/*
realizar un programa que calcule el índice de masa 
corporal o IMC
*/

//IMC=Peso/Altura^2
#include <iostream>
#include <math.h>
#include <iomanip>

using namespace std;

int main(){
	float peso = 0; //se inicializa a 0 para que no salgan valores en memoria
	float altura = 0;
	float resultado = 0;
	
	cout<<"Calculadora IMC\n";
	cout<<"Ingrese su peso en KG: ";
	cin>>peso;
	
	cout<<"ingrese altura en METROS :";
	cin>>altura;
	
	//resultado = peso/(altura*altura);
	resultado = peso/pow(altura,2);
	cout<<"su IMC es: "<<setprecision(4)<<resultado<<"kg/m^2"; //precisión de 4 nums
	return 0;
}

