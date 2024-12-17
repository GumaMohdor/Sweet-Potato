/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./public/**/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        transparent: 'transparent',
        current: 'currentColor',
        'sweetPotato': 'C39BD3',
        'lightpotato': 'F4E3B6',
        'brownpotato': 'D89A73' 
      },
    },
  plugins: [],
  }
}
