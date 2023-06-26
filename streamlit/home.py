import streamlit as st

if __name__=="__main__":
    # Add CSS styling for background image
    st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("https://github.com/Hmittal15/NewYork-taxi-fare-prediction/assets/108916132/a929dbe4-597d-474b-87c7-7758d1e12044");
                background-attachment: fixed;
                background-size: cover
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    st.title("MedIQ ChatBot")
    st.subheader("Your Virtual Doctor's Appointment")

    # Introduction and description
    st.markdown(
        """
        Welcome to the MedIQ ChatBot interface, a smart and intuitive platform designed to provide you with medical information and assistance in a convenient and personalized manner. MedIQ chatbot leverages advanced natural language processing and deep learning techniques to simulate a virtual doctor's appointment, addressing your medical queries and concerns.
        """
    )

    st.markdown("## Key Features:")
    st.markdown("- **Intelligent Medical Advice**: Our ChatBot is equipped with extensive medical knowledge and the ability to interpret your input, offering insightful advice and possible diagnoses based on your symptoms.")
    st.markdown("- **Enhanced User Experience**: Enjoy a user-friendly interface that emulates a virtual doctor's consultation. The chat history is preserved during current session, allowing for a secure and seamless flow of information during your medical journey.")
    st.markdown("- **Flexibility and Customization**: The ChatBot is built with flexibility in mind, accommodating various medical scenarios and allowing for customization to cater to specific medical specialties.")

    st.markdown("## Advantages:")
    st.markdown("- **Immediate Medical Support**: MedIQ ChatBot offers instant access to medical information and guidance, providing timely support when you need it the most.")
    st.markdown("- **24/7 Availability**: Access the ChatBot anytime, anywhere, ensuring round-the-clock medical assistance and information, regardless of time zones or geographical location.")
    st.markdown("- **Educational Resource**: Engaging with the MedIQ ChatBot not only offers immediate assistance but also serves as an educational resource, enhancing your medical knowledge and promoting self-care.")
    st.markdown("- **Privacy and Confidentiality**: Rest assured that your medical queries and personal information are treated with the utmost privacy and confidentiality, adhering to stringent data protection standards.")

    st.session_state["chat_messages"] = []