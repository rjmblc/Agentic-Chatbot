import streamlit as st
from src.langGraphAgenticAI.ui.streamlit.loadui import LoadStreamlitUI


def load_langgraph_agentic_ai_app():
    """
    Loads and runs the LangGraph application with Streamlit UI.
    This function initializes the UI, handles user input, configures the LLM model,
    sets up the graph based on the selected use case, and dispalys the output while 
    implementing exception handling for robustness.
    """

    ui = LoadStreamlitUI()
    user_input=ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load user input from the UI.")
        return

    user_message = st.chat_input("Enter your message:")

    if user_message:
        pass
        # try:
        #     obj_llm_config= GroqLLM(user_controls_input=user_message)
        #     model = obj_llm_config.get_llm_model()

        #     if not model:
        #         st.error("Error: LLM model could not be initialized.")
        #         return

        #     usecase=user_input.get("selected_usecase")
        #     if not usecase:
        #         st.error("Error: No use case selected.")
        #         return
