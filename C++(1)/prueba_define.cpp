#include <iostream>
//(parametros) secuencia
#define multiplicacion(a,b) a*b 
#define elevado(a) a*a

using namespace std;
int main() {
	int Multip = multiplicacion(7,9);
	cout<<"Prueba del define \n";
	cout<<Multip<<"\n";
	int elev = elevado(3);
	cout<<elev;
	return 0;
}

