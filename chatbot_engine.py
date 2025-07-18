from langchain_community.embeddings import OllamaEmbeddings
import os
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_core.documents import Document
from flask import current_app
from models import Job
from langchain.chat_models import init_chat_model

load_dotenv()
if not os.environ.get("GOOGLE_API_KEY"):
    raise ValueError("GOOGLE_API_KEY not found in environment variables.")

llm = init_chat_model("gemini-2.0-flash", model_provider="google_genai")
embedding=OllamaEmbeddings(model="llama3")

def jobs_to_doc():
    jobs=Job.query.all()
    docs=[Document (page_content=f"""
Title: {job.title}
Company: {job.company_name}
Location:{job.location}
Job Type: {job.job_type}
Description: {job.description}
Skills: {job.skills}
""", metadata={"Job Id":job.id})for job in jobs]
    return docs


def get_chatbot_response(user_input):
    with current_app.app_context():
        documents = jobs_to_doc()
        vector_store = FAISS.from_documents(documents, embedding)
        retriever = vector_store.as_retriever(search_kwargs={"k": 5})
        qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever,chain_type="stuff")
        return qa_chain.run(user_input)

