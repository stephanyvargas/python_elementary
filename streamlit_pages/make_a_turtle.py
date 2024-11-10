# streamlit_pages/mix_colors.py

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def mix_colors():
    st.write("### Let's Mix Colors 🎨")
    st.write("Use the sliders to mix red, green, and blue to make colors!")

    # Fun Explanation
    st.write("""
        **Did you know?** Colors on screens are made by mixing three colors: **Red**, **Green**, and **Blue**!
        Each color can have a strength from **0** (completely off) to **255** (the brightest possible).
        When we change the strength of red, green, or blue, we create new colors!

        Try moving the sliders below and watch how the color changes.
        - If you set **Red**, **Green**, and **Blue** to the same number, you get a shade of gray.
        - Setting **Red** to 255 and **Green** and **Blue** to 0 gives you a pure red color.
        - Mixing full **Red** and **Green** but no **Blue** gives you **Yellow**!

        Can you make your favorite color by adjusting the sliders? 🎨
    """)

    # Color sliders
    red = st.slider("Red", 0, 255, 127)
    green = st.slider("Green", 0, 255, 127)
    blue = st.slider("Blue", 0, 255, 127)

    # Displaying the color
    color = f"rgb({red}, {green}, {blue})"
    st.write(f"Your mixed color: {color}")
    st.markdown(f'<div style="width:200px;height:100px;background-color:{color};"></div>', unsafe_allow_html=True)
