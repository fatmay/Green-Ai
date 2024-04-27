import gradio as gr
import google.generativeai as genai
import apifile
import requests

def get_saglik_bilgisi(cevap_text):
    # ... (Mevcut kodunuz)

    # TTK API'sine istek gönderin.
    ttk_yaniti = requests.get("https://tttk.org.tr/")
    # TTK yanıtını işleyin ve tıbbi bilgi olup olmadığını kontrol edin.
    if ttk_yaniti.status_code == 200:
        ttk_bilgisi = parse_ttk_response(ttk_yaniti.content)
        if ttk_bilgisi:
            return ttk_bilgisi

genai.configure(api_key=apifile.api_key)
model = genai.GenerativeModel('gemini-pro')

def generate(prompt):
    # Kullanıcı girdisini küçük harfe dönüştürün.
    prompt = prompt.lower()

    # Sağlık ile ilgili anahtar kelimeleri arayın.
    saglik_anahtar_kelimeleri = ["sağlık", "hastalık", "tedavi", "belirti", "doktor"]
    for kelime in saglik_anahtar_kelimeleri:
        if kelime in prompt:
            # Kullanıcı sorgusu sağlık ile ilgiliyse, Gemini'yi kullanarak yanıt oluşturun.
            cevap = model.generate_content(prompt)
            return cevap.text

    # Kullanıcı sorgusu sağlık ile ilgili değilse, varsayılan yanıtı döndürün.
    return "Sağlık ile ilgili sorunuzu anlayamadım. Lütfen sorunuzu başka bir şekilde ifade edin."

title =' Yapay Zeka Sağlık Sohbet Botu'
description='Google yapay zekasına sağlık sorularınızı sorabilirsiniz.'

gr.Interface(fn=generate, inputs=["text"], outputs=["text"],
             title=title, description=description,
             # Set theme and launch parameters.
             theme='finlaymacklon/boxy_violet').launch(server_port=8080, share=True)
