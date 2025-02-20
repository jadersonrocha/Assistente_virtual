import pyttsx3
import speech_recognition as sr
import wikipediaapi
import webbrowser
from getopt.geocoders import Nominatim
from geopy.distance import geodesic

# Configuração inicial de voz
engine = pyttsx3.init()
recognizer = sr.Recognizer()
wiki_wiki = wikipediaapi.Wikipedia('pt')

# Função para transforma texto em voz
def falar(texto):
    engine.say(text)
    engine.runAndWait()

# Função para ouvir os comandos de voz
def ouvir():
    with sr.Microphone() as source:
        print('Ouvindo...')
        recognizer.adjust_for_ambient_noise(source) #ajusta o ruido do ambiente
        audio = recognizer.listen(source) #captura o audio
        comando = ''

        try:
            comando = recognizer.recognize_google(audio, language='pt-BR')
            print('Você disse: ' + comando)
            return comando.lower() #converte o comando em minuscula
        except sr.UnknownValueError:
            falar('Desculpe, Não entendi!')
            return None
        except sr.RequestError as e:
            falar('Desculpe, estou com erros no reconhecimento de voz.!')
        return None



#Função para pesquisar no wikipedia
def pesquisar_wikipedia(termo):
    falar('Pesquisando no Wikipedia...{termo}')
    page = wiki_wiki.page(termo)
    if page.exists():
        resumo = page.summary[:500]
        print(resumo)
        falar(resumo)
    else:
        falar('Desculpe, não encontrei nada sobre ' + termo)        


def assistente():
    falar('Olá, em que posso ajudar?')
    while True:
        comando = ouvir_comando()
        if comando:
            if "wikipedia" in comando:
                termo = comando.replace("wikipedia", "").strip()
                pesquisar_wikipedia(termo)            
            else:
                falar("Desculpe, não entendi o comando. Pode repetir?")

#iniciando a assistente virtual.
if __name__ == '__main__':
    assistente()
