# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 16:13:25 2022

@author: jh
"""

import streamlit as st
from PIL import Image
from pororo import Pororo

def main():
    st.title('KoGPT2를 이용한 시 생성')
    st.subheader('이미지 캡셔닝')
    

    
    
    
    
#이미지    
    #img_upload = st.file_uploader('이미지 찾아보기')
    img_url = st.text_input('이미지 url 붙여넣기')
    
    show_img = st.empty()
     
    #업로드
    '''
    if img_upload:
        bytes_img = img_upload.getvalue()
        show_img.image(img_upload)
    '''
    
    #url 
    if img_url != '':
        show_img.image(img_url)    
           
        
#캡셔닝
    caption = Pororo(task='caption', lang='ko')
    st.text_input(caption)


    #페이지
    st.sidebar.markdown("# 옵션 설정 🎈") 
    
    
        
  
    
  
if __name__ == '__main__':
    main()