import sounddevice as sd
from scipy.io.wavfile import write
import whisper
from gtts import gTTS
import os
from dotenv import load_dotenv
from openai import OpenAI

# ========================
# CARREGAR .ENV (FORÇADO)
# ========================
load_dotenv(dotenv_path="d:/Victor/Projetos/Assistente de Voz/.env")

print("DEBUG arquivos:", os.listdir())
print("DEBUG API carregada com sucesso")

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("API KEY não encontrada. Coloque no arquivo .env")

client = OpenAI(api_key=api_key)

# ========================
# CONFIG
# ========================
fs = 44100
seconds = 5
file_name = "audio.wav"

# ========================
# GRAVAÇÃO
# ========================
print("Gravando...")
audio = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()
write(file_name, fs, audio)
print("Gravação finalizada.")

# ========================
# TRANSCRIÇÃO
# ========================
model = whisper.load_model("small")
result = model.transcribe(file_name, language="pt")
transcription = result["text"].strip()

print("Você disse:", transcription)

if not transcription:
    print("Nada foi captado.")
    exit()

# ========================
# OPENAI
# ========================
response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[{"role": "user", "content": transcription}]
)

reply = response.choices[0].message.content
print("Resposta:", reply)

# ========================
# TEXTO → VOZ
# ========================
tts = gTTS(text=reply, lang="pt")
tts.save("resposta.mp3")

print("Áudio salvo como resposta.mp3")