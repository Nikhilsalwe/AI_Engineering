from dotenv import load_dotenv
from langgraph.graph import MessagesState
from langgraph.prebuilt import ToolNode

from react import llm, tools

load_dotenv()

SYSTEM_MESSAGE = """You are a helpful assistant that can use tools to answer questions.
Always use the available tools when needed. If a question involves multiple steps:
1. Break down the steps
2. Use tools for each step
3. Combine the results

For calculations:
1. First get the data using search tools
2. Then use the calculation tools on the results
3. Show your work clearly

Remember:
- You have access to a search tool for current information
- You can use the triple tool for multiplication by 3
- Always show your reasoning
"""

def run_agent_reasoning(state: MessagesState) -> MessagesState:
    """
    Run the agent reasoning node.
    """
    response = llm.invoke([{"role": "system", "content": SYSTEM_MESSAGE}, *state["messages"]])
    return {"messages": [response]}

tool_node = ToolNode(tools)