# Project Name

Small experiment project to see how hard it'd really be to make a basic AI vtuber. Turns out it's not that hard.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)

## Installation

Download the repo
Install [Python](https://www.python.org/downloads/)

Install [Vtube Studio](https://store.steampowered.com/app/1325860/VTube_Studio/)

Install [Voicemeeter](https://vb-audio.com/Voicemeeter/)

Using CMD, navigate to the folder and input "pip install -r requirements.txt"

## Usage

There's a couple of things you have to modify on a user-per-user basis to make it work:
- Open up config.py with python IDLE/VSC/...
- Follow the comments there. Should be self explanatory.

If you're not using OpenAI, everything you need to change is in chat.py, Otherwise just head into config and change the API key.

If you're using VTube studio:
- Go to its microphone config and change it to the virtual cable you selected in config.py
- Go to the model options and change MouthOpen's input to "VoiceVolumePlusMouthOpen" 
(Enables lip syncing)

Once that's done, Just run Voicemeeter, VTube studio & main.py
