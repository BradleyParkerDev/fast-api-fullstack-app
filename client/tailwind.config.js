/** @type {import('tailwindcss').Config} */
module.exports = {
  mode: 'jit',
  content: [
    "../server/templates/**/*.{html,js,ts}",
    "../server/static/dist/**/*.{html,js,ts}",
    "/typescript/**/*.{html,js,ts}"
 
  
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
