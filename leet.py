import streamlit as st
import  matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg') #backend
from wordcloud import WordCloud #Visualization

#Functions
LEET_DICTIONARY={'a': '4', 'b': '13', 'c': '(', 'd': '[)', 'e': '3', 'f': '7', 'g': '9', 'h': '#', 'i': '!'}
GREEK_DICTIONARY={'a': 'α', 'b': 'β', 'c': 'γ', 'd': 'Δ', 'e': 'ε', 'f': 'ζ', 'g': '9', 'h': 'Η', 'i': 'ι'}
NATOPHONETICS_DICTIONARY = {"A": "Alpha", "B": "Beta", "C": "Car", "D": "Delta", "E": "Elephant", "F": "Fox", "G": "Goa", "H": "Helicopter"}

def leet_convertor(term):
    result = [LEET_DICTIONARY.get(i,i) for i in list(term.lower())]
    return ''.join(result)

def greek_convertor(term):
    result = [GREEK_DICTIONARY.get(i,i) for i in list(term.lower())]
    return ''.join(result)
def nato_phonetizer(term):
    result = [NATOPHONETICS_DICTIONARY.get(i,i) for i in list(term.upper())]
    return ' '.join(result)
# Functions for visualization
#@st.cache Deprecated
def plot_wordcloud(docx):
    mywordcloud= WordCloud().generate(docx)
    fig = plt.figure(figsize= (20,10))
    plt.imshow(mywordcloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(fig)

def main():
    st.title("Leet Speak App")
    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Home":
        # Layout
        col1, col2 = st.columns(2)
        with col1:
            st.info("Leet Convertor")
            # Form
            with st.form(key='Leetform', clear_on_submit=True):
                raw_text=st.text_area("Enter Text Here")
                convertion_choice = st.selectbox("Choice",['Normal', 'Greek'])
                submit_button = st.form_submit_button(label='Convert')
                # Result
                if submit_button:
                    st.info("Results")
                    st.write("Original:{}".format(raw_text))
                    if convertion_choice == 'Greek':

                        result = greek_convertor(raw_text)
                    else:
                        result = leet_convertor(raw_text)
                    st.code(result)
                    # Visualization
                    with st.expander("Visualize"):
                        plot_wordcloud(raw_text)


        with col2:
            st.success("Nato Phonetizor")
            with st.form(key='natoform', clear_on_submit=True):
                raw_text = st.text_area("Enter Text Here")
                submit_button = st.form_submit_button(label='Phonetize')
            # Result
            if submit_button:
                st.info("Results")
                st.write("Original:{}".format(raw_text))
                result = nato_phonetizer(raw_text)
                st.info("Copy")
                st.code(result) #Copiable
                #Visualize
                with st.expander("Visualize"):
                    plot_wordcloud(result)
    else:
        st.subheader("About")
        st.text("Leet Speak App")
if __name__ =='__main__':
        main()