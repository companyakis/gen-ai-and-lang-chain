import google.generativeai as gemini

gemini.configure(api_key="string_your_key")

model = gemini.GenerativeModel("gemini-pro")

first_prompt = " Who is the founder of Turkish Republic? And I have another question: Can you translate this proverb into Turkish? The proverb: 'A rolling stone gathers no moss'"

response = model.generate_content(first_prompt)

print(response.text) 

"""
**Founder of the Turkish Republic:**

* Mustafa Kemal Atatürk

**Translation of the proverb "A rolling stone gathers no moss" into Turkish:**

* Yuvarlanan taş yosun tutmaz.
      
"""
