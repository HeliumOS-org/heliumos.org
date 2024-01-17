/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["**/*.html"],
    theme: {
        extend: {},
    },
    daisyui: {
        themes: [
            {
                mytheme: {
                    "primary": "#3daee9",
                    "secondary": "#eff0f1",
                    "accent": "#3daee9",
                    "neutral": "#eff0f1",
                    "base-100": "#fcfcfc",
                    "info": "#3daee9",
                    "success": "#27ae60",
                    "warning": "#f67400",
                    "error": "#da4453",
                },
            },
        ],
    },
    plugins: [require("daisyui")],
}
