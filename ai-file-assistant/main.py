import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Load API key
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Initialize Gemini model via LangChain
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=api_key)

# Create prompt template
template = """
You are a helpful assistant. 
Use the below context to answer the user's question.

Context:
{context}

Question:
{question}
"""

prompt = PromptTemplate(template=template, input_variables=["context", "question"])
chain = LLMChain(prompt=prompt, llm=llm)

# Load local data
with open("data.txt", "r") as f:
    data = f.read()

# User query
question = input("👤 You: ")
response = chain.run({"context": data, "question": question})

print("\n🤖 AI:", response)
