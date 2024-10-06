import streamlit as st

# Använding av css för att byta backgrounden (för streamlit har inte)
Background_Page = '''
<style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://www.pixel4k.com/wp-content/uploads/2024/01/after-sunset-minimal-2024-4k-3840x2160_1705278513.jpg.webp");
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
    [data-testid="stBaseButton-secondary"] {
        border-color: white;
        margin-top: 20px;
        width: 120px;
        background-color: black;
    }  
    
    [id="text_input_1"]{
        background-color: black;
    }

    [data-testid="stBaseButton-headerNoPadding"] {
        visibility: hidden;
    }

    [data-testid="stSidebar"] {
        visibility: hidden;
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
    # Med hjälp av markdown kan vi använda css
st.markdown(Background_Page, unsafe_allow_html=True)

with st.container(border=True,height=250):
    user_name = st.text_input("Username", max_chars=16)
    finish = st.button("Done")
if user_name and finish:
    st.switch_page("pages/Home_Page.py")
elif not user_name and finish:
    st.error("Enter your name please")
