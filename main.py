# Primeiro, é necessário instalar um pacote de reconhecimento de voz
# Exemplo:

# pip install SpeechRecognition

# Em seguida, crie um programa em Python para identificar diferentes vozes humanas.

import speech_recognition as sr

# Crie um objeto de reconhecimento de voz
r = sr.Recognizer()

# Obtenha o áudio de uma pessoa
with sr.Microphone() as source:
    print("Fale algo: ")
    audio = r.listen(source)

# Reconheça o áudio
try:
    print("Você disse: " + r.recognize_google(audio))
except:
    print("Não foi possível identificar a voz")