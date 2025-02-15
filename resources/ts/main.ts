/// <reference types="webpack/module" /> 
import '../css/main.css';
import { getPokemon } from "./api/getPokemon";
import messageInnerText from './lib';


// console.log(import.meta.webpack); // without reference declared above, TypeScript will throw an error
getPokemon();

// Get the element by ID and check for null
let message = document.getElementById("message"); // Ensure the correct ID is used

if (message) { // Ensure the element is not null
    message.innerText = messageInnerText();
} else {
    console.error('Element with ID "message" not found.');
}







console.log("Hello, world!")

let helloWorld:any = document.getElementById('helloWorld')
// new comment
helloWorld.innerHTML = "Hello, Bradley!!!! Welcome to the Home Page!!!"
console.log('Hello')
let rainbow = [
    'bg-red-500',    // Red
    'bg-orange-500', // Orange
    'bg-yellow-500', // Yellow
    'bg-green-500',  // Green
    'bg-blue-500',   // Blue
    'bg-indigo-500', // Indigo
    'bg-purple-500'  // Violet (Purple)
];

let backgroundColor = 'bg-[pink]';

helloWorld.classList.add(`${backgroundColor}`)








let newElement = document.createElement('div');

document.body.appendChild(newElement)

newElement.innerHTML = 'The css is updating!'

let newElement2 = document.createElement('div');

document.body.appendChild(newElement2)

newElement2.innerHTML = 'Updated scripts in the package.json!'

let colorButton = document.createElement('button');
colorButton.type = 'button'; // Setting the type attribute
document.body.appendChild(colorButton);
colorButton.innerHTML = 'Color Button';


colorButton.classList.add(`bg-[pink]`, 
                        'border-black', 
                        'border-solid', 
                        'border-[2px]',
                        'rounded-[5px]',
                        );

// Variable to keep track of the current color index
let currentColorIndex = 0;

colorButton.addEventListener('click', () => {
    // Remove the current color class
    helloWorld.classList.remove(rainbow[currentColorIndex]);
    
    // Move to the next color, cycling back to the start if necessary
    currentColorIndex = (currentColorIndex + 1) % rainbow.length;

    // Add the new color class
    helloWorld.classList.add(rainbow[currentColorIndex]);
});


