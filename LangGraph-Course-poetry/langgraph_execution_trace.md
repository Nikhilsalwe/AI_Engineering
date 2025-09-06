# LangGraph Execution Trace

Total Duration: **9.77s**

|   Step | Node            | Action                            | Duration   |
|-------:|:----------------|:----------------------------------|:-----------|
|      1 | agent_reason    | ChatGoogleGenerativeAI (LLM call) | 2.93s      |
|      2 | should_continue | Condition check                   | 0.00s      |
|      3 | act             | tavily_search (API call)          | 3.38s      |
|      4 | agent_reason    | ChatGoogleGenerativeAI (LLM call) | 1.26s      |
|      5 | should_continue | Condition check                   | 0.00s      |
|      6 | act             | triple (local tool)               | 0.00s      |
|      7 | agent_reason    | ChatGoogleGenerativeAI (LLM call) | 0.83s      |
|      8 | should_continue | Condition check                   | 0.00s      |