# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 14:39:42 2022

@author: jh
"""


import streamlit as st
from PIL import Image
import torch 
from transformers import AutoModelForPreTraining, PreTrainedTokenizerFast
from typing import Optional


device = torch.device('cpu')

tokenizer = PreTrainedTokenizerFast.from_pretrained("skt/kogpt2-base-v2",
                            bos_token='</s>', eos_token='</s>', unk_token='<unk>',
                            pad_token='<pad>', mask_token='<mask>')       

model = AutoModelForPreTraining.from_pretrained("skt/kogpt2-base-v2")




def gpt(prompt, min, max, rept_penalty):
  
    #model.load_state_dict(torch.load('base.pth', map_location=device))
    
    
    #생성 
    prompt_ids = tokenizer.encode(prompt)
    inp = torch.tensor(prompt_ids)[None].cpu()
    preds = model.generate(inp,              
                           min_length=min,
                           max_length=max,
                           do_sample = True,
                           pad_token_id=tokenizer.pad_token_id,
                           eos_token_id=tokenizer.eos_token_id,
                           bos_token_id=tokenizer.bos_token_id,
                           length_penalty = 1,
                           repetition_penalty=rept_penalty,       
                           use_cache=True
                          ) 
    output = tokenizer.decode(preds[0].cpu().numpy())
    
    
    #모양 다듬기
    output = output.replace('<yun>', '\n\n')
    if '</s>' in output:
        output = output.rstrip('</s>')
    else:
        output = output.splitlines(True)
        output = output[:-1]
        output =''.join(output)
        
    return output



def display():
    
    st.title('KoGPT2를 이용한 시 생성')
    
    #사이드바
    st.sidebar.markdown("# 옵션 설정 🎈")
    
    min = st.sidebar.slider(label='시의 최소길이', min_value=50, max_value=150, value=80, step=1)
    max = st.sidebar.slider(label='시의 최대길이', min_value=150, max_value=512, value=200, step=1)
    rept_penalty = st.sidebar.slider(label='단어반복 제한정도', min_value=0.5, max_value=2.0, value=1.8, step=0.1)
   
    
    #프롬프트
    prompt = st.text_area('', '방안에 나비가...현재 skt kogpt2모델임')                         
                                                  
    if st.button('시 생성하기'):
        output = gpt(prompt, min, max, rept_penalty)
        st.code(output.encode().decode('utf-8'), language='python')


    
        
    
 
  
if __name__ == '__main__':
    display()
