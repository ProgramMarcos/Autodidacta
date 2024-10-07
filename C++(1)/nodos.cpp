#include <iostream>
#include <conio.h>
#include <cmath>  // Necesario para pow()
#include <clocale>
#include <stdlib.h>

using namespace std;




int main() {
	struct nodo{
		int n; //almacena el numero del nodo
		nodo *sig; //apuntador (puntero)
	}*cab=NULL, *aux, *aux1; //la cabeza no puede apuntar a nada,
							//los elementos detrás de cabeza apuntan a cabeza
	
	 
	
	do{
		aux = (nodo*)malloc(sizeof (struct nodo)); //reservo memoria
		cout<<"Ingresa un dato : ";
		cin>>aux->n; //aux es un puntero, el dato se almacena en n
		
		if (cab==NULL){
			cab=aux1=aux;
		}
		else { //si la cabeza no es NULL es que ya existe un dato
			aux1->sig=aux;
			aux1=aux;
			aux1->sig=NULL;
		}
	}while(aux->n!=0);
	cout<<"Tu lista es : "<<endl;
	aux1=cab;
	while(aux1!=NULL){
		cout<<aux1->n<<" - ";
		aux1=aux1->sig;
	}

    return 0;
}

