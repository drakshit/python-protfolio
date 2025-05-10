import streamlit as st
import pandas

def show_content(row_data):
    st.header(row_data['title'])
    st.write(row_data['description'])
    st.image(f"images/{row_data['image']}")
    st.write(f"[Source Code]({row_data['url']})")


st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.jpg', width=400)
with col2:
    st.title("About Debasish!")
    about_me = """
        Dynamic Full-Stack Developer with 16 years of experience delivering innovative web
        solutions and significantly enhancing user engagement. Expertise encompasses both
        front-end and back-end technologies, with a strong focus on React JS, Next JS,
        and Node JS, facilitating the creation of scalable and high-performance applications.
        Proficiency in Agile methodologies and CI/CD practices ensures timely project delivery
        and efficient processes. Strong analytical skills combined with a passion for leveraging
        cloud technologies contribute to the development of robust and maintainable systems.
        Committed to continuous improvement and fostering collaboration within diverse team
        environments.
    """
    st.info(about_me)
note = """
Below you'll find some apps which I have built in Python, feel free to connect me!
"""
st.write(note)

col3, empty_col, col4 = st.columns([1.5,0.5,1.5])
df = pandas.read_csv("data.csv", sep=';')

for index, row in df.iterrows():
    match index % 2:
        case 0:
            with col3:
                show_content(row)

        case _:
            with col4:
                show_content(row)
