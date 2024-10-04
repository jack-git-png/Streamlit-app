import streamlit as st

# Använding av css för att byta backgrounden (för streamlit har inte)
Background_Page = '''
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://asset.gecdesigns.com/img/wallpapers/beautiful-fantasy-wallpaper-ultra-hd-wallpaper-4k-sr10012418-1706506236698-cover.webp");
        background-size: cover;
        background-position: center;
        align-items: center;
    }
    [data-testid="stHeader"] {
        background: rgba(0,0,0,0);
    }
    [data-testid="stToolbar"] {
        right: 2rem;
    }
    [data-testid="stVerticalBlockBorderWrapper"] {
        background: linear-gradient(135deg, rgba(255,255,255,0.18));
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border-radius: 20px;
        border: 1px solid rgba(255,255,255,0.18);
        box-shadow: 0 8px 32px 0 rgba(0,0,0,0.37);
        align-content: center;
        text-align: center;
    }
    [data-testid="stVerticalBlock"] {
        display: contents;
        padding: 10%
    }
    [data-testid="stTextInputRootElement"] {
        border-radius: 15px;
        border-color: white;
    }
    [data-testid="stTextInputRootElement"]:hover{
        border-color: grey;
    }
    [id="text_input_1"]{
        background-color: black;
    }
    [data-testid="stBaseButton-secondary"] {
        border-color: white;
        margin-top: 20px;
        width: 120px;
        background-color: black;
    }  
    [data-testid="stBaseButton-secondary"]:hover{
        border-color: grey;
        -webkit-text-fill-color: grey;
    }
    [data-testid="stBaseButton-headerNoPadding"] {
        visibility: hidden;
    }
    </style>
    '''
    # Med hjälp av markdown kan vi använda css
st.markdown(Background_Page, unsafe_allow_html=True)
    
with st.container(border=True,height=250):
    user_name = st.text_input(f"{:bust_in_silhouette:} Username", max_chars=16)
    finish = st.button("Done")
