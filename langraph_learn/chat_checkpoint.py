from dotenv import load_dotenv
from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.mongodb import MongoDBSaver

load_dotenv()

llm = init_chat_model(
    model="gpt-4.1-mini",
    model_provider="openai"
)


class State(TypedDict):
    messages: Annotated[list, add_messages]


def chatbot(state: State):
    response = llm.invoke(state["messages"])
    return {"messages": [response]}


graph_builder = StateGraph(State)
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)


DB_URI = "mongodb://admin:admin@localhost:27017/lg?authSource=admin"

# lifecycle management
mongo_ctx = MongoDBSaver.from_conn_string(DB_URI)
checkpointer = mongo_ctx.__enter__()

graph = graph_builder.compile(checkpointer=checkpointer)

config = {
    "configurable": {
        "thread_id": "anumifly"
    }
}

for chunk in graph.stream(
    {"messages": [" you know about ai?"]},
    config,
    stream_mode="values"
):
    chunk["messages"][-1].pretty_print()

# clean shutdown
mongo_ctx.__exit__(None, None, None)
