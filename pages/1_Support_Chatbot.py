import streamlit as st

st.title("Support Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Ask something")

if user_input:

    st.session_state.messages.append(
        {"role":"user","content":user_input}
    )

    with st.chat_message("user"):
        st.write(user_input)

    if "laptop" in user_input.lower():
        response = "Our laptop has 16GB RAM."

    elif "delivery" in user_input.lower():
        response = "Delivery takes 3-5 days."

    elif "refund" in user_input.lower():
        response = "Refunds take 5-7 days."

    elif "return" in user_input.lower():
        response = "Returns allowed within 30 days."

    elif "payment" in user_input.lower():
        response = "We accept UPI, Cards and Net Banking."

    elif "order status" in user_input.lower():
        response = "Please provide your order ID."

    else:
        response = "Please ask about products, delivery, refunds or orders."

    st.session_state.messages.append(
        {"role":"assistant","content":response}
    )

    with st.chat_message("assistant"):
        st.write(response)
