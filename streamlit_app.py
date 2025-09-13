import requests
import streamlit as st

token = st.secrets["GITHUB_TOKEN"]
repo = st.secrets["GITHUB_REPO"]

r = requests.get(f"https://api.github.com/repos/{repo}", headers={"Authorization": f"token {token}"})
st.write(r.status_code, r.json())

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
