import boto3.dynamodb
import streamlit as st
import datetime
import boto3 
from streamlit_option_menu import option_menu
from boto3.dynamodb.conditions import Attr

styling = '''
<style>
[data-testid="stTextInputRootElement"]{
    border-color: white;
}
[data-testid="stSelectbox"]{
    border-color: white;
}

</style>
'''
st.markdown(styling,unsafe_allow_html=True)

navigation_bar = option_menu(
    menu_title=None,
    icons=("house-door","gear"),
    options=["Home","Settings"],
    orientation="horizontal",
    styles={
        "container": {},
        "nav-link": {},
        "nav-link-selected": {"background-color": "lightblue"},
    }
)

# Sets up the region and the Table
AWS_REGION = "us-east-1"
dynamodb = boto3.resource("dynamodb", region_name=AWS_REGION)
table = dynamodb.Table("Save")

# all needed items will be taken from these
today = datetime.datetime.today()
week_num = today.isocalendar()[1]
time_stamp = today.strftime("%Y-%m-%d %H:%M")

# Will allow us to store data so we can use it
def data_saving(content,title,week_num,time_stamp):
    table.put_item(
        Item={
            'content': content,
            'title': title,
            'week': week_num,
            'timestamp': time_stamp
        }
    )
# Will save it according to the current week
def get_savings_by_week(week):
    try:
        response = table.scan(
            FilterExpression=Attr('week').eq(week)
        )
        return response['Items']
    except Exception as e:
        st.error(f"Error scanning table: {e}")
        return []

# Basic streamlit colums for sizes, widths etc
col1,col2 = st.columns((1,1.15))
with col1:
    title = st.text_input("Title",max_chars=30, key="title")
with col2:
    available_weeks = [str(week) for week in range(38, 50) if week != 44] # Selection from 38 to 50
    selected_week = st.selectbox("Select the Week",available_weeks,key="week") # The selectbox 
    items = get_savings_by_week(int(selected_week)) # usage of the previous function

# Content & Button
content = st.text_area("Document here", height=300, key="docs") # Where text wil be written
save_button = st.button("Save",key="saving") # So data can be saved if pressed

if save_button:
    if not title or not content: # Will not be pressed if there is no title or content
        st.error('title and content are obligatory')
    else:
        data_saving(content,title,week_num,time_stamp) # Saves the data otherwise if there is
        st.success('Document has been saved!')

if not items:
   st.info(f"No saved documents found for this week.") # will show if it exists in the data or not for the specific week

else: # Then here is what it would show when we save
   with st.container(border=True,height=200):
    for item in items:
        st.write(f"**Title:** {item['title']}")
        st.write(f"**Content:** {item['content']}")
        st.write(f"**Week:** {item['week']}")
        st.write(f"**Date:** {item['timestamp']}")
        st.write('---')
