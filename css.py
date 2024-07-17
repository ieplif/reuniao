import streamlit as st

def add_custom_css():
    st.markdown(
        """
        <style>
        .main {
            background-color: #f0f2f6;
            padding: 0 2rem;  /* Ajusta a margem lateral da área principal */
        }
        .sidebar .sidebar-content {
            background-color: #4B8BBE;
            color: white;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #1a73e8;
            font-size: 50px; /* Tamanho da fonte para headers */
        }
        .stText, .stMarkdown {
            font-size: 52px; /* Tamanho da fonte para texto e markdown */
        }
        
        .stButton>button {
            font-size: 40px; /* Tamanho da fonte para botões */
        }
        </style>
        """,
        unsafe_allow_html=True
    )
