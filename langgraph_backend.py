from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage, SystemMessage
from langchain_groq import ChatGroq
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph.message import add_messages
from dotenv import load_dotenv

load_dotenv()

# LLM
llm = ChatGroq(
    model="openai/gpt-oss-120b"
)


# State
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


# Chat node
def chat_node(state: ChatState):

    messages = state["messages"]

    system_message = SystemMessage(
        content="""
You are a helpful and friendly chatbot.

Follow these rules:
- Always respond in plain text.
- Do not use LaTeX.
- Do not use \\( or \\).
- Do not use \\[ or \\].
- Do not use $$ for mathematics.
- For mathematical calculations, use normal text.
- For example, write: 30 × 13 = 390
- Do not surround mathematical expressions with special formatting.
"""
    )

    response = llm.invoke(
        [system_message] + messages
    )

    return {
        "messages": [response]
    }


# Checkpointer
checkpointer = InMemorySaver()


# Build graph
graph = StateGraph(ChatState)

graph.add_node("chat_node", chat_node)

graph.add_edge(START, "chat_node")
graph.add_edge("chat_node", END)


# Compile
chatbot = graph.compile(
    checkpointer=checkpointer
)
