import streamlit as st
from backend.upload import load_document
from backend.splitter import split_documents
from backend.embedding import get_embeddings
from backend.LLM_model import ask_questions


st.set_page_config(
    page_title="AskMyDocs",
    page_icon="📄",
    layout="wide"
)
def load_css():
    with open("Logo/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()
col1, col2, col3 = st.columns([2,1,2])

with col2:
    st.image("Logo/logolight.png", width=220)
# Title
st.markdown(
    """
    <h1 class="title">📄 AskMyDocs With AI</h1>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <p class="subtitle">
    Upload a document and prepare it for question answering.
    </p>
    """,
    unsafe_allow_html=True,
)

st.markdown("<br>", unsafe_allow_html=True)


# Upload file
documents = st.file_uploader(
    "Choose a file",
    type=["pdf", "txt", "docx", "csv"]
)

if documents is not None:
    # Load document
    with st.spinner("Loading document..."):
        documents = load_document(documents)

    st.success("Document Loaded Successfully!")

    st.write(f"Number of Pages: {len(documents)}")
    # Split document
    with st.spinner("Splitting document..."):
        chunks = split_documents(documents)

    st.success(f"Chunks Created: {len(chunks)}")

    st.subheader("Preview")

    st.write(chunks[0].page_content[:1000])
    # Load embeddings
    embeddings = get_embeddings()


    # Create FAISS Vector Database
    from langchain_community.vectorstores import FAISS
    vector_db = FAISS.from_documents(
    chunks,
    embeddings
)

   # Create Retriever
    retriever = vector_db.as_retriever(
        search_kwargs={"k": 2}
)

    st.success("Retriever Created Successfully!")
     
    
    st.divider()

    question = st.text_input("Ask your question")
    
    if st.button("Ask"):

        if question:

            with st.spinner("Generating Answer..."):
                
                answer = ask_questions(question, retriever)

            st.subheader("Answer")
            st.write(answer)


# with open("report.html", "rb") as f:
#     st.download_button(
#         "Download Report",
#         f,
#         file_name="report.html",
#         mime="text/html"
#     )







    

