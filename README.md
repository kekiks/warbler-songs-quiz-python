# Birdsong Quiz

This app allows you to practice identifying birds by ear using recordings from [Cornell Lab of Ornithology's Macauley Library](https://www.macaulaylibrary.org).

### important requirements

You must own [a set of audio files](https://www.macaulaylibrary.org/product/the-cornell-guide-to-bird-sounds-us-and-canada/) purchased from Cornell Lab of Ornithology's Macauley library.
In the folder with the app, create a folder named "sounds". Copy all audio files (.mp3s) that you want to practice for to this folder. **The app only works for these recordings**.

### how the app works
The app plays a recording randomly selected from all recordings in the `/sounds` folder.
If you want to hear the sound again, click `Repeat`.
Once you think you know you have identified the species that produced the sound, you can click `Reveal` to show a picture of the bird along with some additional information.
When you are ready to go to the next item, click `Next`. After the app has played all the sounds in the `sounds` folder, it will start over again.

Sound files purchased from the Macauley Library contain metadata, including a picture, common name, Latin name, place of recording, and recording artist. The app pulls this information directly from the sound file and presents it on screen. The app therefore only needs the soundfile as input. You can easily make custom quizzes (e.g. Spring migration warblers in your area) by only including a relevant subset of soundfiles in the `sounds/` folder.

![](app-screenshot.png)
