
# MIDITools

Miditools is an easy to use tool to help in the process of manually reviewing MIDI files for Tesla coil concerts of the [Clubelek](https://www.clubelek.fr).

## Index
- [Overview](#-overview)
- [Key Features](#️-key-features)
- [Requirements](#-requirements)
- [Installation and usage](#️-installation-and-usage)
- [License](#license)

## 🔍 Overview
At INSA, the Clubelek is a technical association primarily known for their Tesla coil shows, notably at the student festival _Les 24H de l’INSA_. In order to play music, the machines need to be fed a special signal and thus adding new music to the playlists is more complicated than using common sound file formats (such as .mp3, .ogg or .wav).

Do do so the association uses the MIDI format (Musical In- strument Digital Interface). These files are manually reviewed to make sure they fit within the requirements imposed by the Tesla coils, such as the number of notes that can be played simultaneously for example.

## 🛠️ Key Features

| Feature | Description |
| --- | --- |
| Merge | Takes two or more MIDI files and returns a single file containing all note events, hence creating a medley out of songs, while still respecting each song’s tempo and time signature |
| Verify | Verifies if a given MIDI file respects all constraints specific to the Clubelek's Tesla coils and indicates where are the invalid events (with their time and channel) |
| Generate configurations | Generates for a given MIDI file a list of SysEx events handling channel assignments and other common Tesla coil parameters. The events are returned in the [Syfoh](https://github.com/MMMZZZZ/Syfoh) format in order to be compatible with the Clubelek’s music player software. |


## 📦 Requirements
- [Python 3.8+](https://www.python.org/downloads/)
- [tkinter](https://docs.python.org/3/library/tkinter.html)
- [mido 1.3.3](https://mido.readthedocs.io/en/stable/installing.html)
- [packaging](https://pypi.org/project/packaging/)

## ⚙️ Installation and usage

1. Clone the repository:
    ```bash
    git clone https://github.com/clement-marty/miditools.git
    ```

2. (optional) Create a virtual Python environment
    ```bash
    python -m venv env
    source env/bin/activate
    ```

3. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```

4. Start the application:
    ```bash
    python main.py
    ```

## License
This project  is copyright (c) 2026 Clément MARTY. See the [LICENSE](LICENSE) file for more details.

This project also uses and contains the [Syfoh](https://github.com/MMMZZZZ/Syfoh) library, which is licensed under the MPL-2.0 License. See the [Syfoh LICENSE](Syfoh/LICENSE.txt).

