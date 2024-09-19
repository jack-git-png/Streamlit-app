import streamlit as st

# Använding av css för att byta backgrounden (för streamlit har inte)
page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://www.pixelstalk.net/wp-content/uploads/image10/A-purple-space-4K-OLED-Desktop-Wallpaper-with-geometric-shapes-and-patterns-intersecting-a-starry-background-creating-a-modern-and-artistic-look.jpg");
    background-size: cover;
    background-position: center;
}
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}
[data-testid="stToolbar"] {
    right: 2rem;
}
</style>
'''

# Med hjälp av markdown kan vi använda css
st.markdown(page_bg_img, unsafe_allow_html=True)
st.markdown("", unsafe_allow_html=True)

# Pengar insättning
dina_pengar = 0

st.title("Här kan du välja ett namn för dig")
with st.container(border=True):   
    user_name = st.text_input("Användarnamn", max_chars=16)
