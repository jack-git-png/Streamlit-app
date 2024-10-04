import streamlit as st
import datetime
import boto3 

AWS_REGION = "us-east-1"
dynamodb = boto3.resource('dynamodb', region_name=AWS_REGION)
table = dynamodb.Table("inlagg")

tdy = datetime.datetime.today()

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
st.title(f"Welcome! ")

Styling = '''
<style>
[data-testid="stBaseButton-secondary"]{
    padding: 30px;
    margin-top: 30%
}
[data-testid="stVerticalBlockBorderWrapper"]{
    text-align: center;
    border-radius: 100px;
}
[data-testid="stBaseButton-headerNoPadding"]{
    
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
