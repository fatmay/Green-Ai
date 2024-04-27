# import google.generativeai as genai
# import apifile
# genai.configure(api_key=apifile.api_key)
#
# for m in genai.list_models():
#     if 'generateContent' in m.supported_generation_methods:
#         print(m.name)
# model = genai.GenerativeModel('gemini-pro')
#
# response = model.generate_content("esmaray unutama beni sözlerini yaz")
# print(response.text)