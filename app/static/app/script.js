'use strict'

const form = document.querySelector('.form');
const add = document.querySelector('.add');
let count = 0

addInput()

function addInput() {
    const label = document.createElement('label');
    const input = document.createElement('input');
    count ++;
    label.classList.add('label');
    label.textContent = `name_${count}`;
    input.classList.add('input');
    input.name = `name_${count}`;
    input.type = 'text'
    label.append(input);
    form.append(label);
}

add.addEventListener('click', addInput)