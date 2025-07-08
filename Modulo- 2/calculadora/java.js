function appendToDisplay(value) {
    document.getElementById('display').value += value;
} // appendToDisplay es para agregar el caracter al display

function clearDisplay() {
    document.getElementById('display').value = '';
} // clearDisplay es para limpiar la pantalla

function deleteLast() {
    const display = document.getElementById('display');
    display.value = display.value.slice(0, -1);
} // deleteLast es para eliminar el ultimo caracter
// calculateResult es para calcular el resultado
function calculateResult()  {
    const display = document.getElementById('display');
    let expression = display.value;

    expression = expression.replace(/%/g, '/100');                             // Si funciona 
    expression = expression.replace(/\^/g, '**') ;                             // Si funciona 

    evaluateExpression(expression, display);

} 

function replaceFunctions(expression) {

     expression = expression.replace(/raiz\(([^)]+)\)/g, 'Math.sqrt($1)');      // No funciona
    expression = expression.replace(/sin\(([^)]+)\)/g, 'Math.sin()');          // No Funciona
    expression = expression.replace(/cos\(([^)]+)\)/g, 'Math.cos($1)');        // No fuanciona
    expression = expression.replace(/tan\(([^)]+)\)/g, 'Math.tan($1)');        // No funciona
    return expression;
}

function  evaluateExpression(expression, display) {
    try {
        const result = eval(expression);
        display.value= result;

    } catch (error){
        display.value='Error';
    }
}