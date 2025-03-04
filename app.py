import streamlit as st
import google.generativeai as genai

# 🔹 Configure Gemini API Key (Replace with your actual API key)
genai.configure(api_key="AIzaSyAgV3CEYwwRaLBuGG3qbInpsA1dB_TTZoc")

# 🔹 Initialize Gemini 2.0 Flash Model
model = genai.GenerativeModel("gemini-1.5-flash")  # Correct model for Gemini 2.0 Flash

# 🔹 System Instructions to Keep Chatbot Focused
SYSTEM_PROMPT = """
You are a chatbot that provides expert advice only on:
- Nutritious food and healthy eating habits
- Gym workouts and exercise routines
- Diet plans based on user goals (weight loss, muscle gain, general fitness)

If a user asks anything unrelated, politely steer the conversation back to health & fitness.
"""

# 🎨 Streamlit UI
st.set_page_config(page_title="Health & Fitness Chatbot", page_icon="💪")
st.title("🤖 Health & Fitness Chatbot")
st.write("Ask me anything about **nutrition, workouts, and diet plans!**")

# 🏋️‍♂️ User Goal Selection
goal = st.selectbox("🎯 Select your fitness goal:", ["General Health", "Weight Loss", "Muscle Gain", "Endurance"])

# 💾 Initialize Chat History in Session State
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# 💬 Display Chat History
for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):  
        st.markdown(chat["message"])

# 💬 User Input
user_input = st.chat_input("💡 Ask me a question about nutrition, gym, or diet:")

if user_input:
    # Display user message in chat
    st.session_state.chat_history.append({"role": "user", "message": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # 📝 Customize prompt based on user goal
    prompt = f"{SYSTEM_PROMPT}\nUser Goal: {goal}\nUser: {user_input}\nChatbot:"
    
    # 🔥 Get Response from Gemini 2.0 Flash
    response = model.generate_content(prompt)
    chatbot_reply = response.text

    # Display chatbot response in chat
    with st.chat_message("assistant"):
        st.markdown(chatbot_reply)

    # Save chatbot response to chat history
    st.session_state.chat_history.append({"role": "assistant", "message": chatbot_reply})
