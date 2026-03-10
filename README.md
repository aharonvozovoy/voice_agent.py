# ​📄 README.md (проект "Voice Agency AI")
​Voice Agency AI: Digital Twin Agent
​Интеллектуальная система для автоматизации звонков в Telegram. Проект представляет собой «цифрового двойника» (Ахарона), который может принимать звонки, понимать человеческую речь и отвечать клонированным голосом в реальном времени.
​🛠 Стек технологий
​Мозг: Gemini 1.5 Flash (через Google AI Studio)
​Голос (TTS): ElevenLabs API (клонированный голос Ахарона)
​Слух (STT): OpenAI Whisper API
​Транспорт: Pyrogram + PyTgCalls (WebRTC)
​Хостинг: Render.com
​🚀 Быстрый запуск
​1. Подготовка окружения
​Установите необходимые системные зависимости (актуально для Ubuntu/Render):
apt-get update && apt-get install -y ffmpeg libopus-dev
