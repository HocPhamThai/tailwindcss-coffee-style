/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./public/**/*.{html,js}'],
  theme: {
    extend: {
      fontFamily: {
        Karla: ['Karla', 'sans-serif'],
      },
      colors: {
        coffee: {
          50: '#E8D6D0',
          200: '#C89F94',
          400: '#A25F4B',
          600: '#744838',
        },
      },
      keyframes: {
        slowDown: {
          '0%': { transform: 'translateY(-100%)' },
          '100%': { transform: 'translateY(0)' },
        },
      },
      animation: {
        slowDown: 'slowDown .4s ease-in-out',
      },
      backgroundImage: {
        'slider-bg': "url('./img/slider.jpg')",
      },
    },
  },
  plugins: [],
}
