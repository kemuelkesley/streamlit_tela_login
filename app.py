# Tela de login
import streamlit as st

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


col1, col2, col3 = st.columns([1,2,1])

with col2:
    with st.form(key="login", clear_on_submit=True):
        st.markdown("## Login")
        input_email = st.text_input(label="E-mail", placeholder="email@email.com")
        input_senha = st.text_input(label="Senha", max_chars=10, placeholder="***************", type="password")
        input_button = st.form_submit_button("Entrar")
        
                
        if input_email == "kemuel@gmail.com" and input_senha == "123456":
            st.success("Logado com Sucesso")
        

