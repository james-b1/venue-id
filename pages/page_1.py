import streamlit as st
import google.generativeai as genai

# Load API key from secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash",
  generation_config=generation_config,
  system_instruction="""You will be given a venue type from the following list: 
                    artist venues, party venues, wedding venues, sports tournament, 
                    esports tournament, theater show, product expo, political rally, 
                    and hackathon. You will be given the country, state, and city. 
                    If the selected venue type is an artist venue, then you will receive 
                    the artist's monthly Spotify listener count instead of the expected audience. Based
                    on the monthly listener count, estimate the expected audience amount. Specify that you 
                    estimated the expected audience amount based on the listener count. Otherwise, you will 
                    receive the expected audience amount. Also describe how this expected audience value was predicted 
                    based on the Spotify monthly listeners.
                    You will be given the time of the 
                    event in Eastern Standard Time. Based on this information, locate the best 3 specific venues that 
                    would accommodate the specified event type with 
                    the expected audience amount. Make sure you consider the hours of operation and holidays. If the location is 
                    unavailable, please provide an explanation why under an additional 'Note:' heading in the provided format.
                    
                    Provide each of the venues in the following format with each heading bolded, and give a short description of the venue before: 
                    Venue:

                    Address: 

                    Why this venue? 

                    Capacity: 

                    Location: 

                    Features: 

                    Url To Website: 

                    Time & Date:
                    
                    """,
)

chat_session = model.start_chat(
  history=[]
)

# Configure Page
st.set_page_config(page_title="Venue ID", page_icon="images/icon.png", layout="wide")


with st.container():
    if st.button("Return Home", icon="🏠"):
        st.switch_page("hackathon_project.py")  # Redirects to hackathon_project

with st.container():

    st.write("---")
    # Style text with CSS
    st.markdown("""
        <style>
        .big-font {
        font-size:60px !important;
        font-weight: bold;
        text-align: center;
        }
        </style>
        """, unsafe_allow_html=True)
    st.markdown('<p class="big-font">Select Your Preferences</p>', unsafe_allow_html=True)
    st.write("##")
    
    first_col, second_col, third_col = st.columns(3)

    with first_col:
        # Create Venue Selection
        userVenue = st.radio(
            "Select Venue Type",
            key="ven_type",
            options=["Artist Venue", "Party Venue", "Wedding Venue", "Sports Tournament", "Esports Tournament", "Theater Show", "Product Expo", 
                     "Political Rally", "Hackathon"],
        )

    with second_col:
        # Get Country, State, and City input
        userCountry = st.text_input("Country", placeholder="Enter")
        userState = st.text_input("State", placeholder="Enter")
        userCity = st.text_input("City", placeholder="Enter")

    with third_col:
        # Get Date and time input
        userDate = st.date_input('Date')
        userTime = st.text_input("Time (EST)", placeholder="Enter")         
        
        # Change information needed to Spotify monthly listeners if Artist Venue is selected
        if not userVenue == "Artist Venue" :
            userAud = st.text_input("Expected Audience", placeholder="Enter")
        else:
            userAud = st.text_input("Spotify Monthly Listeners", placeholder="Enter")
            
        

    if st.button("Generate Now", use_container_width=True):
        # Ensure variables are properly formatted
        response_text = (
            f"Venue Type: {userVenue}; "
            f"Country: {userCountry}; "
            f"State: {userState}; "
            f"City: {userCity}; "
            f"Date: {userDate}; "
            f"Time: {userTime}; "
            f"Expected Audience OR Spotify Monthly Listeners: {userAud};" 
        )
        
        # Ensure chat_session is correctly defined
        if "chat_session" in locals() or "chat_session" in globals():
            # Get response from AI
            response = chat_session.send_message(response_text)
            st.write(response.text)
        else:
            st.write("Error: chat_session is not defined. Please check your setup.")


    
