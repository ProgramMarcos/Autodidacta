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
            Sleep(500);
            continue;
        }

        for (int j = 0; j < MAX; j++) {
            if (letra == ascii[j][0]) { // si la letra introducida es como la de la cadena ascii
                cout << morse[j] << " "; // imprime el código morse completo de una vez
                for (int jj = 0; jj < morse[j].length(); jj++) {
                    if (morse[j][jj] == '.') {
                        Beep(300, 100);
                    } else if (morse[j][jj] == '-') {
                        Beep(700, 100);
                    }
                    Sleep(200);
                }
                break;
            }
        }
        Sleep(500);
    }
}

int main() {
    convertir("a");
    return 0;
}

