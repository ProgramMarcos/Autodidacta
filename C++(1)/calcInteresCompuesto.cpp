#include <iostream>
#include <conio.h>
#include <cmath>  // Necesario para pow()
#include <clocale>

using namespace std;

int main() {
    setlocale(LC_CTYPE, "Spanish");  // Para caracteres especiales en español (ñ, á, etc.)

    float CapIni = 0;
    float TasaInteres = 0;
    int tiempo = 0;
    float resultado = 0;

    while (CapIni <= 0) {
        cout << "Ingrese capital inicial : ";
        cin >> CapIni;
    }
    while (TasaInteres <= 0) {
        cout << "Ingrese la tasa de interés anual : ";
        cin >> TasaInteres;
    }
    while (tiempo <= 0) {
        cout << "Ingrese el tiempo en años : ";
        cin >> tiempo;
    }

    // Cálculo del monto final con interés compuesto
    resultado = CapIni * pow(1 + TasaInteres / 100, tiempo);

    cout << "El dinero generado es de : $" << resultado;
    getch();  // Espera a que toquemos una tecla al finalizar
    return 0;
}

