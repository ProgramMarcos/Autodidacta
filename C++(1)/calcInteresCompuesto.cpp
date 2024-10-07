#include <iostream>
#include <conio.h>
#include <cmath>  // Necesario para pow()
#include <clocale>

using namespace std;

int main() {
    setlocale(LC_CTYPE, "Spanish");  // Para caracteres especiales en espa�ol (�, �, etc.)

    float CapIni = 0;
    float TasaInteres = 0;
    int tiempo = 0;
    float resultado = 0;

    while (CapIni <= 0) {
        cout << "Ingrese capital inicial : ";
        cin >> CapIni;
    }
    while (TasaInteres <= 0) {
        cout << "Ingrese la tasa de inter�s anual : ";
        cin >> TasaInteres;
    }
    while (tiempo <= 0) {
        cout << "Ingrese el tiempo en a�os : ";
        cin >> tiempo;
    }

    // C�lculo del monto final con inter�s compuesto
    resultado = CapIni * pow(1 + TasaInteres / 100, tiempo);

    cout << "El dinero generado es de : $" << resultado;
    getch();  // Espera a que toquemos una tecla al finalizar
    return 0;
}

