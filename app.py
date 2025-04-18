import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_groq import ChatGroq

# 🌿 Sanjeevini: Fast, Groq-powered Ayurveda Agent

# Groq Setup
llm = ChatGroq(
    groq_api_key="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",
    model_name="llama3-8b-8192"
)

# Prompt
template = """
You are Sanjeevini Agent, an expert in Indian medicinal plants and Ayurveda.
Answer clearly using Ayurvedic knowledge. Avoid any tech or software references.

User Question: {query}
"""
prompt = PromptTemplate(
    input_variables=["query"],
    template=template
)

chain = LLMChain(llm=llm, prompt=prompt)

# Streamlit UI
st.set_page_config("🌿 Sanjeevini Agent", layout="centered")

# Larger and cleaner custom styles
st.markdown("""
<style>
    html, body, [class*="css"]  {
        font-size: 18px !important;
    }
    .stChatMessageContent p {
        font-size: 18px !important;
    }
    .stTextInput>div>div>input {
        font-size: 18px !important;
        text-align: center;
    }
    .block-container {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
</style>
""", unsafe_allow_html=True)

st.title("🌿 Sanjeevini Agent")
st.markdown("<p style='font-size:20px;'>Ask me anything about Indian medicinal plants and Ayurveda!</p>", unsafe_allow_html=True)

# Chat input
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("💬 Ask your question")

if user_input:
    st.session_state.chat_history.append({"role": "user", "text": user_input})
    response = chain.run(query=user_input)
    st.session_state.chat_history.append({"role": "ai", "text": response})

# Display chat
for msg in st.session_state.chat_history:
    with st.chat_message("user" if msg["role"] == "user" else "assistant"):
        st.markdown(msg["text"], unsafe_allow_html=True)

# Sidebar with popular plants
with st.sidebar:
    st.header("🌱 Popular Medicinal Plants")
    popular_plants = [
        ("Tulsi", "Holy Basil"),
        ("Neem", "Azadirachta indica"),
        ("Amla", "Indian Gooseberry"),
        ("Ashwagandha", "Withania somnifera"),
        ("Brahmi", "Bacopa monnieri"),
        ("Turmeric", "Curcuma longa")
    ]
    for common, botanical in popular_plants:
        st.markdown(f"**🌿 {common}**  ", unsafe_allow_html=True)
        st.caption(f"*{botanical}*")
