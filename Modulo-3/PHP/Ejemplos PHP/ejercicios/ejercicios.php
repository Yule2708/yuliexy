<?

// 1. Escribe un script que cuente y muestre la cantidad de números 
//pares e impares que hay en el rango del 1 al 50.

$pares = 0;
$impares = 0;

echo "Números pares:\n";
for ($i = 1; $i <= 50; $i++) {
    if ($i % 2 == 0) {
        echo "$i ";
        $pares++;
    }
}

echo "\nTotal de números pares: $pares\n\n";

echo "Números impares:\n";
for ($i = 1; $i <= 50; $i++) {
    if ($i % 2 != 0) {
        echo "$i ";
        $impares++;
    }
}

echo "\nTotal de números impares: $impares\n";

// 2. Crea un script que genere y muestre en la terminal la tabla de multiplicar completa del 
//número 8, desde el 8x1 hasta el 8x10.

$numero = 8;

for ($i = 1; $i <= 10; $i++) {
    echo "$numero x $i = " . ($numero * $i) . "\n";
}

// 3. Desarrolla un programa que simule un juego de "adivina el número". 
//Define una variable con un número secreto y utiliza un bucle while para "intentar" 
//divinarlo incrementando un contador hasta encontrarlo, mostrando cada intento.

// 4. Escribe un script que calcule la suma de todos los números impares desde el 1 hasta el 100.

$suma = 0;

echo "Números impares del 1 al 100:\n";

for ($i = 1; $i <= 100; $i += 2) {
    echo "$i ";
    $suma += $i;
}

echo "\nSuma de números impares del 1 al 100: $suma\n";

// 5. Crea un programa que verifique si una persona puede obtener una licencia de conducir. 
//La condición es que debe tener al menos 18 años y no más de 65 años. 
//Define una variable para la edad y muestra si cumple los requisitos o no.

// 6. Utilizando bucles anidados, crea un script que dibuje un cuadrado de 5x5 en la terminal 
//utilizando el carácter #.

// 7. Desarrolla un script que determine si un número almacenado en una variable 
//es positivo, negativo o cero y muestre el resultado.

$numero = -7; // Cambiar para probar

if ($numero > 0) {
    echo "El número es positivo.\n";
} elseif ($numero < 0) {
    echo "El número es negativo.\n";
} else {
    echo "El número es cero.\n";
}

// 8. Escribe un programa que imprima los números del 1 al 30. 
//Para los múltiplos de 3, debe imprimir "Mar" en su lugar. 
//Para los múltiplos de 5, debe imprimir "Tierra". 
//Para los múltiplos de ambos (3 y 5), debe imprimir "MarTierra".

for ($i = 1; $i <= 30; $i++) {
    if ($i % 3 == 0 && $i % 5 == 0) {
        echo "MarTierra\n";
    } elseif ($i % 3 == 0) {
        echo "Mar\n";
    } elseif ($i % 5 == 0) {
        echo "Tierra\n";
    } else {
        echo "$i\n";
    }
}

// 9. Crea un script que, dada una variable numérica que representa la temperatura en grados Celsius, 
//muestre un mensaje diferente si la temperatura es "fría" (menos de 10°C), "templada" (entre 10°C y 25°C) 
//o "calurosa" (más de 25°C).

$temperatura = 45; // Cambiar para probar

if ($temperatura < 10) {
    echo "La temperatura es fría.\n";
} elseif ($temperatura <= 25) {
    echo "La temperatura es templada.\n";
} else {
    echo "La temperatura es calurosa.\n";
}

// 10. Escribe un programa que realice una cuenta regresiva para Año Nuevo desde el 10 hasta el 1. 
//Al final, debe mostrar el mensaje "¡Feliz Año Nuevo!".

for ($i = 10; $i >= 1; $i--) {
    echo "$i\n";
}

echo "¡Feliz Año Nuevo!\n";

?>