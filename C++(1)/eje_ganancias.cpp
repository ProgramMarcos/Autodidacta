#include <iostream>


using namespace std;

int main(){
	int horas=0;
	cout<<"Cuantas horas has trabajado?: ";
	cin>>horas;
	
	if (horas<5){
		cout<<"Tu ganancia es de 5 €";
	}else if(horas>=5 && horas<11){
		cout<<"Tu ganancia es de 10 €";
	}else if (horas>10){
		cout<<"Tu ganancia 15€";
	}
	
	return 0;
}

