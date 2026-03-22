import streamlit as st
import random

# 1. Page Config
st.set_page_config(page_title="For Fatima Zahra 🌸", page_icon="✨", layout="wide")

# 2. THE ULTIMATE DESIGN
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@300;400;600&display=swap');

    /* Animated Background */
    .stApp {
        background: linear-gradient(-45deg, #ff9a9e, #fad0c4, #ffd1ff, #a1887f);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
    }
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Glass Card */
    .main .block-container {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(12px);
        border-radius: 40px;
        border: 1px solid rgba(255, 255, 255, 0.4);
        padding: 50px 60px 80px 60px !important;
        max-width: 600px;
        margin: auto;
        margin-top: 5vh;
        text-align: center;
        box-shadow: 0 15px 35px rgba(0,0,0,0.1);
        animation: float 6s ease-in-out infinite;
    }

    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-15px); }
    }

    /* TYPOGRAPHY */
    .hb-text {
        font-family: 'Poppins', sans-serif;
        font-size: 1.1rem !important;
        letter-spacing: 4px;
        color: #ff4d6d !important;
        font-weight: 600;
        margin-bottom: -10px;
    }

    .glow-name {
        font-family: 'Dancing Script', cursive;
        color: #c9184a !important;
        font-size: 4.5rem !important;
        margin-top: 0px;
    }

    h3, p, span, b, div {
        color: #4a4a4a !important;
        font-family: 'Poppins', sans-serif;
    }

    /* Message Boxes */
    .phrase-box {
        background: rgba(255, 255, 255, 0.5);
        border: 2px solid #ff4d6d;
        border-radius: 15px;
        padding: 15px;
        margin: 20px 0;
        color: #c9184a !important;
        font-weight: 600;
        animation: fadeIn 0.5s ease-in;
    }
    @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

    /* Centering Hack */
    div.stButton {
        text-align: center;
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 100%;
    }

    .stButton>button {
        background: #ff4d6d;
        color: white !important;
        border-radius: 50px;
        padding: 12px 60px;
        border: none;
        font-weight: 600;
        font-size: 1.1rem;
        transition: 0.3s all ease;
    }
    .stButton>button:hover {
        transform: scale(1.1);
        box-shadow: 0 10px 25px rgba(255, 77, 109, 0.5);
    }

    .tag-container {
        display: flex; justify-content: center; gap: 10px; margin-top: 15px;
    }
    .tag {
        background: rgba(255, 77, 109, 0.15); 
        padding: 6px 15px; 
        border-radius: 20px; 
        font-size: 0.85rem; 
        font-weight: 600; 
        color: #c9184a !important;
    }

    .letter-box {
        background: rgba(255,255,255,0.4); 
        padding: 30px; 
        border-radius: 25px; 
        margin-top: 40px; 
        margin-bottom: 30px; 
        border-left: 6px solid #ff4d6d; 
        text-align: left;
    }

    /* Styling for the Expander (Vault) */
    .streamlit-expanderHeader {
        background-color: transparent !important;
        border-radius: 15px !important;
        color: #ff4d6d !important;
        font-weight: 600 !important;
    }

    header, footer, #MainMenu {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# 3. LOGIC
if 'unlocked' not in st.session_state:
    st.session_state.unlocked = False

if not st.session_state.unlocked:
    st.markdown("<h1 class='glow-name' style='font-size: 3.5rem !important;'>For your eyes only <3.</h1>", unsafe_allow_html=True)
    pw = st.text_input("Enter the magic word:", type="password")
    
    if st.button("Open with Love ✨"):
        if pw.lower() == "october":
            st.session_state.unlocked = True
            st.rerun()
        else:
            st.error("Access denied. Try 'october'! 💕")
else:
    st.balloons()
    st.markdown("<p class='hb-text'>HAPPY BIRTHDAY ✨</p>", unsafe_allow_html=True)
    st.markdown("<h1 class='glow-name'>Fatima Zahra 💕</h1>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class="tag-container">
            <span class="tag">#the sweetest 🍯</span>
            <span class="tag">#the kindest 🤍</span>
            <span class="tag">#the zin dyalna 😼</span>
        </div>
    """, unsafe_allow_html=True)

    # Music Section
    st.markdown('<div style="background: rgba(255,255,255,0.3); border-radius: 20px; padding: 15px; margin: 30px 0; border: 1px solid rgba(255, 77, 109, 0.2);">', unsafe_allow_html=True)
    st.markdown("<p style='font-weight: 600; font-size: 0.9rem;'>🎵 Play me:</p>", unsafe_allow_html=True)
    try:
        with open('pardon.mp3', 'rb') as f:
            st.audio(f.read())
    except:
        st.write("*(File 'pardon.mp3' not found)*")
    st.markdown('</div>', unsafe_allow_html=True)

    # THE LETTER
    st.markdown("""
        <div class="letter-box">
            <p style="font-style: italic; font-size: 1.1rem; line-height: 1.8;">
                "To <b>Fatima Zahra</b>, Happy Birthday to the girl with the kindest heart.
                 May your day be filled with your favorite songs and surrounded by people who appreciate you as much as I do.
                 You’re truly one of a kind.
                 Here’s to a brilliant year ahead! ^^"
            </p>
            <p style="text-align: right; font-weight: bold; color: #ff4d6d !important; margin-top: 15px;">— Reda :3</p>
        </div>
    """, unsafe_allow_html=True)

    # Surprise Button Section
    phrases = [
        "You're the brightest star in the room! ✨",
        "The world is luckier because you're in it. 🌍",
        "Wishing you a day as sweet as you are! 🍯",
        "Keep shining, azin! 💖",
        "You're truly the 'Zina' forever! 😼",
        "I hope your day is full of Spanish sunshine and K-Pop beats! 💃"
    ]
    
    if st.button("Click for a Surprise ✨"):
        random_msg = random.choice(phrases)
        st.markdown(f'<div class="phrase-box">{random_msg}</div>', unsafe_allow_html=True)

    # --- VAULT AT THE VERY BOTTOM WITH ARROW ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    with st.expander("hmm..👀"):
        st.markdown("<p style='font-size: 0.8rem; opacity: 0.7;'> you can ignore this one, but if you insist..</p>", unsafe_allow_html=True)
        vault_code = st.text_input("Enter the secret code:", type="password", key="vault_key")
        
        if vault_code.lower() == "awdi":
            st.markdown("""
                <div class="phrase-box" style="border: 2px solid #ff4d6d; background: rgba(255, 255, 255, 0.6); text-align: left;">
                     <b>A Memory Restored:</b><br><br>
                    <i>"That night, what I feared most since the beginning finally happened. 
                    Looking back now at the time we spent together,
                    and despite everything that went down, I just wanted to say that I hold no grudges, even tho i miss us, Those days were an important lesson for me or even both of us. Now, after all these years,
                    I sincerely wish you all the best in your life."</i> 🤍
                </div>
            """, unsafe_allow_html=True)