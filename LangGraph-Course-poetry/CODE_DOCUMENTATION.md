# LangGraph Course Poetry - Code Documentation

## Project Structure
```
LangGraph-Course-poetry/
├── main.py         # Main application entry point
├── nodes.py        # Node definitions and agent reasoning
├── react.py        # Tool and LLM configurations
└── README.md       # Project documentation
```

## main.py - Graph Configuration and Execution
This file sets up the ReAct agent's workflow using LangGraph.

A ReAct agent is an LLM-based agent that combines Reasoning (thought process with LLM) and Acting (calling tools/APIs) in a loop until it reaches a final answer.

Reasoning → LLM decides the next step

Acting → Executes tools (like Tavily search)

Loop continues until no more tool calls → then returns the answer


### Key Components:
1. **Imports and Environment Setup**
   ```python
   from langgraph.graph import MessagesState, StateGraph, END → Core LangGraph classes
   ```
   - Loads environment variables and required LangGraph components
   - Imports custom nodes and tools
 - 2. MessagesState

A shared state object that keeps the conversation messages across nodes (LLM outputs, tool calls).

Lets the agent "remember" context while reasoning and acting.

3. StateGraph

Defines the workflow (nodes + edges) of the agent.

Each node is either:

LLM reasoning node (agent_reason)

Tool execution node (act)

4. END

Special marker that tells LangGraph when to stop execution.

Used in should_continue conditional check.

2. **Constants Definition**
   ```python
   AGENT_REASON = "agent_reason"
   ACT = "act"
   LAST = -1
   ```
   - Defines node names and utility constants
   - Used for graph navigation and message handling

3. **Flow Control Function**
   ```python
   def should_continue(state: MessagesState) -> str
   ```
   - Determines whether to continue processing or end
   - Checks for tool calls in the last message
   - Returns either END or ACT

4. **Graph Construction**
   ```python
   flow = StateGraph(MessagesState)
   ```
   - Creates the state machine for message processing
   - Adds nodes for reasoning and tool execution
   - Configures edges for flow control

5. **Execution**
   - Compiles the graph
   - Generates a visual representation (flow.png)
   - Processes user queries and returns results

## nodes.py - Agent Reasoning and Tool Integration
This file defines the core reasoning logic and tool integration.

### Key Components:
1. **System Message**
   ```python
   SYSTEM_MESSAGE = """..."""
   ```
   - Defines the agent's behavior and capabilities
   - Provides instructions for multi-step reasoning
   - Explains available tools and their usage

2. **Agent Reasoning Function**
   ```python
   def run_agent_reasoning(state: MessagesState) -> MessagesState
   ```
   - Processes the current state
   - Invokes the LLM with system message and context
   - Returns updated message state

3. **Tool Node Configuration**
   ```python
   tool_node = ToolNode(tools)
   ```
   - Creates a node for executing tools
   - Integrates with the tools defined in react.py

## react.py - Tools and LLM Configuration
This file sets up the language model and available tools.

### Key Components:
1. **Tool Definitions**
   ```python
   @tool
   def triple(num: float) -> float
   ```
   - Defines custom tools (e.g., triple function)
   - Integrates external tools (e.g., TavilySearch)

2. **LLM Configuration**
   ```python
   llm = ChatGoogleGenerativeAI(...)
   ```
   - Configures the Gemini model
   - Sets up temperature and other parameters
   - Binds tools to the language model

### Flow Diagram
The application follows this sequence:
1. User input → AGENT_REASON
2. AGENT_REASON → should_continue
3. should_continue → ACT (if tools needed)
4. ACT → AGENT_REASON (for next step)
5. should_continue → END (if complete)

## Usage
1. **Setup**
   ```bash
   poetry install
   ```

2. **Run**
   ```bash
   poetry run python main.py
   ```

3. **Example Query**
   ```python
   "What is the temperature in Tokyo? List it and then triple it"
   ```

## Error Handling
- The system includes error handling for:
  - Missing API keys
  - Tool execution failures
  - Invalid message states

## Dependencies
- langgraph
- langchain
- google-generativeai
- python-dotenv
- requests
