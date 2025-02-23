import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Venue ID", page_icon="images/icon.png", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_music = load_lottieurl("https://lottie.host/91c50720-5926-45a5-886f-363ac30f5cb1/pD6AhqN0vB.json")


with st.container():

    if st.button("Return Home", icon="🏠"):
        st.switch_page("hackathon_project.py")  # Redirects to hackathon_project


with st.container():
    st.write("---")

with st.container():
    left_column, right_column = st.columns(2)

    with left_column:
        st.subheader("What We See in Our Future:")
        st.write("""In the future, for businesses and touring artists, VenueID could integrate real-time 
                 audience analytics, ticket sales insights, and travel logistics optimization to create a 
                 smart event ecosystem. AI-powered demand heatmaps, sentiment analysis, and predictive 
                 booking models will allow event organizers to maximize attendance while reducing costs.
                  We also envision AR & VR venue walkthroughs, allowing users to explore spaces before booking.
                  Additionally, an AI-powered chat planner could generate complete event plans, auto-negotiating
                  contracts, setting up vendor partnerships, and providing real-time cost-saving recommendations. 
                 Further expansion could include automated booking and outreach tools, allowing event organizers
                  to instantly contact venues via AI-generated email templates, as well as dynamic weather
                  considerations for outdoor events like weddings and festivals. VenueID could also feature 
                 crowd flow predictions, sustainability rankings, and map integrations that allow users to
                  zoom in on venue locations and view accessibility options. Ultimately, VenueID has the 
                 potential to become a one-stop AI-driven event planning hub, offering instant venue bookings,
                  smart logistics, and interactive recommendations, making venue selection seamless, efficient,
                  and highly customized""")
    with right_column:
        st_lottie(lottie_music, height=300, key="music")
