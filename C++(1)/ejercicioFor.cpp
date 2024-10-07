#include <iostream>
#include <conio.h>
#include <cmath>  // Necesario para pow()
#include <clocale>


using namespace std;

int main() {
	
	int prueba[4],a;
	for (int i = 0; i<5; i++){
		cout<<"Ingresa un dato: ";
		cin>>a;
		prueba[i] = a;
	}
    
    for (int i = 0; i<5; i++){
		cout<<prueba[i]<<endl;

	}
    return 0;
}

