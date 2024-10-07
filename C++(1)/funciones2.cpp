#include <iostream>

using namespace std;

void suma(int a=5);


int main(){
	suma(); //devuelve 5*10=50
	suma(6); //devuelve 6*10=60
	return 0;
}
void suma(int a){
	cout<<a*10<<"\n";
	
}

