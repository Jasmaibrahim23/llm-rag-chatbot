import streamlit as st
from chatbot import ask_question

st.set_page_config(page_title="RAG-Powered Chatbot", layout="wide")
st.title("🔎 Retrieval-Augmented Chatbot")

query = st.text_input("Ask a question about the documents:")
if query:
    # with st.spinner("Searching..."):
    #     response = ask_question(query)
    #     st.write(response)
    #     if query:
    with st.spinner("Searching..."):
        response = ask_question(query)
        # Display the main answer
        st.markdown("### Answer:")
        st.write(response.get("result", "No answer found."))

        # Optionally display source docs nicely
        st.markdown("### Source Documents:")
        for i, doc in enumerate(response.get("source_documents", [])):
            st.write(f"**Document {i+1}:**")
            #metadata = doc.get("metadata", {})
            metadata = getattr(doc, "metadata", {})

            # Show some metadata info
            st.write(metadata)
            # Show snippet of content (truncate if too long)
            content = doc.get("page_content", "")
            st.write(content[:500] + ("..." if len(content) > 500 else ""))

