# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 20:38:40 2022

@author: Prakash
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
import io
import nltk
from nltk.tokenize import word_tokenize, RegexpTokenizer, sent_tokenize
from nltk.corpus import stopwords
import PyPDF2 as pdfs
from PyPDF2 import PdfFileMerger
import streamlit as st
from wordcloud import WordCloud
from nltk.corpus.reader.api import *
from nltk.corpus.reader.util import *
from nltk.tokenize import line_tokenize
st.set_option('deprecation.showPyplotGlobalUse', False)
from stop_words import get_stop_words
s = list(get_stop_words('en'))
stop_words_NLP = stopwords.words('english')
stop_words_NLP.extend(s)
custom_stop_words = [",", "@", "%", "c", "Aa=Zz", 
";", ",", '•', '.', "(", ")", ":", "[", "]",
"0-9", "-", "_", ",", 
"–", "the", "a", "of", "as", 
"by", "on", "and", "is", "The", "i", 
"in", "to", "for", "this", "an", "it", "A", "’", "<", ">", 
"................................", "„", "‟", "of", "as", "hi", "am", "is", "that", "s", "“", "”",
"at", "we", "not", "be", "with", "are", "..", "t", "&", "THE", "AND", "‘", "if", "IF" ]
#os.chdir(r'input_file.path')


# Sidebar options

#option = st.sidebar.selectbox('Navigation', key = "m"
#["Word Count",
# "UniGram", 
# "BiGram",
#"TriGram", 
 #"Word Cloud"])

def uploaded_files():
    with open(os.path.join("storefiles", uploads.name),"wb") as f:
        f.write(uploads.getbuffer())
    #return st.write("Saved")
        

       
choice = st.selectbox(
     'Select Type Of PDF File Input',
     ( 'Single PDF', 'Multi PDF'))

st.write('You selected:', choice)

if choice == 'Single PDF':
    option = st.sidebar.selectbox('Navigation',
    ["Word Count",
     "UniGram", 
     "BiGram",
    "TriGram", 
     "Word Cloud"], key=(11))
    input_file = st.file_uploader("Choose a PDF file", type=['pdf'], accept_multiple_files=False)
    
    if not input_file:
        st.title("Please upload a PDF File")
        st.stop()
        
            
else:
    pass
        

if choice == 'Multi PDF':
    option = st.sidebar.selectbox('Navigation',
    ["Word Count",
     "UniGram", 
     "BiGram",
    "TriGram", 
     "Word Cloud"], key=(12))
    input_files = st.file_uploader("Choose PDF files", type=['pdf'], accept_multiple_files=True)
    if input_files is not None:
        st.subheader("Upload Minimum 2 PDF Files")
        
   
        for uploads in input_files:
            uploaded_files()
            

            #x = len(uploads)
        #if st.button("Submit File", key="30"):
                #d = os.listdir('tempDir')
        #d = os.getcwd()
        #d
        #fd = os.path.join("storefiles")
            
        path_to_files = r'storefiles/'
                    
        merger = PdfFileMerger()
            
                
            #g = str(path_to_files)
            #fd
        #st.subheader("Uploaded Files Names")
        #e = list(os.listdir(path_to_files))
        #e
            
            #x = [a for a in e if a.endswith(".pdf")]
        for root, dirs, file_names in os.walk(path_to_files):
            for file_name in file_names:
                merger.append(path_to_files + file_name)
        merger.write("file.pdf")
        merger.close()
        mypath = "storefiles/"
        for root, dirs, files in os.walk(mypath):
            for file in files:
                os.remove(os.path.join(root, file))
        #st.success('Done!')
                
                   
                     
        
                #merger.append(pdf)
        #merged_file = "file.pdf"
            #file_details = {"filename":merged_file.name, "filetype":merged_file.type,
                                       #"filesize":merged_file.size}
            #st.write(file_details)
        
       #x
    #st.write("saved")
    
        #st.stop()
        #x = len(input_files)
        



    #for item in input_files:
        #for uploads in input_files:
            
            #with open(os.path.join("tempDir", uploads.name),"wb") as f:
                #f.write(uploads.getbuffer())
            #uploads =[] 
            #st.success("Saved")   
                    
                  
                #st.success("Saved")
                #st.title("Please upload PDF Files")
                    
                       
                      
                       
else:
      pass                   
                       
                #st.stop()
                    
            
        
            #x = len(input_files)
            
            #bytes_data = uploads.read()
            #pdf = pdfs.open(io.BytesIO(bytes_data))
            #st.write("file name:", uploads.name)
        #def save_uploaded_file(input_files):
            
               
    
if choice == 'Single PDF':
    
    file_details = {"filename":input_file.name, "filetype":input_file.type,
                               "filesize":input_file.size}
    st.write(file_details)
    fileReader = pdfs.PdfFileReader(input_file)
    pages = fileReader.numPages
    st.caption("Pages of The File")
    st.caption(pages)
else:
    pass
    
if option == 'Word Count' and choice == 'Single PDF':
    if st.button("Click to Submit File", key="1"):
        num_pages = fileReader.numPages
        count = 0
        text = ""
        while count < num_pages:
            pageObj = fileReader.getPage(count)
            count +=1
            text += pageObj.extractText()
            stop_words_list = stop_words_NLP and custom_stop_words
            word_tokens = word_tokenize(text)
            without_stopwords_sentence = []
              
        for w in word_tokens:
            if w not in stop_words_list:
                without_stopwords_sentence.append(w)
                    #without_stopwords_sentence
           
        fdist1 = nltk.FreqDist(without_stopwords_sentence)
            #Get Most Common Words

        common = fdist1.most_common(50)

            #common.plot()
        df = pd.DataFrame(common)
        df.columns = ['word', 'counts']
        st.subheader("Showing 50 Words Count")
        df

elif option == 'UniGram' and choice == 'Single PDF':
         
    if st.button("Click to Submit File", key="2"):
        num_pages = fileReader.numPages
        count = 0
        text = ""
        while count < num_pages:
            pageObj = fileReader.getPage(count)
            count +=1
            text += pageObj.extractText()
            stop_words_list = stop_words_NLP and custom_stop_words
            word_tokens = word_tokenize(text)
            without_stopwords_sentence = []
              
        for w in word_tokens:
            if w not in stop_words_list:
                without_stopwords_sentence.append(w)
        fdist1 = nltk.FreqDist(without_stopwords_sentence)
        #Get Most Common Words

        common = fdist1.most_common(10)

        #common.plot()
        df_unigram = pd.DataFrame(common)
        df_unigram.columns = ['word', 'counts']
        #st.subheader("Showing 50 Words Count")
        st.subheader("Showing Top 10 Words")
        df_unigram.plot()
        sns.barplot(x='word',y='counts',data=df_unigram)
        plt.xticks(rotation=70)
        #sns.lineplot(x='word',y='counts',data=df)
        st.pyplot()
        #st.image(graph)
        st.bar_chart(data=df_unigram, x="word", y="counts",use_container_width=True)
        
elif option ==  "BiGram" and choice == 'Single PDF':
    if st.button("Click to Submit File", key="3"):
        num_pages = fileReader.numPages
        count = 0
        text = ""
        while count < num_pages:
            pageObj = fileReader.getPage(count)
            count +=1
            text += pageObj.extractText()
            stop_words_list = stop_words_NLP and custom_stop_words
            word_tokens = word_tokenize(text)
            without_stopwords_sentence = []
              
        for w in word_tokens:
            if w not in stop_words_list:
                without_stopwords_sentence.append(w)
        fdist1 = nltk.FreqDist(without_stopwords_sentence)
        #Get Most Common Words

        bigram_words = nltk.FreqDist(nltk.bigrams(without_stopwords_sentence))
        bigram_count = bigram_words.most_common(10)
        df_bigram = pd.DataFrame(bigram_count)
        df_bigram.columns = ['Bigram Word', 'Counts']
        #st.subheader("Showing 50 Words Count")
        st.subheader("Showing Top 10 Bigram Words")
        df_bigram.plot()
        bigram_sns = sns.barplot(x='Bigram Word',y='Counts',data=df_bigram)
        plt.xticks(rotation=70)
        #sns.lineplot(x='word',y='counts',data=df)
        st.pyplot()
        #st.image(graph)
        st.bar_chart(data=df_bigram, x="Bigram Word", y="Counts",use_container_width=True)
        
elif option ==  "TriGram" and choice == 'Single PDF':
    if st.button("Click to Submit File", key="4"):
        #file = open(input_file)
        #st.subheader("Total Number Of Pages")
        
        num_pages = fileReader.numPages
        count = 0
        text = ""
        while count < num_pages:
            pageObj = fileReader.getPage(count)
            count +=1
            text += pageObj.extractText()
            stop_words_list = stop_words_NLP and custom_stop_words
            word_tokens = word_tokenize(text)
            without_stopwords_sentence = []
              
        for w in word_tokens:
            if w not in stop_words_list:
                without_stopwords_sentence.append(w)
        
        bigram_words = nltk.FreqDist(nltk.trigrams(without_stopwords_sentence))
        #Get Most Common Words

        trigram_count = bigram_words.most_common(10)

        #common.plot()
        df_trigram = pd.DataFrame(trigram_count)
        df_trigram.columns = ['Trigram Word', 'Counts']
        #st.subheader("Showing 50 Words Count")
        st.subheader("Showing Top 10 Trigram Words")
        df_trigram.plot()
        trigram_sns = sns.barplot(x='Trigram Word',y='Counts',data=df_trigram)
        plt.xticks(rotation=70)
        #sns.lineplot(x='word',y='counts',data=df)
        st.pyplot()
        #st.image(graph)
        st.bar_chart(data=df_trigram, x="Trigram Word", y="Counts",use_container_width=True)
    
elif option ==  "Word Cloud" and choice == 'Single PDF':
    if st.button("Click to Submit File", key="5"):
        num_pages = fileReader.numPages
        count = 0
        text = ""
        while count < num_pages:
            pageObj = fileReader.getPage(count)
            count +=1
            text += pageObj.extractText()

        
        stop_words_list = stop_words_NLP and custom_stop_words
        word_tokens = word_tokenize(text)
        without_stopwords_sentence = []
          
        for w in word_tokens:
            if w not in stop_words_list:
                without_stopwords_sentence.append(w)
        wc = WordCloud(
        background_color = 'black',
        stopwords = stop_words_list,
        height = 700,
        width = 1000
        )
        i = wc.generate(str(without_stopwords_sentence))
        #plt.imshow(i)
        fig, ax = plt.subplots()
        ax.imshow(i, interpolation='bilinear')
        ax.axis("off")
        st.pyplot(fig)
 
#if choice == 'Multi PDF':
    
    #if st.button("Submit File", key="11"):
        
        #d = os.listdir('tempDir')
        #d = os.getcwd()
        #d
        #fd = os.path.join("storefiles")
        
        #path_to_files = r'storefiles/'
                
        #merger = PdfFileMerger()
        
            
        #g = str(path_to_files)
        #fd
        #st.write("Uploaded File Names")
        #e = list(os.listdir(path_to_files))
        #e
        
        #x = [a for a in e if a.endswith(".pdf")]
        #for root, dirs, file_names in os.walk(path_to_files):
            #for file_name in file_names:
                #merger.append(path_to_files + file_name)
        #merger.write("file.pdf")
        #merger.close()
            #merger.append(pdf)
        #merged_file = "file.pdf"
        #file_details = {"filename":merged_file.name, "filetype":merged_file.type,
                                   #"filesize":merged_file.size}
        #st.write(file_details)
        #fileReader_multi = pdfs.PdfFileReader(merged_file)
        #pages = fileReader_multi.numPages
        #st.caption("Pages of The File")
        #st.caption(pages)    
        #merger.write("merged.pdf")
        #merger.close()
        #for pdf in x:
            
            #merger.append(open(pdf, 'rb'))
        #with open("merged.pdf", "wb") as fout:
            #merger.write(fout)
        
    #Iterate over the list of file names
            
                
        
               
        #Append PDF files
             
        
        #def change():
            #os.chdir(r"./tempDir")
        #buton_click()
        #change()
        #def merging():
        
        
        #for pdf in os.listdir(r'tempDir'):
            
            #merger.append(pdf)
            #with open("merged.pdf", "wb") as fout:
        #merger.write("mergered.pdf")
        #merger.close()
        #merger = PdfFileMerger()
        
                
                 
        #merging()         
        #fileReader = pdfs.PdfFileReader("storefiles/merged.pdf")
        #pages = fileReader.numPages
        #st.caption("Pages of The File")
        #st.caption(pages)   
        
        #os.chdir(r'./tempDir')
        
       
    #os.chdir(r'C:/Users/Prakash/tempDir/')
      
    
    #with open(input_files, "wb") as f:
        #f.write(buf.getbuffer())
    
        
        #with open(os.path.join("tempDir",input_files.name),"wb") as f:
          #f.write(input_files.getbuffer())
            
#def submit_button():
    #st.button("Click to Submit File", key="22")
    
if option == 'Word Count' and choice == 'Multi PDF':
        #submit_button()
    if st.button("Click to Submit", key="31"):
        merged_file = "file.pdf"
        fileReader_multi = pdfs.PdfFileReader(merged_file)
        pages = fileReader_multi.numPages
        st.caption("Pages of The File")
        st.caption(pages) 
        
        #fileReader_multi = pdfs.PdfFileReader(merged_file)
        num_pages = fileReader_multi.numPages
        count = 0
        text_multi = ""
        while count < num_pages:
            pageObj = fileReader_multi.getPage(count)
            count +=1
            text_multi += pageObj.extractText()
            stop_words_list = stop_words_NLP and custom_stop_words
            word_tokens = word_tokenize(text_multi)
            without_stopwords_sentence_multi = []
              
        for w in word_tokens:
            if w not in stop_words_list:
                without_stopwords_sentence_multi.append(w)
        fdist1_mutiword = nltk.FreqDist(without_stopwords_sentence_multi)
                    #Get Most Common Words

        common_multi_wordcount = fdist1_mutiword.most_common(50)

            #common.plot()
        df_multi_word = pd.DataFrame(common_multi_wordcount)
        df_multi_word.columns = ['word', 'counts']
        st.subheader("Showing 50 Words Count")
        df_multi_word
        
elif option ==  "UniGram" and choice == 'Multi PDF':
    if st.button("Click to Submit", key="32"):
        merged_file = "file.pdf"
        fileReader_multi = pdfs.PdfFileReader(merged_file)
        pages = fileReader_multi.numPages
        st.caption("Pages of The File")
        st.caption(pages) 
        
        #fileReader_multi = pdfs.PdfFileReader(merged_file)
        num_pages = fileReader_multi.numPages
        count = 0
        text_multi = ""
        while count < num_pages:
            pageObj = fileReader_multi.getPage(count)
            count +=1
            text_multi += pageObj.extractText()
            stop_words_list = stop_words_NLP and custom_stop_words
            word_tokens = word_tokenize(text_multi)
            without_stopwords_sentence_multi = []
              
        for w in word_tokens:
            if w not in stop_words_list:
                without_stopwords_sentence_multi.append(w)
        fdist1_mutiword = nltk.FreqDist(without_stopwords_sentence_multi)
                    #Get Most Common Words
    
        common_multi_wordcount = fdist1_mutiword.most_common(10)
        df_multi_word = pd.DataFrame(common_multi_wordcount)
        df_multi_word.columns = ['word', 'counts']
        st.subheader("Showing 10 UniGram Words Count")
       
        df_multi_word.columns = ['word', 'counts']
        #st.subheader("Showing 50 Words Count")
        #st.subheader("Showing Top 10 Words")
        df_multi_word.plot()
        sns.barplot(x='word',y='counts',data=df_multi_word)
        plt.xticks(rotation=70)
        #sns.lineplot(x='word',y='counts',data=df)
        st.pyplot()
        #st.image(graph)
        st.bar_chart(data=df_multi_word, x="word", y="counts",use_container_width=True)
    
        
elif option ==  "BiGram" and choice == 'Multi PDF':
    if st.button("Click to Submit", key="33"):
        merged_file = "file.pdf"
        fileReader_multi = pdfs.PdfFileReader(merged_file)
        pages = fileReader_multi.numPages
        st.caption("Pages of The File")
        st.caption(pages) 
        
        #fileReader_multi = pdfs.PdfFileReader(merged_file)
        num_pages = fileReader_multi.numPages
        count = 0
        text_multi = ""
        while count < num_pages:
            pageObj = fileReader_multi.getPage(count)
            count +=1
            text_multi += pageObj.extractText()
            stop_words_list = stop_words_NLP and custom_stop_words
            word_tokens = word_tokenize(text_multi)
            without_stopwords_sentence_multi = []
        for w in word_tokens:
            if w not in stop_words_list:
                without_stopwords_sentence_multi.append(w)
        fdist1 = nltk.FreqDist(without_stopwords_sentence_multi)
        
        bigram_words_multi = nltk.FreqDist(nltk.bigrams(without_stopwords_sentence_multi))
        bigram_count = bigram_words_multi.most_common(10)
        
        df_bigram_multi = pd.DataFrame(bigram_count)
        df_bigram_multi.columns = ['Bigram Word', 'Counts']
        #st.subheader("Showing 50 Words Count")
        st.subheader("Showing Top 10 Bigram Words")
        df_bigram_multi.plot()
        bigram_multi_sns = sns.barplot(x='Bigram Word',y='Counts',data=df_bigram_multi)
        plt.xticks(rotation=70)
        #sns.lineplot(x='word',y='counts',data=df)
        st.pyplot()
        #st.image(graph)
        st.bar_chart(data=df_bigram_multi, x="Bigram Word", y="Counts",use_container_width=True)
    
elif option ==  "TriGram" and choice == 'Multi PDF':
    if st.button("Click to Submit", key="34"):
        merged_file = "file.pdf"
        fileReader_multi = pdfs.PdfFileReader(merged_file)
        pages = fileReader_multi.numPages
        st.caption("Pages of The File")
        st.caption(pages) 
        
        #fileReader_multi = pdfs.PdfFileReader(merged_file)
        num_pages = fileReader_multi.numPages
        count = 0
        text_multi = ""
        while count < num_pages:
            pageObj = fileReader_multi.getPage(count)
            count +=1
            text_multi += pageObj.extractText()
            stop_words_list = stop_words_NLP and custom_stop_words
            word_tokens = word_tokenize(text_multi)
            without_stopwords_sentence_multi = []
        for w in word_tokens:
            if w not in stop_words_list:
                without_stopwords_sentence_multi.append(w)
        fdist1 = nltk.FreqDist(without_stopwords_sentence_multi)
        
        trigram_words_multi = nltk.FreqDist(nltk.trigrams(without_stopwords_sentence_multi))
        
        trigram_count_multi = trigram_words_multi.most_common(10)

        #common.plot()
        df_trigram_multi = pd.DataFrame(trigram_count_multi)
        df_trigram_multi.columns = ['Trigram Word', 'Counts']
        #st.subheader("Showing 50 Words Count")
        st.subheader("Showing Top 10 Trigram Words")
        df_trigram_multi.plot()
        trigram_sns_multi = sns.barplot(x='Trigram Word',y='Counts',data=df_trigram_multi)
        plt.xticks(rotation=70)
        #sns.lineplot(x='word',y='counts',data=df)
        st.pyplot()
        #st.image(graph)
        st.bar_chart(data=df_trigram_multi, x="Trigram Word", y="Counts",use_container_width=True)
    
elif option ==  "Word Cloud" and choice == 'Multi PDF':
    if st.button("Click to Submit", key="35"):
        merged_file = "file.pdf"
        fileReader_multi = pdfs.PdfFileReader(merged_file)
        pages = fileReader_multi.numPages
        st.caption("Pages of The File")
        st.caption(pages) 
        
        #fileReader_multi = pdfs.PdfFileReader(merged_file)
        num_pages = fileReader_multi.numPages
        count = 0
        text_multi = ""
        while count < num_pages:
            pageObj = fileReader_multi.getPage(count)
            count +=1
            text_multi += pageObj.extractText()
            stop_words_list = stop_words_NLP and custom_stop_words
            word_tokens = word_tokenize(text_multi)
            without_stopwords_sentence_multi = []
        for w in word_tokens:
            if w not in stop_words_list:
                without_stopwords_sentence_multi.append(w)
        
        wc = WordCloud(
        background_color = 'black',
        stopwords = stop_words_list,
        height = 700,
        width = 1000
        )
        i = wc.generate(str( without_stopwords_sentence_multi))
        #plt.imshow(i)
        fig, ax = plt.subplots()
        ax.imshow(i, interpolation='bilinear')
        ax.axis("off")
        st.pyplot(fig)
    
    
    
        
            
else:
  pass            
         
             
     
            
         
        
            
            
            
     
 

    

    