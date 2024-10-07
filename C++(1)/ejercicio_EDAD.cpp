#include <iostream>


using namespace std;

int main(){
	int edad=0;
	
	cout<<"Ingrese su edad: ";
	cin>>edad;
	
	if (edad<18){
		cout<<"No se admiten menores";
	}else{
		cout<<"Pase y disfrute";
	}

	
	return 0;
}

