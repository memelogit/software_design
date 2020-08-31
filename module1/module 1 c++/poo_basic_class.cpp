#include <iostream>
#include<cstdio>
#include <string>
#include <vector>

using namespace std;
typedef unsigned char ui8;
typedef unsigned int ui32;

class Gato
{
public:
    string nombre;
    int edad;
    int peso;
    string color;

    Gato(string nom, int ed, int pes, string col)
    {
        nombre = nom;
        edad  = ed;
        peso  = pes;
        color = col;
    }

    char* detalles()
    {
        char* buffer = new char[100];
        sprintf(buffer, "%s es un gato de %d anios color %s que pesa %d kilos\n",nombre.c_str(), edad,color.c_str(), peso);
        return buffer;
    }
};


int main()
{
    Gato tom("Tom", 3, 7, "Cafe");

    char* arr = tom.detalles();
    cout << arr << endl;
    return 0;
}

