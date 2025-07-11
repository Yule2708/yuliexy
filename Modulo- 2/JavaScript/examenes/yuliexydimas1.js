// Examen Práctico de JavaScript: Módulos 1-3

//Instrucciones:**  
//Resuelve los siguientes 10 ejercicios. 
//Escribe el código JavaScript necesario para cumplir con los requisitos de cada problema. 
//Se evaluará la correcta utilización de variables, operadores, condicionales y bucles.

// 1️⃣ Perfil de Producto

//Declara variables para describir un producto de una tienda online:

//Usa `const` para el nombre del producto (`nombreProducto`), que será **"Tablet 10 pulgadas"**.
//Usa `let` para el precio (`precio`), que será **450.99**.
//Usa `let` para la cantidad en stock (`stock`), que será **25**.
//Usa `const` para si el producto tiene envío gratis (`envioGratis`), que será **true**.

//Finalmente, muestra cada una de estas variables en la consola con un mensaje descriptivo.  
//Ejemplo: `Nombre del producto: Tablet 10 pulgadas`.

const nombre_del_producto = "Tabla 10 pulgadas";
let precio = 450.99;
let stock= 25;
const envioGratis = true

console.log(`Nombre del producto: ${nombre_del_producto}`);
console.log(`Precio: ${precio}`);
console.log(`stock: ${stock}`);
console.log(`Haces envios gratis: ${envioGratis}`);

// 2️⃣ Cálculo de Total de Compra

//Usando las variables del ejercicio anterior, un cliente compra **2 tablets**.  
//Calcula el subtotal (`precio * cantidad`).  
//Luego, calcula el total final añadiendo un **7% de impuesto** sobre el subtotal.  
//Muestra en la consola el subtotal y el total final formateado a 2 decimales.

const nombre_del_producto1 = "Tabla 10 pulgadas";
let compra = "2 tablets";
let precio1 = 450.99;
let stock1= 2;
let multiplicacion = precio1 * stock1; 
const envioGratis1 = true

let impuesto = 0.07;
let subtotal = multiplicacion;
let totalFinal = subtotal + (subtotal * impuesto);

console.log(`Nombre del producto: ${nombre_del_producto1}`);
console.log(`Precio: ${precio1}`);
console.log(`Multiplicación: ${multiplicacion}`);
console.log(`Subtotal: ${subtotal.toFixed(2)}`);
console.log(`Total final: ${totalFinal.toFixed(2)}`);


// 3️⃣ Verificación de Edad para Conducir

//Crea una variable `edadUsuario` con un valor de **20**.  
//Usando una estructura `if/else`, determina si el usuario es mayor de edad para conducir
// (edad mínima 18 años).

//- Si es mayor o igual a 18, muestra en consola: **"Puedes obtener tu licencia de conducir."**
//- Si es menor de 18, muestra: **"Aún no tienes la edad para obtener la licencia."**

let edadUsuario = 20;

if (edadUsuario >= 18) {
    console.log("Puedes obtener tu licencia de conducir.");
}
else {
    console.log("Aún no tienes la edad para obtener la licencia.");
}

// 4️⃣ Sistema de Semáforo

//Declara una variable `colorSemaforo` y asígnale un valor ("verde", "amarillo" o "rojo").  
//Usando `if`, `else if` y `else`, crea un programa que muestre un mensaje diferente según el color:

//- Si es "verde", muestra **"Puede avanzar."**
//- Si es "amarillo", muestra **"Reduzca la velocidad, precaución."**
//- Si es "rojo", muestra **"Debe detenerse."**
//- Si es cualquier otro color, muestra **"Color no válido."**

let colorSemaforo = "verde";

if (colorSemaforo === "verde") {
    console.log("Puede avanzar.");
} 
else if (colorSemaforo === "amarillo") {
    console.log("Reduzca la velocidad, precaución.");
} 
else if (colorSemaforo === "rojo") {
    console.log("Debe detenerse.");
} 
else {    
    console.log("Color no válido.");
}

// 5️⃣ Menú del Día con switch

//Crea una variable `diaSemana` con el valor **3**.  
//Usando una estructura `switch`, crea un programa que muestre el plato del día según el número:

//- **Lunes:** Lentejas
//- **Martes:** Pollo al horno
//- **Miércoles:** Pescado a la plancha
//- **Jueves:** Pasta
//- **Viernes:** Paella

//Para cualquier otro número, debe mostrar **"Día no válido para menú."**

 let Dia_Semana=3;

 switch(Dia_Semana){

    case 1:
        console.log("Lunes: Lentejas");
        break;

        case 2:
        console.log("Martes: Pollo al horno");
        break;

        case 3:
        console.log("Miercoles: Pescado a la Plancha");
        break;

        case 4:
        console.log("Jueves: Pasta");
        break;

        case 5:
        console.log("Viernes: Paella");
        break;

        default:
        console.log("Dia no valido para menú.");
        break;
 }

// 6️⃣ Números Pares con for

//Usando un bucle `for`, escribe un programa que imprima en la consola 
// **todos los números pares del 2 al 20** (inclusive).

for(let i=2; i=20; i=+20){

    if(i%2===0){
        console.log(i);
    }
}

// 7️⃣ Cuenta Regresiva con while

//Usando un bucle `while`, crea un programa que simule una cuenta regresiva para un cohete.  
//Debe imprimir en la consola los números del **10 al 1**, y al final, imprimir **"¡Despegue!"**.

let cuenta_regresiva=10;
 
while(cuenta_regresiva>=1){
    console.log(cuenta_regresiva);
    cuenta_regresiva--;
}
console.log("¡Despegue!");

//## 8️⃣ El Reto "FizzBuzz"

//Escribe un programa que use un bucle `for` para iterar del **1 al 50**. Para cada número, 
// aplica las siguientes reglas:

//- Si el número es divisible por 3, imprime **"Fizz"**.
//- Si el número es divisible por 5, imprime **"Buzz"**.
//- Si el número es divisible por 3 y por 5, imprime **"FizzBuzz"**.
//- Si no cumple ninguna de las anteriores, imprime el número.

//💡 *Pista: Necesitarás el operador módulo (%).*

for (let i=1; i<=50; i++){

    if (i%3 === 0 && i%5 == 0){
        console.log("FizzBuzz");
    }
    else if (i%3 === 0){
        console.log("Fizz");
    }
    else if (i%5===0){
        console.log("Buzz");
    }
    else {
        console.log(i);   
    }
}

// 9️⃣ Suma de los Primeros 100 Números

//Crea una variable `sumaTotal` inicializada en **0**.  
//Usando un bucle `for`, calcula la suma de todos los números del **1 al 100** 
// y almacena el resultado en `sumaTotal`.  
//Al final del bucle, imprime el valor de `sumaTotal` en la consola.

let Suma_Total=0;

for (let i=1; i<=100; i++){
    Suma_Total += i; 
}
console.log(`La suma total de los primeros 100 numeros es: ${Suma_Total}`);

// 🔟 Acceso a Evento Exclusivo

//Un usuario quiere entrar a un evento. Las condiciones son:  
//- Ser mayor de edad (`edad >= 18`) **Y**  
//- Tener una entrada (`tieneEntrada = true`)

//Declara dos variables:  
//- `edad` con valor **19**  
//- `tieneEntrada` con valor **false**

//Usando operadores lógicos (`&&`), evalúa si el usuario puede pasar.  
//Muestra en consola **"Acceso concedido"** o **"Acceso denegado"** según el resultado.  
//Cambia los valores de las variables para probar ambos casos.

let edad= 19;
let tiendaEntrada= false;

if (edad >= 18 && tiendaEntrada){
    console.log("Acceso concedido");
}
else {
    console.log("Acceso denegado");
}