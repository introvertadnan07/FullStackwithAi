from dotenv import load_dotenv
from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain.chat_models import init_chat_model

load_dotenv()

llm = init_chat_model(
    model="gpt-4.1-mini",
    model_provider="openai"
)


class State(TypedDict):
    messages: Annotated[list, add_messages]


def chatbot(state: State):
    response = llm.invoke(state.get("messages"))
    return {"messages": [response]}


def sample_node(state: State):
    print("\n\nInside chatbot", state)
    return {"messages": ["This is a sample node"]}


graph_buildder = StateGraph(State)


graph_buildder.add_node("chatbot", chatbot)
graph_buildder.add_node("sample_node", sample_node)

graph_buildder.add_edge(START, "chatbot")
graph_buildder.add_edge("chatbot", "sample_node")
graph_buildder.add_edge("sample_node", END)

graph = graph_buildder.compile()

updated_state = graph.invoke(
    {"messages": ["Hi", "My name is Md Adnan Qaisar"]}
)

print("\n\nupdate_state", updated_state)
