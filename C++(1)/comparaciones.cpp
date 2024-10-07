
#include <iostream>

//AND=&&
//OR=|| (Alt GR + 1)
//Negar valor -> !(valor)

using namespace std;

int main(){
	int a, b, c, d =0;
	bool respuesta=false;
	
	a=5;
	b=10;
	c=15;
	d=20;
	
	respuesta = (b>a && d>c);
	
	cout<<respuesta;
	return 0;
}

