import voice_assistant as va
import hugging_face as hf
import document_scanner as ds
from dotenv import *
import os
import streamlit as st
import cv2
import numpy as np

#loading API_KEYS
load_dotenv(find_dotenv())
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")


    

    
def main():
    # st.set_page_config(page_title="Artificial Eye", page_icon="6")
    # st.header("Artificial Eye")
    
    # #document scanner
    # st.sidebar.title('Document Scanner')

    
    # uploaded_file = st.sidebar.file_uploader("Upload Image of Document:", type=["png", "jpg"])
    # image = None
    # final = None
    # col1, col2 = st.columns(2)

    # with col1:
    #         st.title('Input')
            # st.image(image, channels='BGR', use_column_width=True)
    # with col2:
    #     st.title('Scanned')
    #     # final = scan(image)
    #     # st.image(final, channels='BGR', use_column_width=True)

    # if uploaded_file is not None:

    #     # Convert the file to an opencv image.
    #     file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    #     image = cv2.imdecode(file_bytes, 1)
        
    #     ds.document_scanner(image)

    # try:
    #     # url = "venv\AEYE\yy3.gif"
    #     with open("yy3.gif", "rb") as f:
    #         st.image(f.read(), caption='Sunrise by the mountains')
    # except FileNotFoundError:
    #     st.error("Image file not found. Please check the file path.")

    
    va.voiceCommand()

    
        
        #if input is image
        # uploaded_file2 = st.file_uploader("Choose an img", type=["png", "jpg"])
        
        # if uploaded_file2 is not None:
        #     print(uploaded_file2)
        #     bytes_data = uploaded_file2.getvalue()
        #     with open(uploaded_file2.name, "wb") as file:
        #         file.write(bytes_data)
        #     st.image(uploaded_file2, caption='Uploaded Img',
        #             use_column_width=True)
            
            
            
            
        # uploaded_file2 = None
        


if __name__ == "__main__":
    main()
    