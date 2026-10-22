
import streamlit as st
import fitz
import io
import base64
import os
st.set_page_config(page_title="PDF Statement Finder", page_icon="📄", layout="wide")
if os.path.exists("earth.png."):
    with open("earth.png", "rb") as image:
        encoded_image = base64.b64encode(image.read()).decode()
    background_css = f'background-image: url("data:image/jpeg;base64,{encoded_image}");'
st.markdown(f"""
<style>
.stApp {{
    {background_css}
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}
.stApp::before {{
    content: "";
    position: fixed;
    inset: 0;
    background: rgba(0, 0, 0, 0.55);
    pointer-events: none;
}}
.stApp > header, .stApp > div {{
    position: relative;
}}
h1, h2, h3, p, label {{
    color: white !important;
}}
div[data-testid="stFileUploader"], div[data-testid="stTextInput"] {{
    background: rgba(255, 255, 255, 0.12);
    padding: 15px;
    border-radius: 12px;
}}
div.stButton > button {{
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 10px 25px;
    font-weight: bold;
}}
div.stButton > button:hover {{
    background-color: #0056b3;
    color: white;
}}
</style>
""", unsafe_allow_html=True)
st.title("📄 PDF Statement Finder")
st.write("Upload your PDF document and find any statement instantly.")
uploaded_file = st.file_uploader("Upload your PDF document", type=["pdf"])
statement = st.text_input("Enter the statement or keyword you are looking for", placeholder="Example: Employees are entitled to annual leave")
if uploaded_file is not None:
    pdf_bytes = uploaded_file.getvalue()
    try:
        pdf = fitz.open(stream=pdf_bytes, filetype="pdf")
        st.success(f"PDF uploaded successfully! Total pages: {len(pdf)}")
        if st.button("🔍 Search Statement"):
            if statement.strip():
                results = []
                for page_number in range(len(pdf)):
                    page = pdf[page_number]
                    matches = page.search_for(statement.strip())
                    if matches:
                        results.append((page_number, matches))
                if results:
                    st.success(f"Statement found on {len(results)} page(s)!")
                    st.write("### Matching Pages")
                    for page_number, matches in results:
                        st.subheader(f"📌 Page {page_number + 1}")
                        page = pdf[page_number]
                        for match in matches:
                            highlight = page.add_highlight_annot(match)
                            highlight.set_colors(stroke=(1, 1, 0))
                            highlight.update()
                        pix = page.get_pixmap(matrix=fitz.Matrix(1.5, 1.5), alpha=False)
                        st.image(pix.tobytes("png"), caption=f"Page {page_number + 1}", use_container_width=True)
                        st.info(f"Found {len(matches)} matching occurrence(s) on page {page_number + 1}.")
                    output = io.BytesIO()
                    pdf.save(output, garbage=4, deflate=True)
                    st.download_button("📥 Download Highlighted PDF", data=output.getvalue(), file_name="highlighted_document.pdf", mime="application/pdf")
                else:
                    st.warning("Statement not found in the uploaded PDF.")
            else:
                st.warning("Please enter a statement or keyword to search.")
        pdf.close()
    except Exception as error:
        st.error(f"Unable to process PDF: {error}")
else:
    st.info("Please upload a PDF document to begin.")
st.markdown("---")
st.caption("PDF Statement Finder by Riley Gakuo")