# 📚 AskMyDocs with AI

An AI-powered document question-answering application that allows users to upload PDF documents and ask questions in natural language. The application uses Large Language Models (LLMs), vector embeddings, and semantic search to provide accurate answers based on the uploaded documents.

---

## 🚀 Features

* 📄 Upload one or more PDF documents
* 🤖 Ask questions in natural language
* 🧠 AI-powered document understanding
* 🔍 Semantic search using vector embeddings
* ⚡ Fast responses with FAISS vector database
* 🌐 Simple and interactive Streamlit interface

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **LangChain**
* **FAISS**
* **Google Generative AI Embeddings**
* **Cohere LLM**
* **PyPDF**
* **python-dotenv**

---

## 📂 Project Structure

```text
AskMyDocs/
│
├── app.py
├── requirements.txt
├── .env
├── logo.png
├── style.css
│
├── backend/
│   ├── embedding.py
│   ├── llm.py
│   ├── ques_Ans_chain.py
│   ├── splitter.py
│   ├── vector.py
│   └── CreateVector.py
│
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/AskMyDocs.git
```

### 2. Navigate to the project

```bash
cd AskMyDocs
```

### 3. Create a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a **.env** file in the project root.

```env
COHERE_API_KEY=your_cohere_api_key
GOOGLE_API_KEY=your_google_api_key
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📖 How It Works

1. Upload one or more PDF files.
2. The PDFs are split into smaller text chunks.
3. Embeddings are created for each chunk.
4. FAISS stores the embeddings as a vector database.
5. When you ask a question, the application retrieves the most relevant chunks.
6. The LLM generates an answer using the retrieved context.

---

## 📦 Main Dependencies

* Streamlit
* LangChain
* FAISS
* Cohere
* Google Generative AI
* PyPDF
* python-dotenv

---

## 📸 Screenshots
![Final Output]https://github.com/RahulYadav-75/AskmyDocs/blob/main/Final_output.png

Example:

```
images/
├── home.png
├── upload.png
└── answer.png
```

---

## 🎯 Future Improvements

* Support Word and PowerPoint documents
* Chat history
* Multiple LLM providers
* User authentication
* Cloud deployment
* OCR support for scanned PDFs

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Rahul Yadav**

Computer Science (Data Science) Student

Feel free to contribute or raise issues for improvements.

