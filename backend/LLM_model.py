# 6 LLM import
from langchain_cohere import ChatCohere
from dotenv import load_dotenv
import os
load_dotenv
COHERE_API_KEY = os.getenv("COHERE_API_KEY")


llm = ChatCohere(
    cohere_api_key=COHERE_API_KEY,
    model="command-a-03-2025"

)
def ask_questions(question, retriever):
    # Search relevant documents
    docs = retriever.invoke(question)

    # Create context
    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    # Prompt
    prompt = f"""
Answer the question using only the given context.

Context:
{context}

Question:
{question}
"""

    # Generate answer
    response = llm.invoke(prompt)

    return response.content







