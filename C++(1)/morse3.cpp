#include <iostream>
#include <string>
#include <Windows.h>
#define MAX 96 // creo cte de modo global

using namespace std;

string morse[] = {".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..",
                  "--", "-.", "--.--", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--",
                  "-..-", "-.--", "--..", "-----", ".----", "..---", "...--", "....-", ".....", "-....",
                  "--...", "---..", "----.", ".-.-.-", "--..--", "..--..", "-....-", "-..-.", ".--.-.",
                  "-...-", "-.-.--", "---..."};

string ascii[] = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P",
                  "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5",
                  "6", "7", "8", "9", ".", ",", "?", "-", "/", "@", "=", "!", ":"};

void convertir(string cadena) {
    for (int i = 0; i < cadena.length(); i++) {
        char letra = toupper(cadena[i]); // poner toda la cadena en mayúscula

        if (letra == ' ') {
            cout << " ";
            Sleep(500); // pausa más larga para los espacios
            continue;
        }

        for (int j = 0; j < MAX; j++) {
            if (letra == ascii[j][0]) { // si la letra introducida es como la de la cadena ascii
                for (int jj = 0; jj < morse[j].length(); jj++) {
                    if (morse[j][jj] == '.') {
                        cout << ".";   // imprime el punto
                        Beep(300, 100); // sonido del punto (tono más bajo)
                    } else if (morse[j][jj] == '-') {
                        cout << "-";   // imprime el guion
                        Beep(700, 100); // sonido del guion (tono más alto)
                    }
                    Sleep(200); // pequeña pausa entre símbolos
                }
                cout << " "; // espacio entre letras
                break;
            }
        }
        Sleep(500); // pausa más larga entre letras
    }
}

int main() {
    string salida;
	cout<<"¿Que debo convertir? : ";
	cin>> salida;
	convertir(salida);
	return 0;
}

