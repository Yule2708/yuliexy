//📘 EXAMEN DE PROGRAMACIÓN EN C++

//🧪 Ejercicio 1: "Hola Mundo" y Tipos de Datos
//Escribe un programa que imprima en la consola el mensaje "¡Hola, Mundo!". 
// Luego, declara e inicializa una variable para cada uno de los siguientes tipos de datos:
//- Entero (int)
//- Flotante (float)
//- Carácter (char)
//- Booleano (bool)

//Finalmente, imprime el valor de cada una de estas variables.

#include <iostream>
using namespace std;

int main() {
    cout << "¡Hola, Mundo!" << endl;

    int entero = 50;
    float flotante = 5.55;
    char caracter = 'A';
    bool booleano = true;

    cout << "Entero: " << entero << endl;
    cout << "Flotante: " << flotante << endl;
    cout << "Carácter: " << caracter << endl;
    cout << "Booleano: " << booleano << endl;

    return 0;
}

//📚 Temas: iostream, Variables, Tipos de datos.

//🧮 Ejercicio 2: Operadores y Librería cmath
//Crea un programa que solicite al usuario dos números. El programa debe calcular y mostrar:
//- La suma, resta, multiplicación y división de los dos números.
//- Utilizando la librería <cmath>, calcula y muestra 
// la potencia del primer número elevado al segundo y la raíz cuadrada del primer número.

#include <iostream>
#include <cmath>
using namespace std;

int main() {
    double numero1, numero2;
    cout << "Ingrese el primer número: ";
    cin >> numero1;
    cout << "Ingrese el segundo número: ";
    cin >> numero2;

    cout << "Suma: " << numero1 + numero2 << endl;
    cout << "Resta: " << numero1 - numero2 << endl;
    cout << "Multiplicación: " << numero1 * numero2 << endl;
    cout << "División: " << numero1 / numero2 << endl;
    cout << "Potencia: " << pow(numero1, numero2) << endl;
    cout << "Raíz cuadrada del primer número: " << sqrt(numero1) << endl;

    return 0;

}

//📚 Temas: Operadores, iostream, Librería cmath.

//🔍 Ejercicio 3: Condicionales if-else
//Desarrolla un programa que pida al usuario su edad. 
// El programa debe utilizar una estructura condicional if-else para determinar si el usuario es 
// mayor de edad (18 años o más) y mostrar un mensaje apropiado en la pantalla.

#include <iostream>
using namespace std;

int main() {
    int edad;
    cout << "Ingrese su edad: ";
    cin >> edad;

    if (edad >= 18) {
        cout << "Eres mayor de edad." << endl;
    } else {
        cout << "Eres menor de edad." << endl;
    }

    return 0;
}

//📚 Temas: Condicionales, Operadores, Variables.

//🔁 Ejercicio 4: Bucle for y Constantes con #define
//Utiliza #define para crear una constante simbólica llamada LIMITE con un valor de 10. 
//Luego, escribe un programa que pida al usuario un número y utilice un bucle for para 
//imprimir la tabla de multiplicar de ese número desde 1 hasta LIMITE.

#include <iostream>
#define LIMITE 10
using namespace std;

int main() {
    int numero;
    cout << "Ingrese un número: ";
    cin >> numero;

    for (int i = 1; i <= LIMITE; i++) {
        cout << numero << " x " << i << " = " << numero * i << endl;
    }

    return 0;
}

//📚 Temas: Bucle for, #define, iostream.

//🎯 Ejercicio 5: Bucle while
//Crea un programa que simule un juego de adivinanza. 
// El programa debe generar un número secreto (por ejemplo, int numeroSecreto = 42;). 
// Luego, debe pedir al usuario que adivine el número. 
// Utiliza un bucle while para que el programa siga pidiendo un número mientras el usuario no adivine el correcto. 
// Proporciona pistas como "más alto" o "más bajo".

