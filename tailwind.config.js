import colors from 'tailwindcss/colors'

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.{html,js}"],
  theme: {
    extend: {
      fontFamily: {
        cabin: ['Cabin', 'sans-serif'],
        open_sans: ['"Open Sans"', 'sans-serif'],
        outfit: ['"Outfit"', 'sans-serif'],
        ubuntu: ['"Ubuntu"', 'sans-serif'],
        roboto_slab: ['"Roboto Slab"', 'sans-serif'],
      },
      colors: {
        primary: colors.red,
        'black-website': '#161616',
        'text-color': '#FFFFFF',
    },
  },
  plugins: [],
}
}
