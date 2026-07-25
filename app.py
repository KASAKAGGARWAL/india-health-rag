import time

import streamlit as st

from retriever import Retriever
from llm import generate_answer


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Health Policy RAG Assistant",
    page_icon="🇮🇳",
    layout="wide"
)

st.markdown("""
<style>

/* Main container */
.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

/* Header Card */
.header-box{
    background:#0E1117;
    padding:25px;
    border-radius:15px;
    border:1px solid #31333F;
    margin-bottom:25px;
}

.metric-box{
    background:#F8F9FA;
    padding:10px;
    border-radius:10px;
}

.footer{
    text-align:center;
    color:gray;
    font-size:14px;
    margin-top:40px;
}

</style>
""", unsafe_allow_html=True)
# --------------------------------------------------
# Session State
# --------------------------------------------------

if "history" not in st.session_state:
    st.session_state.history = []

if "retriever" not in st.session_state:
    st.session_state.retriever = Retriever()

retriever = st.session_state.retriever

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:

    st.title("🇮🇳 Health Policy RAG")

    st.info(
    """
### About

This application uses:

- 🔍 Semantic Search
- 📚 FAISS Vector Database
- 🤖 Groq Llama 3.1
- 🧠 BGE Embeddings

Responses are generated **only** from the supplied PIB document.
"""
)

    top_k = st.slider(
        "Retrieved Chunks",
        min_value=2,
        max_value=8,
        value=5
    )

    if st.button("🧹 Clear Conversation"):

        st.session_state.history = []

        st.rerun()

# --------------------------------------------------
# Header
# --------------------------------------------------

st.markdown("""
<div class="header-box">

# 🇮🇳 Health Policy RAG Assistant

### AI-powered Document Intelligence

Ask questions grounded in the **Press Information Bureau's "India's Health Transformation"** report using Retrieval-Augmented Generation (RAG).

</div>
""", unsafe_allow_html=True) 

st.subheader("🔍 Ask a Question")

question = st.text_input(
    "Question",
    placeholder="Example: What is Ayushman Bharat?",
    label_visibility="collapsed"
)

ask = st.button(
    "🔍 Analyze Question",
    type="primary",
    use_container_width=True
)

# --------------------------------------------------
# Main Logic
# --------------------------------------------------

if ask:

    if question.strip() == "":

        st.warning("Please enter a question.")

    else:

        start = time.time()

        with st.spinner("Searching document..."):

            results = retriever.search(
                question,
                top_k
            )

            context = "\n\n".join(
                item["text"]
                for item in results
            )

        with st.spinner("Generating answer..."):

            answer = generate_answer(
                question,
                context
            )

        elapsed = time.time() - start

        st.session_state.history.append(
            {
                "question": question,
                "answer": answer,
                "sources": results,
                "time": elapsed,
            }
        )

# --------------------------------------------------
# Conversation Display
# --------------------------------------------------

if st.session_state.history:

    st.divider()

    st.subheader("Conversation")

    for idx, item in enumerate(reversed(st.session_state.history), start=1):

        with st.container(border=True):

            st.markdown(f"### Question {idx}")

            st.write(item["question"])

            st.markdown("### Answer")

            st.write(item["answer"])

            col1, col2 = st.columns([3, 1])

            with col1:
                st.caption(
                    f"Retrieved {len(item['sources'])} chunks"
                )

            with col2:
                st.metric(
                    "⚡ Response Time",
                    f"{item['time']:.2f}s"
                )

            st.markdown("### Sources")

            for source in item["sources"]:

                st.success(
                    f"📄 Evidence {source['id']}  |  Confidence: {source['score']*100:.1f}%"
                )

            with st.expander("Retrieved Context"):

                for source in item["sources"]:

                    st.markdown(
                        f"#### 📄 Evidence {source['id']}"
                    )

                    st.write(source["text"])

                    st.divider()

            st.download_button(
                label="📥 Download Answer",
                data=item["answer"],
                file_name="answer.txt",
                mime="text/plain",
                key=f"download_{idx}"
            )

st.divider()

st.markdown("""
<div class="footer">

<b>Health Policy RAG Assistant</b><br>

Built using Python • Streamlit • FAISS • Sentence Transformers • Groq Llama 3.1

<br><br>

Responses are generated only from the supplied PIB document using Retrieval-Augmented Generation (RAG).

</div>
""", unsafe_allow_html=True)