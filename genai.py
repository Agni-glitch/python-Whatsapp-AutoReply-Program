import google.generativeai as genai
genai.configure(api_key="AIzaSyDoLkqXU40ajz1t61OLLksDTaGMzPfeVHg")
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 100,
  "response_mime_type": "text/plain",
}
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)
chat_session = model.start_chat(
    history=[
    ]
)
def res(command):
    response = chat_session.send_message(command)
    return response.text