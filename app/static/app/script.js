'use strict'

const form = document.querySelector('.form');
const add = document.querySelector('#add');
let count = 0

addInput()

function addInput() {
    const label = document.createElement('label');
    const input = document.createElement('input');
    count ++;
    label.classList.add('label');
    label.textContent = `Field ${count}`;
    input.classList.add('input');
    input.name = `field_${count}`;
    input.type = 'text';
    input.required = true;
    label.append(input);
    form.append(label);
}

add.addEventListener('click', addInput)