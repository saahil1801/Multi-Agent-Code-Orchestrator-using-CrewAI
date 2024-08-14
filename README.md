 api_key_input = st.sidebar.text_input("Enter your GROQ API Key", type="password", label_visibility="collapsed")
    api_key = api_key_input
    if api_key.strip() == "":
        st.sidebar.warning("Please enter a valid GROQ API Key.")
        return api_key==""
    else:
        return api_key