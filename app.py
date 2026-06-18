#


import streamlit as st
from groq import Groq

# Secure Page Configuration
st.set_page_config(page_title="Emmanuel Legal Platform", page_icon="⚖️")

# Master Header
st.title("⚖️ Emmanuel Pan-African Legal Platform")
st.markdown("### Official Proprietary Intelligence Engine")
st.write("Providing secure, deep-context legal analysis and comprehensive historical research across Africa.")

st.divider()

# Security & Master Key Verification
try:
    groq_api_key = st.secrets["GROQ_API_KEY"]
    if st.secrets["ADMIN_USERNAME"] and st.secrets["ADMIN_PASSWORD"]:
        st.success("System Status: Secure Master Connection Established 🟢")
except Exception:
    st.error("System Status: Security Vault Keys Missing. Please check Streamlit Advanced Settings.")
    st.stop()

# Initializing the Neural Network
client = Groq(api_key=groq_api_key)

# The Memory Bank
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# The Chat Interface
user_query = st.chat_input("Enter your legal or historical query...")

if user_query:
    with st.chat_message("user"):
        st.markdown(user_query)
    
    st.session_state.chat_history.append({"role": "user", "content": user_query})

    with st.chat_message("assistant"):
        with st.spinner("Processing deep-context analysis..."):
            try:
                # The Upgraded Brain Rules
                messages_for_ai = [
                    {
                        "role": "system",
                        "content": "You are a highly intelligent Pan-African expert in both corporate law and history. When asked a question, provide highly detailed, comprehensive, and exhaustive answers. Tell the full, complete story. Use chapters, headings, and bullet points to structure your response. Do not summarize or give short answers. Write as much detail as possible."
                    }
                ]
                messages_for_ai.extend(st.session_state.chat_history)

                # The Upgraded Token Limit
                chat_completion = client.chat.completions.create(
                    messages=messages_for_ai,
                    model="llama-3.3-70b-versatile",
                    max_tokens=6000, # This allows for massive, book-chapter length answers
                )
                
                ai_response = chat_completion.choices[0].message.content
                st.markdown(ai_response)
                
                st.session_state.chat_history.append({"role": "assistant", "content": ai_response})
                
            except Exception as e:
                st.error(f"An error occurred during communication with the AI: {e}")
```
**Step 2:** Tap the green **Commit changes** button. 

---

### 
