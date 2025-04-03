from langchain_openai.chat_models import ChatOpenAI
from state.state_message import ReportState, Queries
from dotenv import load_dotenv
load_dotenv()

def generate_report_sections(state: ReportState):

    topic = state.topic
    chat_model = ChatOpenAI(
        model="gpt-4.5-preview",
        temperature=0.7,
    )
    
    structured_llm = chat_model.with_structured_output(Queries)

    
