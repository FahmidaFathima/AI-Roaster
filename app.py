import streamlit as st
import random
from roast_engine import smart_sentiment_roast
from compliment_engine import sweet_sentiment_compliment
from textblob import TextBlob
from gtts import gTTS
import os
from datetime import datetime

# 🔥 Roast & Compliment History Setup
if "roast_history" not in st.session_state:
    st.session_state.roast_history = []
if "last_roast" not in st.session_state:
    st.session_state.last_roast = ""
if "mode" not in st.session_state:
    st.session_state.mode = "Roast"

# 🌈 Page Configuration
st.set_page_config(page_title="Roastify Me", page_icon="🔥", layout="wide")

# 🎨 Custom Styling (Light SNOW / Peach background)
st.markdown("""
    <style>
    .stApp {
        background-color: #FFF5EE; /* Peach / Snow tone */
    }
    .stButton>button {
        color: black;
        background-color: #ff4b4b;
        border-radius: 12px;
        padding: 0.75em 2em;
        font-weight: bold;
    }
    .stTextInput>div>div>input {
        border: 2px solid #f58b54;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# 🎛️ Sidebar
with st.sidebar:
    st.header("✨ Roastify Me Settings")
    st.markdown("""
    Welcome to **Roastify Me** 💣 – where sass meets sweet.

    🔥 **Choose your vibe:** Decide if you want a fierce roast or a sugar-coated compliment.  
    🎙️ **Get it read out loud:** Turn your sass into sound with our built-in voice playback.  
    🪞 **Try Mirror Mode:** Flip your own words back at you for a playful burn.  
    🎲 **Random Surprise:** Can't decide? Let fate roast or compliment you.  

    ### ✨ New Features Just for You:
    - More GIF reactions for epic burns & warm fuzzies  
    - Lighter, eye-friendly theme for a smoother experience  
    - Extended roast/compliment logic for sharper wit & sweeter praise  
    - Optimized voice playback for crisp delivery  
    - Roasts powered by AI that know exactly when to be savage or sweet  

    ⚠️ **Warning:** May cause uncontrollable laughter or minor ego bruises. Use responsibly.
    """)
    st.markdown("---")
    st.info("Made with ❤️ by Fahmida Fathima the Savage fierce 👸")

# 🧠 Main Title
st.title("💣 Roastify Me")
st.subheader("Let the sass fly, or flip the switch for sweetness 😘")

# 📊 Mood Slider
with st.container():
    st.markdown("### 🌈 Mood-o-Meter")
    mood_slider = st.slider("How's your mood today?", -1.0, 1.0, 0.0)
    st.caption("⬅️ Grumpy | Neutral 😶 | Happy ➡️")

# 🧃 Mode Selection
st.session_state.mode = st.radio("Choose your vibe:", ["Roast", "Compliment"], horizontal=True)

# 🪞 Mirror Mode Toggle
mirror_mode = st.checkbox("🪞 Mirror Mode (Roast using your words)")

# 💬 User Input
user_input = st.text_input("💬 Spill the tea:", placeholder="Type your sass bait here...")

# 🧠 Response Generator
def get_response(text, mood, mode, mirror):
    if mirror and text:
        return f"You said: *{text}*... and still thought you’d escape a roast? 😏"
    if mode == "Compliment":
        return sweet_sentiment_compliment(text)
    else:
        return smart_sentiment_roast(text, override_sentiment=mood)

# 🔘 Buttons
col1, col2 = st.columns([1, 1])
roast_btn = col1.button("🔥 Roast Me!" if st.session_state.mode == "Roast" else "💖 Compliment Me!")
random_btn = col2.button("🎲 Random Surprise!")

# 📄 Roast Logger
def log_interaction(user_input, roast_text):
    with open("roast_log.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} | {st.session_state.mode} | Input: {user_input} | Output: {roast_text}\n")

# 🎤 Voice Output
def play_tts(text):
    tts = gTTS(text=text, lang="en")
    tts.save("voice.mp3")
    st.audio("voice.mp3", format="audio/mp3")

# 🌟 GIF Reactions
gif_links = [
    "https://media.giphy.com/media/3o7qDPxorBbvpBtvOU/giphy.gif",
    "https://media.giphy.com/media/l1J9w53vToII2A8Os/giphy.gif",
    "https://media.giphy.com/media/3o6gE5aYQo7zSsmZ4k/giphy.gif",
    "https://media.giphy.com/media/YTbZzCkRQCEJa/giphy.gif",
    "https://media.giphy.com/media/l4FGuhL4U2WyjdkaY/giphy.gif",
    "https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif",
    "https://media.giphy.com/media/3o6Mbf8vTw3cE2zw9G/giphy.gif",
    "https://media.giphy.com/media/xT9IgzoKnwFNmISR8I/giphy.gif",
    "https://media.giphy.com/media/3ohs4BSacFKI7A717y/giphy.gif",
    "https://media.giphy.com/media/l1J9EdzfOSgfyueLm/giphy.gif",
    "https://media.giphy.com/media/3oriNVVnN4j3Z3I4cw/giphy.gif",
    "https://media.giphy.com/media/xUOwGcvNiu6UOA8lBS/giphy.gif",
    "https://media.giphy.com/media/ZCSPU93A6lZ0w/giphy.gif",
    "https://media.giphy.com/media/3o6gE5aXGl7tpr3VFe/giphy.gif",
    "https://media.giphy.com/media/3oz8xAFtqoOUUrsh7W/giphy.gif",
    "https://media.giphy.com/media/26xBKqeFFzLhK5Y6c/giphy.gif",
    "https://media.giphy.com/media/l1J9w27I6CJKH1lQY/giphy.gif",
    "https://media.giphy.com/media/xUPGcgtKxm4PADy3Ck/giphy.gif",
    "https://media.giphy.com/media/3oz8xKaR836UJOYeOc/giphy.gif",
    "https://media.giphy.com/media/l3q2K5jinAlChoCLS/giphy.gif",
    "https://media.giphy.com/media/3o7TKtnuHOHHUjR38Y/giphy.gif",
    "https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif",
    "https://media.giphy.com/media/3oz8xLd9DJq2l2VFtu/giphy.gif",
    "https://media.giphy.com/media/3o6Zt481isNVuQI1l6/giphy.gif",
    "https://media.giphy.com/media/jUwpNzg9IcyrK/giphy.gif",
    "https://media.giphy.com/media/Q7ozWVYCR0nyW2rv5u/giphy.gif",
    "https://media.giphy.com/media/3o7abldj0b3rxrZUxW/giphy.gif",
    "https://media.giphy.com/media/f9k1tV7HyORcngKF8v/giphy.gif",
    "https://media.giphy.com/media/TdfyKrN7HGTIY/giphy.gif",
    "https://media.giphy.com/media/xT1R9ZgHSYAlDNgHLa/giphy.gif",
    "https://media.giphy.com/media/fWg6nqV7aR7y3Z4Fwj/giphy.gif",
    "https://media.giphy.com/media/12XDYvMJNcmLgQ/giphy.gif",
    "https://media.giphy.com/media/xT0xeuOy2Fcl9vDGiA/giphy.gif",
    "https://media.giphy.com/media/MFdlhTghIfddO/giphy.gif"
]

# 🚀 Response Logic
if roast_btn or random_btn:
    if random_btn:
        user_input = random.choice(["I’m coding", "Why is AI so weird", "Feeling meh", "Surprise me!"])
    if user_input.strip():
        roast_text = get_response(user_input, mood_slider, st.session_state.mode, mirror_mode)
        st.session_state.last_roast = roast_text
        st.session_state.roast_history.append(roast_text)

        # 💾 Save to Log
        log_interaction(user_input, roast_text)

        # 🔊 TTS
        play_tts(roast_text)

        # 💥 Show Roast Card
        st.markdown(f"""
       <div style='background-color:#fff5f5;padding:20px;border-radius:10px;border:2px solid #ff6666;margin-bottom:10px'>
    <h4 style='color:#d6336c;text-align:center;'>💥 Your Roast:</h4>
    <p style='font-size:18px;text-align:center; color:#000000'><strong>{roast_text}</strong></p>
</div>
        """, unsafe_allow_html=True)

        # 😈 Random GIF Reaction
        gif = random.choice(gif_links)
        st.image(gif, use_container_width=True)
    else:
        st.warning("Don't be shy, give me *something* to roast, sugar 💅")

# 🕘 Roast History
if st.session_state.roast_history:
    st.markdown("---")
    st.subheader("📜 Your Sass & Compliment History")
    for i, r in enumerate(reversed(st.session_state.roast_history), 1):
        st.markdown(f"{i}. {r}")

# 👣 Footer
st.markdown("---")
st.caption("Made with fire & love 🔥💖 by Fahmida")
