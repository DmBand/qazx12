'use strict'

let oneField = document.querySelectorAll('.one-field');
let container = document.querySelector('#my-form');
let addBtn = document.querySelector('#add-form');
let total = document.querySelector('#id_form-TOTAL_FORMS');
let formNum = oneField.length - 1;
const hidden = document.querySelector('.hidden')


addBtn.addEventListener('click', addForm)

function addForm(event) {
    event.preventDefault();
    
    let newForm = oneField[0].cloneNode(true);
    let formRegex = RegExp(`form-(\\d){1}-`,'g');
    formNum++;
    let labels = newForm.querySelector('.label');
    labels.textContent = `Field ${formNum+1}`;
    newForm.innerHTML = newForm.innerHTML.replace(formRegex, `form-${formNum}-`);
    container.insertBefore(newForm, hidden);
    total.setAttribute('value', `${formNum+1}`);
}
