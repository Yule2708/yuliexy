//📘 EXAMEN DE PROGRAMACIÓN EN C++

//🧪 Ejercicio 1: "Hola Mundo" y Tipos de Datos
//Escribe un programa que imprima en la consola el mensaje "¡Hola, Mundo!". 
// Luego, declara e inicializa una variable para cada uno de los siguientes tipos de datos:
//- Entero (int)
//- Flotante (float)
//- Carácter (char)
//- Booleano (bool)

//Finalmente, imprime el valor de cada una de estas variables.

//📚 Temas: iostream, Variables, Tipos de datos.

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

//🧮 Ejercicio 2: Operadores y Librería cmath
//Crea un programa que solicite al usuario dos números. El programa debe calcular y mostrar:
//- La suma, resta, multiplicación y división de los dos números.
//- Utilizando la librería <cmath>, calcula y muestra 
// la potencia del primer número elevado al segundo y la raíz cuadrada del primer número.

//📚 Temas: Operadores, iostream, Librería cmath.

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

//🔍 Ejercicio 3: Condicionales if-else
//Desarrolla un programa que pida al usuario su edad. 
// El programa debe utilizar una estructura condicional if-else para determinar si el usuario es 
// mayor de edad (18 años o más) y mostrar un mensaje apropiado en la pantalla.

//📚 Temas: Condicionales, Operadores, Variables.

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

//🔁 Ejercicio 4: Bucle for y Constantes con #define
//Utiliza #define para crear una constante simbólica llamada LIMITE con un valor de 10. 
//Luego, escribe un programa que pida al usuario un número y utilice un bucle for para 
//imprimir la tabla de multiplicar de ese número desde 1 hasta LIMITE.

//📚 Temas: Bucle for, #define, iostream.

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

//🎯 Ejercicio 5: Bucle while
//Crea un programa que simule un juego de adivinanza. 
// El programa debe generar un número secreto (por ejemplo, int numeroSecreto = 42;). 
// Luego, debe pedir al usuario que adivine el número. 
// Utiliza un bucle while para que el programa siga pidiendo un número mientras el usuario no adivine el correcto. 
// Proporciona pistas como "más alto" o "más bajo".

//📚 Temas: Bucle while, Condicionales, Variables.

#include <iostream>

int main() {
    int numeroSecreto = 20;
    int intento = 0;

    std::cout << "Adivina el número secreto: ";
    std::cin >> intento;

    while (intento != numeroSecreto) {
        if (intento < numeroSecreto)
            std::cout << "Más alto. Intenta de nuevo: ";
        else
            std::cout << "Más bajo. Intenta de nuevo: ";
        std::cin >> intento;
    }

    std::cout << "¡Correcto! Has adivinado el número." << std::endl;
    return 0;
}

//📋 Ejercicio 6: Bucle do-while y switch
//Escribe un programa que muestre un menú simple con tres opciones:
//1. Saludar
//2. Despedirse
//3. Salir

//El programa debe usar un bucle do-while para mostrar el menú repetidamente hasta que 
// el usuario elija la opción "Salir". 
// Utiliza una estructura switch para manejar la opción seleccionada por el usuario y mostrar 
// el mensaje correspondiente.

//📚 Temas: Bucle do-while, Condicionales switch, iostream.

#include <iostream>

int main() {
    int opcion;

    do {
        std::cout << "\n Menu: " << std::endl;
        std::cout << "1. Saludar" << std::endl;
        std::cout << "2. Despedirse" << std::endl;
        std::cout << "3. Salir" << std::endl;
        std::cout << "Elige una opcion: ";
        std::cin >> opcion;

        switch (opcion) {
            case 1:
                std::cout << "¡Hola!" << std::endl;
                break;
            case 2:
                std::cout << "¡Adiós!" << std::endl;
                break;
            case 3:
                std::cout << "Saliendo del programa..." << std::endl;
                break;
            default:
                std::cout << "Opción no válida." << std::endl;
        }
    } while (opcion != 3);

    return 0;
}

//📐 Ejercicio 7: Funciones con Valor de Retorno
//Desarrolla un programa que contenga una función llamada calcularAreaRectangulo.
//- Declara (Prototipo) la función al inicio del programa.
//- La función debe recibir dos parámetros de tipo float: la base y la altura.
//- La función debe devolver el área calculada.
//- Desde la función main, solicita al usuario la base y la altura, llama a la función y muestra el resultado.

//📚 Temas: Declaración y Definición de Funciones, Función que devuelve valor y recibe parámetros.

#include <iostream>

float calcularAreaRectangulo(float base, float altura);  // Prototipo

int main() {
    float base, altura;
    std::cout << "Ingrese la base: ";
    std::cin >> base;
    std::cout << "Ingrese la altura: ";
    std::cin >> altura;

    float area = calcularAreaRectangulo(base, altura);
    std::cout << "Área del rectángulo: " << area << std::endl;

    return 0;
}

float calcularAreaRectangulo(float base, float altura) {
    return base * altura;
}

//🔄 Ejercicio 8: Paso por Valor vs. Paso por Referencia
//Crea un programa que demuestre la diferencia entre el paso por valor y el paso por referencia.
//- Define una función void llamada modificarPorValor que reciba un entero por valor 
// y le sume 10 dentro de la función.
//- Define otra función void llamada modificarPorReferencia que reciba un entero por referencia y le sume 10.
//- En main, declara una variable entera llamada numero e inicialízala en 20. Imprime su valor, 
// llama a modificarPorValor, vuelve a imprimir numero. Luego, llama a modificarPorReferencia 
// y vuelve a imprimir el valor de numero para observar la diferencia.

//📚 Temas: Paso por valor vs. Paso por referencia, Funciones.

#include <iostream>

void modificarPorValor(int num) {
    num += 25;
}

void modificarPorReferencia(int &num) {
    num += 25;
}

int main() {
    int numero = 20;
    std::cout << "Valor original: " << numero << std::endl;

    modificarPorValor(numero);
    std::cout << "Después de modificarPorValor: " << numero << " (Sin Nungun Cambio)"<< std::endl;

    modificarPorReferencia(numero);
    std::cout << "Después de modificarPorReferencia: " << numero <<" (Modificado)" << std::endl;

    return 0;
}

//🍽️ Ejercicio 9: Librerías vector y string
//Escribe un programa que pida al usuario que ingrese 3 de sus comidas favoritas. 
//Almacena cada comida en un vector de tipo string. Después de que el usuario haya ingresado las tres, 
//utiliza un bucle para recorrer el vector e imprimir cada una de las comidas en la consola.

//📚 Temas: Librería vector, Librería string, Bucles.

#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
    vector<string> comidas;
    string comida;

    for (int i = 0; i < 3; i++) {
        cout << "Ingrese una comida favorita: ";
        getline(cin, comida);
        comidas.push_back(comida);
    }

    cout << "\nTus comidas favoritas son:\n";
    for (string c : comidas) {
        cout << "- " << c << endl;
    }

    return 0;
}

//🧮 Ejercicio 10: Constantes const y Funciones void
//Crea un programa para calcular el perímetro de un círculo.
//- Declara una constante de tipo double usando la palabra clave const para el valor de Pi (π≈3.14159).
//- Escribe una función void llamada calcularPerimetro que no devuelva ningún valor pero que reciba como parámetro el radio del círculo.
//- Dentro de esta función, calcula el perímetro (2⋅π⋅radio) y muéstralo directamente en la consola.
//- Desde main, pide al usuario el radio y llama a la función calcularPerimetro.

//📚 Temas: const, Función que no devuelve valor, Parámetros de función.