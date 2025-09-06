from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_community.tools.tavily_search import TavilySearch
# from langchain_community.tools import TavilySearchResults
from langchain_tavily import TavilySearch


load_dotenv()

@tool
def triple(num: float) -> float:
    """
    param num: a number to triple
    return: the triple of the input number.
    """
    return float(num) * 3



# tools = [TavilySearchResults(max_results=3), triple]
tools = [TavilySearch(max_results=3), triple]

llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",  # Use the correct model name
        temperature=0.0,  # Set temperature for deterministic output
    ).bind_tools(tools)



