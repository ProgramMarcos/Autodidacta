
#include <iostream>

using namespace std;

int main(){
	int opcion = 0;
	int a,b = 0;

	cout<< "Ingresa un numero : ";
	cin>>a;
	cout<< "Ingresa otro numero : ";
	cin>>b;
	cout<<"Opcion 1 : SUMA \nOpcion 2 : RESTA \nOpcion 3 : MULTIPLICACION \n";
	cout<<"ingresa una opcion: ";
	cin>> opcion;
	switch(opcion){
		case 1:
			cout<<"Elegiste opcion 1 --> SUMA";
			cout<<"\n";
			cout<<a+b;
			break;
			
		case 2:
			cout<<"Elegiste opcion 2 --> RESTA";
			cout<<"\n";
			cout<<a-b;
			break;
			
		case 3:		
			cout<<"Elegiste opcion 3 --> MULTIPLICACION";
			cout<<"\n";
			cout<<a*b;
			break;
	}
	
	
	
	return 0;
}

