# Implementation Note

## India Health Policy RAG Assistant

### Introduction

The objective of this project was to build a Retrieval-Augmented Generation (RAG) application capable of answering questions from the Press Information Bureau's *India's Health Transformation* report. The system retrieves relevant information from the document before generating an answer, ensuring that responses are based on the provided content rather than relying only on the language model's pre-trained knowledge.

The application consists of five main stages: document ingestion, text chunking, embedding generation, semantic retrieval, and answer generation using a Large Language Model (LLM). A Streamlit interface was developed to allow users to interact with the system through a simple question-answering interface.


## Design Choices

### Embedding Model

The project uses the **BAAI/bge-small-en-v1.5** embedding model to generate vector representations of document chunks and user queries. This model was selected because it offers good semantic retrieval performance while remaining lightweight enough to run efficiently on a standard laptop. Its balance between accuracy and computational efficiency makes it well suited for a document retrieval application such as this project.

### Storage and Indexing

The generated embeddings are stored using **FAISS (Facebook AI Similarity Search)**. FAISS was chosen because it is specifically designed for fast similarity search over dense vector embeddings and integrates well with Python applications. Since the source document produces only a few hundred text chunks, the **IndexFlatL2** index provides accurate nearest-neighbor search without introducing unnecessary complexity.

The project stores the vector index in `vectorstore/faiss.index`, while the corresponding document chunks are stored separately in `vectorstore/chunks.pkl`. During retrieval, the FAISS index identifies the most relevant vectors, and the stored chunks are used to reconstruct the context for answer generation.

### Language Model

The application uses **Llama 3.1** through the **Groq API** for response generation. Groq was selected because it provides fast inference with a simple API, making it suitable for an interactive question-answering application. The language model receives only the retrieved document context instead of the complete document, allowing it to generate focused and context-aware responses.

### Prompt Design

The prompt is designed to encourage grounded responses. It instructs the language model to answer only from the retrieved document context and to clearly indicate when the required information is not available. This approach helps reduce hallucinations and keeps the generated answers aligned with the source document.


## What I Learned / Research Undertaken

This project provided me with hands-on experience in building a complete Retrieval-Augmented Generation (RAG) application, from document ingestion to answer generation. Before starting this assignment, I had a basic understanding of Large Language Models but limited practical experience with RAG systems and vector databases.

During the implementation, I learned how to extract and clean text from HTML documents using BeautifulSoup and how to split large documents into overlapping chunks using LangChain's `RecursiveCharacterTextSplitter`. I understood the importance of choosing an appropriate chunk size and overlap to preserve context and improve retrieval quality.

I explored how embedding models work and learned how the **BAAI/bge-small-en-v1.5** model converts text into dense vector representations that capture semantic meaning. I also researched **FAISS (Facebook AI Similarity Search)** and gained an understanding of how vector embeddings are indexed and searched efficiently to retrieve the most relevant document chunks.

While integrating the language model, I learned the importance of prompt engineering and how carefully designed prompts help ensure that responses are grounded in the retrieved context rather than relying solely on the model's internal knowledge. This helped me understand how Retrieval-Augmented Generation reduces hallucinations and improves the reliability of AI-generated answers.

Beyond the AI concepts, I strengthened my practical software development skills by organizing the application into modular components, managing project dependencies, using Git and GitHub for version control, documenting the project with a professional README, and debugging compatibility issues to ensure the application worked correctly on a fresh project setup.

Overall, this assignment significantly improved my understanding of Retrieval-Augmented Generation, semantic search, embedding models, vector databases, prompt engineering, and the end-to-end workflow involved in developing a document-based AI assistant. It also gave me valuable experience in building, testing, debugging, and documenting a complete AI application.


## Limitations

Although the application successfully demonstrates a complete Retrieval-Augmented Generation pipeline, it has some limitations.

- The application currently supports only a single HTML document as the knowledge source.
- It does not maintain conversational memory, so each question is processed independently.
- The retrieval process uses exact vector search and does not include hybrid retrieval methods such as keyword-based search combined with semantic search.
- Responses are generated from the retrieved context, but individual sentences are not linked to specific citations within the document.
- The application is designed for local execution and has not been deployed on a cloud platform.


## Future Improvements

If I had two additional days to continue this project, I would focus on improving both functionality and usability.

The first improvement would be to support multiple document formats such as PDF and DOCX, allowing the application to work with a wider range of data sources. I would also extend the system to retrieve information from multiple documents instead of a single knowledge base.

To improve retrieval quality, I would experiment with hybrid search by combining semantic similarity search with keyword-based retrieval. Another useful enhancement would be adding conversational memory so that users could ask follow-up questions without repeating previous context.

From a user experience perspective, I would include inline citations within generated responses, improve the interface further, and deploy the application on a cloud platform so that it could be accessed without requiring a local Python environment.


## Conclusion

This project demonstrates the complete workflow of a Retrieval-Augmented Generation application, from document ingestion and embedding generation to semantic retrieval and grounded answer generation. Working on this project strengthened my understanding of vector databases, embedding models, semantic search, prompt engineering, and Large Language Model integration. It also provided valuable experience in developing an end-to-end AI application using Python and Streamlit.
