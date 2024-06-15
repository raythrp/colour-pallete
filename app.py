import streamlit as st
import numpy as np
import cv2
from colour_extract import do

st.title('Colour Pallete Extraction')
input_file = st.file_uploader('Upload a JPG, JPEG, or PNG', type=['jpg', 'jpeg', 'png'])

st.markdown(
    """
    <style>
    .color-block {
        display: inline-block;
        width: 100px;
        height: 100px;
        margin-right: 10px;
        border-radius: 5px;
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
    }
    .color-label {
        margin-top: 10px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if input_file:
    # image decode
    file_bytes = np.asarray(bytearray(input_file.read()), dtype=np.uint8)
    pic = cv2.imdecode(file_bytes, 1)

    # image handling
    st.image(cv2.cvtColor(pic, cv2.COLOR_BGR2RGB), caption='Your Image', use_column_width=True)
    st.write('')
    st.write('Finding Colour Pallete...')
    colours = do(pic)

    # colour pallet showing
    st.write('Colour Pallete')
    cols = st.columns(4)
    for i, color in enumerate(colours):
        color_hex = "#{:02x}{:02x}{:02x}".format(color[0], color[1], color[2])
        with cols[i]:
            st.markdown(
                f'<div class="color-block" style="background-color: rgb({color[0]}, {color[1]}, {color[2]});"></div>',
                unsafe_allow_html=True
            )
            st.markdown(f'<div class="color-label">RGB: {color}<br>HEX: {color_hex}</div>', unsafe_allow_html=True)