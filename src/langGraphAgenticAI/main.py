import streamlit as st
from src.langGraphAgenticAI.ui.streamlit.loadui import LoadStreamlitUI
from src.langGraphAgenticAI.LLMS.groqllm import GroqLLM
from src.langGraphAgenticAI.graph.graph_builder import GraphBuilder
from src.langGraphAgenticAI.ui.streamlit.display_result import DisplayResultStreamlit


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
        try:
            obj_llm_config= GroqLLM(user_controls_input=user_message)
            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("Error: LLM model could not be initialized.")
                return

            usecase=user_input.get("selected_usecase")
            if not usecase:
                st.error("Error: No use case selected.")
                return

            graph_builder = GraphBuilder(model)
            try:
                graph=graph_builder.setup_graph()
                DisplayResultStreamlit(usecase,graph,user_input)
            except Exception as e:
                st.error(f"Error: Graph setup failed {e}")

        except Exception as e:
            raise ValueError(f"Error Occured with Exception :{e}")

        
