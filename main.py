import streamlit as st

st.set_page_config(

    page_title="hacking",

    page_icon="::alien",

    layout="wide"

)

pg_bg_img = f"""
<style>
[data-testid="stApp"] {{
background-image: url("https://i.imgur.com/cRC0BJP.png");  
background-size: cover;
background-repeat: no-repeat;
background-attachment: local;
background-position: top left;
}}
[data-testid="stHeader"]{{
background-color: rgba(0,0,0,0);
}}

[data-testid="stSidebar"]{{
# background-color: rgba(255,255,243,50);
background-image : url("https://i.imgur.com/EXyTi7q.png")  
}}

</style>
"""

st.markdown(pg_bg_img, unsafe_allow_html=True)
c1,c2 = st.sidebar.columns(2)
with c1:
    st.markdown("""
                        <style>
                        .st-emotion-cache-1v0mbdj > img{
                        border-radius: 40%;
                            }
                        </style>
            
                        """, unsafe_allow_html=True)

    st.image("image.png")

with c2:
    st.empty()
     

