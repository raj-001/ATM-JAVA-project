import pyttsx3
import datetime
voiceEngine = pyttsx3.init('sapi5')
voices = voiceEngine.getProperty('voices')
voiceEngine.setProperty('voices', voices[0].id)
print(voices)

def speakAudio(audio):
    voiceEngine.say(audio)
    voiceEngine.runAndWait()
def wishAccordingToTime():
    timeHours = int(datetime.datetime.now().hour)
    if timeHours > 0 and timeHours < 12:
        speakAudio("Good Morning Sir")
    elif timeHours > 12 and timeHours < 16:
        speakAudio("Good Afternoon Sir")
    else:
        speakAudio("Good Evening Sir")
if  __name__ ='__main__':
    wishAccordingToTime()
    askingHelp = "How Can I Help You"
    speakAudio(askingHelp)
    
