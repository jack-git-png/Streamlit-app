import streamlit as st

Styling = '''
<style>

.st-emotion-cache-1yiq2ps{
    background-image: url("https://i.pinimg.com/originals/a8/55/df/a855df51ab9b3b503221419fd614970f.png");
    background-size: cover;
    position: absolute;
    background-position: center;
    justify-content: center;
    align-items: center;
    
}

[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}

[data-testid="stToolbar"] {
    right: 2rem;
}

[data-testid="stBaseButton-secondary"] {
    padding: 30px;
    margin-top: 30%;
    height: 80px;
    border-color: white;
    background-image: url(https://thumbs.dreamstime.com/b/vector-landscape-blue-sky-clouds-sunset-anime-cartoon-clean-style-background-design-171922579.jpg);
    background-repeat: no-repeat;
    box-shadow: 0 8px 32px 0 rgba(0,0,0,0.37);
    align-content: center
    
}

[data-testid="stVerticalBlockBorderWrapper"] {
    text-align: center;
    border-radius: 40px;
    border-color: white;
    backdrop-filter: blur(5px);
    -webkit-backdrop-filter: blur(1px);
    align-contents: center;
    backdrop-filter: drop-shadow(0 8px 32px 0 rgba(0,0,0,0.37));
    
}
[data-testid="stVerticalBlock"] {
    display: contents;
}

[data-testid="stMarkdownContainer"]{
    color: #fff;
    text-shadow:
    0 0 5px #fff,
    0 0 10px #fff,
    0 0 21px #fff,
    0 0 42px #0fa,
    0 0 82px #0fa,
    0 0 92px #0fa,
    0 0 90px #0fa,
    0 0 120px #0fa; 
}
</style>
'''

st.markdown(Styling, unsafe_allow_html=True)

with st.container(border=True,height=300):
    col1,col2 = st.columns((2,2))
    with col1:
        Docs = st.button("Documment")
    with col2:
        Settings = st.button("Settings")
    if Docs:
        st.switch_page("pages/Documment.py")
    if Settings:
        st.switch_page("pages/Settings.py")
