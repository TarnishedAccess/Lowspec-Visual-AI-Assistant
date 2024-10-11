from g4f import models
import asyncio
import edge_tts
import speech_recognition as sr
import chat_bad
import threading
import keyboard
import sounddevice as sd
from pydub import AudioSegment
from vcam import visualization
import os
import numpy as np
from config import USER, VOICE, DEVICE_INDICES, USE_VISUAL, MIC_LETTER

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
OUTPUT_FILE = "output_audio.mp3"

models = [
    "gpt-3.5-turbo",
]

def reset_audio():
    global microphone
    global recognizer

    recognizer = sr.Recognizer()
    recognizer.non_speaking_duration = 0
    recognizer.pause_threshold = 1
    microphone = sr.Microphone()
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)


def play_audio_on_device(samples, samplerate, device_index):
    sd.default.device = device_index
    sd.play(samples, samplerate=samplerate)
    sd.wait()

def play_audio_through_virtual_cables(file_path, device_indices):

    audio = AudioSegment.from_file(file_path)
    audio = audio.set_channels(2)
    samples = np.array(audio.get_array_of_samples())
    
    if audio.channels == 2:
        samples = samples.reshape((-1, 2))
    
    threads = []
    for device_index in device_indices:
        thread = threading.Thread(target=play_audio_on_device, args=(samples, audio.frame_rate, device_index))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

def recognize_speech_from_mic(recognizer, microphone):
    with microphone as source:
        print("Listening")
        audio = recognizer.listen(source, timeout=None, phrase_time_limit=None)
        print("Processing")
    return audio

def generate_audio(text, voice):
    async def text_to_speech_async():
        communicate = edge_tts.Communicate(text, voice, rate="+10%", pitch="+5Hz")
        await communicate.save(OUTPUT_FILE)

    asyncio.run(text_to_speech_async())

chatbot = chat_bad.ChatManager(model=models[0])
reset_audio()
if USE_VISUAL:
    visual_thread = threading.Thread(target=visualization)
    visual_thread.start()

while True:
    print("waiting for key press")
    keyboard.wait(MIC_LETTER)
    print("trigger detected")
    try:
        audio_data = recognize_speech_from_mic(recognizer, microphone)
        user_message = recognizer.recognize_google(audio_data, pfilter=0, language="en-US")
        bot_message = chatbot.get_response(USER, user_message)
        chatbot.update_memory(USER, user_message, bot_message)
        print(bot_message)
        generate_audio(bot_message, VOICE)  
        play_audio_through_virtual_cables(OUTPUT_FILE, DEVICE_INDICES)
        os.remove(OUTPUT_FILE)

    except sr.WaitTimeoutError:
        print("Listening timed out while waiting for phrase to start")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")