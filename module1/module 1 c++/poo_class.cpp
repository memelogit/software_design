#include <iostream>
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
};


int main()
{
    Gato tom;
    Gato luna;

    tom.nombre = "Tom";
    tom.edad   = 3;
    tom.peso   = 7;
    tom.color  = "Cafe";

    luna.nombre = "Luna";
    luna.edad   = 2;
    luna.peso   = 5;
    luna.color  = "Gris";

    cout << tom.nombre << endl;
    cout << luna.nombre << endl;

    return 0;
}

