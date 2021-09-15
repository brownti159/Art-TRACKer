const colors = require('tailwindcss/colors')

module.exports = {
  purge: [],
  darkMode: false, // or 'media' or 'class'
  theme: {
    color:{
      transparent: 'transparent',
      current: 'currentColor',
      blue: colors.cyan,
    },
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
