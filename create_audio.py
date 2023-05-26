from gtts import gTTS
from subprocess import call 

def create_audio(audio):
    tts = gTTS(audio, lang='pt-br')
    tts.save('audios/teste.mp3')

    
create_audio('Olá, isso é um teste.')
