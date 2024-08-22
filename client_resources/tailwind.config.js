/** @type {import('tailwindcss').Config} */
module.exports = {
  mode: 'jit',
  content: [
    "../templates/**/*.{html,js,ts}",
    "../static/dist/**/*.{html,js,ts}",
    "/typescript/**/*.{html,js,ts}"

  
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
