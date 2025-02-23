import streamlit as st

st.set_page_config(page_title="Venue ID", page_icon="images/icon.png", layout="wide")

with st.container():
    if st.button("Return Home", icon="🏠"):
        st.switch_page("hackathon_project.py")  # Redirects to hackathon_project

with st.container():
    st.write("---")
    st.title("About Us")

    st.write("Meet the team!")

with st.container():
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.image("images/james.jpg", width=150)
        st.write("James Butts")
        with st.expander("See More!"):
            st.write('''
                    I am an Honors Computer Science and Engineering student at The Ohio State University where I 
                     have been selected for the prestigious Integrated Business and Engineering program on the 
                     Software Innovation track (IBE-SI) as well as the Morrill Scholarship Program Excellence Scholarship. 

                    I am passionate about becoming a skilled software developer and advancing technology and society with my 
                     work and values. I am open to networking and exploring opportunities in this forever expanding discipline. 
                     Please feel free to connect with me or email me at butts.208@osu.edu.
            ''')
            st.link_button("LinkedIn", "https://www.linkedin.com/in/jpbutts/")
            

    with col2:
        st.image("images/sai.jpg", width=150)
        st.write("Avyukth Rangarajan")
        with st.expander("See More!"):
            st.write('''
            I am an undergraduate student at The Ohio State University studying computer science with a minor in business
           as part of the prestigious Integrated Business and Engineering (IBE) Honors Program. Possess strong leadership 
        and communication skills, interesting in blending software development with artificial intelligence while developing a 
        strong understanding of marketing software products in the business world.
            ''')
            st.link_button("LinkedIn", "https://www.linkedin.com/in/sai-rangarajan/")

    with col3:
        st.image("images/sky.jpg", width=150)
        st.write("Sky Sie")
        with st.expander("See More!"):
            st.write('''
                    Finance & Neuroscience major with a Computer Science Engineering minor in the Integrated Business and 
                     Engineering (IBE) Honors program on the Software Innovation(SI) track at OSU. 

                    On the IBE-SI track, I learn about the intersection of software and business through topics such 
                     as Fintech, AI, and Software Innovation with a select group of 36 students from the Fisher 
                     College of Business and the College of Engineering.
            ''')
            st.link_button("LinkedIn", "https://www.linkedin.com/in/sky-sie-49489b2a1/")

    with col4:
        st.image("images/thomas.jpg", width=150)
        st.write("Thomas Sobodosh")
        with st.expander("See More!"):
            st.write('''
            I am undergraduate student at The Ohio State University majoring in Computer Science and Engineering and planning on minoring in mathematics.
            I aspire to learn more about software engineering and artifical intelligence through projects and experience.  
            ''')
            st.link_button("LinkedIn", "https://www.linkedin.com/in/tomsobb/")

    with st.container():
        st.write("---")
        st.subheader("Our Mission: Rebuilding Social Connection Through AI-Powered Venue Discovery")
        st.write(
            "In a time where technology dictates our interactions and AI-driven digital spaces shape our daily lives,"
            " we refuse to let real-world connections fade into the background. The necessity for human connection,"
            " shared experiences, and in-person interactions has never been more critical. We exist in a time when social"
            " gatherings are becoming secondary to screens and algorithms."
            "VenueID was born out of this urgency. We have witnessed the gradual erosion of in-person interaction,"
            " exacerbated by global events like the COVID-19 pandemic, where social life became confined to video calls"
            " and online meetups. Yet, as we step into a new world, the desire for meaningful, physical gatherings has only"
            " grown stronger. We believe that AI, rather than replacing human connection, should enhance and empower it."
            "At the heart of every great event—whether it's a wedding, concert, birthday, or corporate retreat—is the"
            " perfect venue, a space where moments are shared and memories are made. Yet, the process of finding the right"
            " venue remains one of the biggest obstacles in event planning. The stress of searching for an ideal location,"
            " ensuring it fits the theme, capacity, and logistical needs, can become overwhelming. We exist to eliminate that barrier."
            "With VenueID, we harness the power of AI not to isolate but to unite—to make event planning seamless, efficient,"
            " and accessible to all. Our platform is designed to simplify the venue discovery process, ensuring that anyone,"
            " from individuals to large-scale event organizers, can effortlessly find the perfect space for their needs."
            "Our mission is more than just optimizing event logistics—it is about revitalizing human connection. We strive"
            " to be the bridge between innovation and tradition, leveraging technology to bring people together, fostering new"
            " experiences, and ensuring that no gathering is ever hindered by the challenge of securing a venue."
            "Let’s redefine the way we gather. Let’s bring the world back together—one venue at a time."
        )