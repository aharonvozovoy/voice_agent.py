import asyncio
import os
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls.types import AudioPiped, AudioVideoPiped
from elevenlabs.client import ElevenLabs
import google.generativeai as genai
import openai # Для Whisper STT

# Инициализация API
el_client = ElevenLabs(api_key=os.getenv("ELEVEN_API_KEY"))
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Client("agency_session", api_id=os.getenv("TG_ID"), api_hash=os.getenv("TG_HASH"))
call_py = PyTgCalls(app)

async def transcribe_audio(file_path):
    """Превращаем голос собеседника в текст (STT)"""
    with open(file_path, "rb") as audio_file:
        transcript = openai.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file,
            language="ru"
        )
    return transcript.text

async def get_my_response(text):
    """Мой мыслительный процесс"""
    system_instruction = "Ты — цифровой двойник Ахарона, проект-менеджера и инженера. Говори кратко."
    response = await model.generate_content_async(f"{system_instruction}\nСобеседник: {text}")
    return response.text

async def talk_with_my_voice(text, chat_id):
    """Генерация твоего голоса и отправка в звонок"""
    audio = el_client.generate(
        text=text,
        voice=os.getenv("VOICE_ID"),
        model="eleven_multilingual_v2"
    )
    temp_file = f"ans_{chat_id}.mp3"
    with open(temp_file, "wb") as f:
        for chunk in audio: f.write(chunk)
    
    # Трансляция в звонок
    await call_py.change_stream(chat_id, AudioPiped(temp_file))

@call_py.on_stream_end()
async def on_stream_end(client, update):
    """Когда я закончил говорить, начинаем слушать (логика переключения)"""
    # Здесь можно добавить логику записи чанка аудио собеседника
    pass

async def main():
    await app.start()
    await call_py.start()
    print("Агент Агентства на связи и готов к звонкам.")
    await asyncio.Event().wait()

if __name__ == "__main__":
    app.run(main())
