from dotenv import load_dotenv
import os
import google.generativeai as genai
from langchain.prompts import PromptTemplate
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
    information = """
        Sachin Ramesh Tendulkar, born on April 24, 1973 in Mumbai, is widely regarded as one of the greatest cricketers in history and is often called the “God of Cricket.” A prodigy who made his international debut at just 16 against Pakistan in 1989, he went on to play for 24 years, becoming the highest run-scorer in international cricket with more than 34,000 runs and the only player to score 100 international centuries. Known as the “Little Master” and “Master Blaster,” Tendulkar achieved numerous milestones including being the first batsman to score a double century in ODIs, and he realized his lifelong dream of winning the World Cup with India in 2011. His contributions to the game earned him countless awards, including the Bharat Ratna in 2014, making him the first sportsperson to receive India’s highest civilian honor. Beyond cricket, Tendulkar has served as a Rajya Sabha member, contributed to philanthropy in children’s health, education, and sports, and remains a global icon admired for his humility, discipline, and ability to inspire generations.
    """

    summary_template = """ given the information {information} about a person I want you to create:
    1. A short summary
    2. His bristh date
    3. His full name
    4. His birthplace
    5. His achievements
    6. two interesting facts about them
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
    res = chain.invoke(input={"information": information})

    # Create a model instance (using the correct model name)
    content = res.content
    print("Generated Summary:")
    print(content)
    # If you want to access specific parts, you can also print metadata
    print("\n=== METADATA ===")
    print(f"Model used: {res.response_metadata['model_name']}")
    print(f"Total tokens: {res.usage_metadata['total_tokens']}")
    print(f"Input tokens: {res.usage_metadata['input_tokens']}")
    print(f"Output tokens: {res.usage_metadata['output_tokens']}")