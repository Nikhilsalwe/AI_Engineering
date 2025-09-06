from dotenv import load_dotenv
import os
import google.generativeai as genai
from langchain.prompts import PromptTemplate
from third_parties.linkedin import scrap_linkin_profile
# from langchain_google_genai import ChatGoogleGenerativeAI    

try:
    from langchain_google_genai import ChatGoogleGenerativeAI
except ImportError:
    print("Error: langchain-google-genai package not found.")
    print("Please install it using: pip install langchain-google-genai")
    exit(1)

# Load environment variables from .env file
load_dotenv()

if __name__ == "__main__":
    api_key = os.getenv('GOOGLE_API_KEY')
    
    if not api_key:
        print("Error: GOOGLE_API_KEY not found in environment variables")
        exit(1)
    
    # Configure the Gemini API
    genai.configure(api_key=api_key)

    print("Hello LangChain with Gemini")
    

    summary_template = """ given the linked information {information} about a person I want you to create:
    1. A short summary
    2. His brith date
    3. His full name
    4. two interesting facts about them
    5. His achievements
    """

    summay_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    # Initilize Gemini model
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",  # Use the correct model name
        temperature=0.0,  # Set temperature for deterministic output
    )

    chain = summay_prompt_template | llm
    linked_data = scrap_linkin_profile("https://www.linkedin.com/in/nikhil-salwe-526a5335/", mock=True)
    res = chain.invoke(input={"information": linked_data})

    # Create a model instance (using the correct model name)
    content = res.content
    print("Generated Summary:")
    print(content)
    # If you want to access specific parts, you can also print metadata
    # print("\n=== METADATA ===")
    # print(f"Model used: {res.response_metadata['model_name']}")
    # print(f"Total tokens: {res.usage_metadata['total_tokens']}")
    # print(f"Input tokens: {res.usage_metadata['input_tokens']}")
    # print(f"Output tokens: {res.usage_metadata['output_tokens']}")