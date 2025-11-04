import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# speech_file_path = "speech.wav" 
# model = "playai-tts"
# voice = "Fritz-PlayAI"
# text = "I love building and shipping new features for our users!"
# response_format = "wav"

# response = client.audio.speech.create(
#     model=model,
#     voice=voice,
#     input=text,
#     response_format=response_format
# )

speech_file_path = "arabic_khalid.wav"
response = client.audio.speech.create(
    model="playai-tts-arabic",
    voice="Khalid-PlayAI",#"Nasser-PlayAI",  [Nasser-PlayAI Khalid-PlayAI Amira-PlayAI Ahmad-PlayAI
    input="السلام عليكم! أنا أحب بناء تطبيقات سريعة جدًا",
    response_format="wav",
)
response.write_to_file(speech_file_path)