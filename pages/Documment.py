import boto3.dynamodb
from boto3.dynamodb.conditions import Attr
import streamlit as st
import datetime
import boto3 
from streamlit_option_menu import option_menu

navigation_bar = option_menu(
    menu_title=None,
    icons=("house-door","gear"),
    options=["Home","Settings"],
    orientation="horizontal"
)

AWS_REGION = "us-east-1"
dynamodb = boto3.resource("dynamodb", region_name=AWS_REGION)
table = dynamodb.Table("Save")

today = datetime.datetime.today()
week_num = today.isocalendar()[1]
time_stamp = today.strftime("%Y-%m-%d %H:%M")

def data_saving(title,content,week_num,time_stamp):
    table.put_item(
        Item={
            'title': title,
            'content': content,
            'week': week_num,
            'timestamp': time_stamp
        }
    )

def get_savings_by_week(week):
   response = table.scan(
      FilterExpression=boto3.dynamodb.conditions.Attr('week').eq(week)
    )
   return response['Items']

styling = '''
<style>
.element-container:nth-of-type(2) .stTextArea {
    width: 200px !important;
        
}

[data-testid="stTextAreaRootElement"]{
    border-color: white;
    background-color: white;
}

</style>
'''
st.markdown(styling, unsafe_allow_html=True)

col1,col2 = st.columns((1,1.15))

with col1:
    title = st.text_input("Title",max_chars=30)
with col2:
    available_weeks = [str(week) for week in range(38, 50) if week != 44]
    selected_week = st.selectbox("Select the Week",available_weeks)
    items = get_savings_by_week(int(selected_week))

content = st.text_area("Documment here", height=500)

press = st.button("Save")
if press:
    if not title or not content:
        st.error('title and content are obligatory')
    else:
        data_saving(title, content, week_num, time_stamp)
        st.success('Documment has been saved!')

if not items:
   st.info(f"Inga inlägg hittades för vecka {selected_week}.")

else:
   for item in items:
    st.write(f"**Title:** {item['title']}")
    st.write(f"**Content:** {item['content']}")
    st.write(f"**Vecka:** {item['week']}")
    st.write(f"**Date:** {item['timestamp']}")
    st.write('---')
