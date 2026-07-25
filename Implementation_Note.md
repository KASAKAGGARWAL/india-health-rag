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


## What I Learned

This project gave me practical experience with Retrieval-Augmented Generation (RAG), a concept that I had previously understood only at a theoretical level. Building the application helped me understand how multiple components work together to create a document-based question-answering system.

During development, I learned how to extract clean text from an HTML document, divide it into overlapping chunks, and convert those chunks into semantic embeddings using a Sentence Transformer model. I also gained practical experience with FAISS for vector indexing and similarity search, which allowed the application to retrieve the most relevant document sections for a given question.

Another important learning outcome was understanding the role of prompt engineering in RAG systems. I learned that the quality of the generated response depends not only on the language model but also on the retrieved context and the instructions provided in the prompt. Integrating the Groq API and building the Streamlit interface also gave me experience in connecting machine learning components into a complete end-to-end application.

Finally, I improved my debugging skills while resolving dependency issues, configuring the development environment, and integrating different Python libraries into a working system.


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