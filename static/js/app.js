// Funcionamiento del filtro de busqueda por precio
const MAXIMO = 80000;
const range = document.getElementById('range');
const min = document.getElementById('min-value');
const max = document.getElementById('max-value');

console.log(range.value)
min.value = 0.0
const initial = (range.value / 100) * MAXIMO

max.value = initial

range.addEventListener('change', (e) => {
    let max_price = (range.value / 100) * MAXIMO
    max.value = max_price
})

