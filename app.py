import streamlit as st
from datetime import datetime

# Function to get zodiac sign
def get_zodiac_sign(day, month):
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    else:
        return "Pisces"

# Function for rule-based horoscope
def generate_horoscope(name, dob, tob, place):
    day = dob.day
    month = dob.month
    zodiac = get_zodiac_sign(day, month)
    
    # Simple rules
    time_period = int(tob.split(":")[0])
    if 5 <= time_period < 12:
        time_trait = "morning-born, energetic and ambitious"
    elif 12 <= time_period < 18:
        time_trait = "afternoon-born, balanced and diplomatic"
    elif 18 <= time_period < 22:
        time_trait = "evening-born, creative and thoughtful"
    else:
        time_trait = "night-born, intuitive and deep thinker"

    return f"Hello {name}, as a {zodiac} born in {place}, you are {time_trait}. This week may bring positive changes in your personal growth and opportunities."

# Function for free text QnA
def answer_question(question, zodiac):
    question = question.lower()
    if "career" in question:
        return f"As a {zodiac}, your career path looks strong with new opportunities ahead. Focus on networking and skill development."
    elif "love" in question or "relationship" in question:
        return f"As a {zodiac}, love life may bring surprises. Stay patient and open-hearted."
    elif "health" in question:
        return f"As a {zodiac}, you need to take care of your diet and regular exercise for good health."
    else:
        return f"As a {zodiac}, trust your instincts. The universe is guiding you towards balance and success."

# Streamlit UI
st.title("🔮 AI Astrologer App")

# Collect user input
name = st.text_input("Enter your Name")
dob = st.date_input("Enter your Date of Birth", datetime(2000, 1, 1))
tob = st.text_input("Enter your Time of Birth (HH:MM in 24hr format)")
place = st.text_input("Enter your Place of Birth")

if st.button("Get Horoscope"):
    if name and tob and place:
        horoscope = generate_horoscope(name, dob, tob, place)
        zodiac = get_zodiac_sign(dob.day, dob.month)
        st.subheader("Your Horoscope:")
        st.write(horoscope)

        # Free question
        st.subheader("Ask a free question:")
        user_q = st.text_input("Type your question here")
        if user_q:
            st.write(answer_question(user_q, zodiac))
    else:
        st.warning("Please fill all details!")
