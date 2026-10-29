import streamlit as st
import time #speed of typing
import random#choose a random sentence
import html#format the output
#page setup
st.set_page_config(page_title="Typing Speed Test")
st.title("Typing Speed Test")
st.write("Type the sentence below as quickly and accurately as possible!")
sentences = [
    "Python is a fun programming language.",
    "I love learning how to code.",
    "Practice makes perfect.",
    "The quick brown fox jumps over the lazy dog.",
    "Technology makes our lives easier",
]
#save the user progress
if "sentence" not in st.session_state:
    st.session_state.sentence = random.choice(sentences)
    st.session_state.start = None
typed = st.text_input("Type here:", key="typing")
if typed and st.session_state.start is None:
    st.session_state.start = time.time()
highlighted = ""
#check each letter and spelling
for i, letter in enumerate(st.session_state.sentence):
    if i < len(typed):
        color = "green" if typed[i] == letter else "red"
    else:
        color = "gray"
    highlighted += f'<span style="color:{color}">{html.escape(letter)}</span>'
st.markdown(
    f'<div style="font-size:24px;line-height:2;letter-spacing:1px">{highlighted}</div>',
    unsafe_allow_html=True
)
#check for accuracy
if typed:
    correct=sum(a==b for a,b in zip(typed,st.session_state.sentence))
    accuracy=correct/len(typed)*100
    st.write(f"Accuracy:{accuracy:.1f}%")
    #summary of output
    if typed==st.session_state.sentence:
        #typing speed
        seconds=time.time()-st.session_state.start
        #word per minute
        wpm=(len(typed)/5)/(seconds/60)
        st.success("Excellent you have finished your sentence")
        st.write(f"Time:{seconds:.1f}seconds")
        st.write(f"Typing speed:{wpm:.1f} wpm")
#generate a new sentence
if st.button("New sentence"):
    st.session_state.sentence = random.choice(sentences)
    st.session_state.start = None
    st.session_state.typing = ""
    st.rerun()