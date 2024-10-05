import streamlit as st
import datetime
import boto3 

AWS_REGION = "us-east-1"
dynamodb = boto3.resource("dynamodb", region_name=AWS_REGION)
table = dynamodb.Table("Inlägg")

today = datetime.datetime.today()

def saved(name,title,content,week_num,time_stamp):
    table.put_item(
        Items={
            'name': name,
            'title': title,
            'content': content,
            'week_num': week_num,
            'time_stamp': time_stamp
        }
    )

Styling = '''
<style>
[data-testid="stAppViewContainer"] {
    background-image: url(https://i.pinimg.com/originals/a8/55/df/a855df51ab9b3b503221419fd614970f.png);
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
[data-testid="stBaseButton-secondary"] {
    padding: 30px;
    margin-top: 32%;
    height: 80px;
    border-color: white;
    background-image: url(https://e0.pxfuel.com/wallpapers/90/509/desktop-wallpaper-light-sky-stars-background-ambient-light.jpg);
    background-repeat: no-repeat;
    box-shadow: 0 8px 32px 0 rgba(0,0,0,0.37);
    align-content: center
}
[data-testid="stAppViewContainer"]::before {
    filter: blur(2px)
}
[data-testid="stVerticalBlockBorderWrapper"] {
    text-align: center;
    border-radius: 100px;
    border-color: white;
    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(1px);
    align-contents: center
    backdrop-filter: drop-shadow(0 8px 32px 0 rgba(0,0,0,0.37);)
}
[data-testid="stVerticalBlock"] {
    display: contents;
    
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
        st.switch_page("Pages/Documment.py")