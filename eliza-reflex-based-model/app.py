import streamlit as st
import re
import random as rd

# Page Configuration
st.set_page_config(
    page_title="Dr. Eliza",
    page_icon="🩺"
)

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
    }
    
    h1 {
        color: #0f172a;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        font-weight: 700;
        font-size: 1.8rem;
        letter-spacing: -0.025em;
    }
    p.subtitle {
        color: #475569;
        font-size: 0.95rem;
        margin-bottom: 2rem;
        font-weight: 400;
    }

    [data-testid="stChatMessageAvatar"] {
        width: 32px !important;
        height: 32px !important;
        border-radius: 50% !important;
        background-color: #e2e8f0 !important;
    }
    [data-testid="stChatMessageAvatar"] img, 
    [data-testid="stChatMessageAvatar"] svg {
        width: 16px !important;
        height: 16px !important;
    }

    [data-testid="stChatMessage"] {
        padding: 1rem 1.25rem;
        border-radius: 16px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.02), 0 2px 4px -1px rgba(0, 0, 0, 0.01);
        margin-bottom: 0.85rem;
        border: 1px solid rgba(226, 232, 240, 0.8);
        background-color: #ffffff;
    }

    [data-testid="stChatInput"] textarea {
        border-radius: 12px !important;
        border-color: #cbd5e1 !important;
    }
    [data-testid="stChatInput"] textarea:focus {
        border-color: #3b82f6 !important;
        box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.15) !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🩺 Dr. Eliza")
st.markdown('<p class="subtitle"><b>A rule-based reflex model (ref. Co-authored by LLAMA 4)</b></p>', unsafe_allow_html=True)

custom_rules = {
    r"i feel (.*)": [
        "Why do you think you feel {0}?",
        "How long have you been feeling {0}?",
        "Does feeling {0} affect your daily routine?"
    ],
    r"i am (.*)": [
        "What makes you say you are {0}?",
        "How does being {0} impact your well-being?",
        "Have you been {0} for a long time?"
    ],
    r"headache|pain|hurt|ache": [
        "Where is the discomfort located specifically?",
        "On a scale of 1 to 10, how severe is the pain?",
        "Have you tried resting or taking medication for that?"
    ],
    r"sleep|tired|exhausted|fatigue": [
        "Rest is crucial. Roughly how many hours of sleep are you getting per night?",
        "Does your fatigue interfere with your concentration during the day?"
    ],
    r"diet|food|eat|stomach": [
        "What have you eaten recently? Diet plays a big role in how we feel.",
        "Are you experiencing any other digestive discomfort?"
    ],
    r"hello|hi|greetings": [
        "Hello. I am Dr. Eliza. What health or wellness topic is on your mind today?",
        "Hi there. How are you feeling physically and mentally today?"
    ],
    r"bye|exit|quit": [
        "Take care of yourself. Goodbye!"
    ]
}

def get_response(user_input):
    for pattern, responses in custom_rules.items():
        match = re.search(pattern, user_input, re.IGNORECASE)
        if match:
            chosen_response = rd.choice(responses)
            if match.groups():
                return chosen_response.format(match.group(1))
            return chosen_response

    fallbacks = [
        "That is interesting. Can you tell me more about your symptoms or thoughts?",
        "I am a simple reflex assistant and want to make sure I understand. Can you rephrase that?",
        "How does that relate to your overall health today?"
    ]
    return rd.choice(fallbacks)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello. I am Dr. Eliza. How are you feeling today?"}
    ]

for message in st.session_state.messages:
    avatar_icon = "🩺" if message["role"] == "assistant" else "👤"
    with st.chat_message(message["role"], avatar=avatar_icon):
        st.markdown(message["content"])

if user_input := st.chat_input("Describe how you are feeling..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user", avatar="👤"):
        st.markdown(user_input)

    # Generate response using fixed logic
    bot_response = get_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    with st.chat_message("assistant", avatar="🩺"):
        st.markdown(bot_response)