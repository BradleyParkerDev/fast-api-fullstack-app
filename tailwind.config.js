/** @type {import('tailwindcss').Config} */
module.exports = {
  mode: 'jit', 
  content: 
  [
    "./resources/**/*.{html,js,jsx,ts,tsx}",
    "./resources/templates/**/*.{html,js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      screens:{
        'sm': '640px',
        'md': '768px',
        'lg': '1024px',
        'xl': '1280px',
        '2xl': '1536px',
      }
    },
  },
  plugins: [],
}