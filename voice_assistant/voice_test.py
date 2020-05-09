# Программа проговаривает то что ты написал

import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', 'ru') 

# Попробовать установить предпочтительный голос
for voice in voices:
    if voice.name == 'Alyona (Russian) SAPI5':
        engine.setProperty('voice', voice.id)

engine.say('Привет, мир! Какой прекрасный сегодня день!')

engine.runAndWait()