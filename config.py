import sounddevice as sd

# Set this to 1 if you want to use Vtube studio for visuals. 0 if you only want the audio. 
USE_VISUAL = 1

# Change this to whatever you want it to be
USER = "TarnishedAccess"

# The voice used for the TTS. Look here for the list of voices: https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts
VOICE = "en-US-AnaNeural"

# Context for the AI. Somewhat dictates how it behaves and processes messages. Change it to something that makes sense.
DEFAULTCONTEXT = "You are an AI companion designed to assist and be helpful. Talk accordingly, speak in english, do not use emote and keep your answers relatively short."

# Press this key to talk (NOT 'q' as that is reserved for quitting the program)
MIC_LETTER = 'g'

# Frame rate and window size. The higher the better but the more taxing it'll be to run.
FRAME_RATE = 30
RESIZE_WIDTH = 320
RESIZE_HEIGHT = 240

# If you want the window to always be on top, set this to 1. 0 otherwise.
TOPMOST = 1

# These are the indices of the devices you want to use.
# One should be your standard audio output (Ex: Speakers)
# The other should be a virtual cable from voicemeeter (Ex: Voicemeeter In 4 (VB-Audio Voicemeeter VAIO), Windows DirectSound)
# IDs and Indices change depending on your setup, so just run this file and look through the resulting list to find the indices you should use.
DEVICE_INDICES = [40, 14]

# Do not touch this.
if __name__ == '__main__':
    print(sd.query_devices())
