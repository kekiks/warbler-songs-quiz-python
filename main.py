import io
import tkinter as tk
import pygame
import os
import glob
import random
import re
from PIL import Image, ImageTk
from mutagen.mp3 import MP3
from mutagen.id3 import ID3

image_shown = False


def repeat_bird(mp3_file_path):
    pygame.mixer.stop()
    quiz_bird(mp3_file_path)

def reveal_bird(bird_image, mp3_file_path):
    global image_shown
    image_shown = True
    audiofile = MP3(mp3_file_path)
    metadata = audiofile.tags.get("COMM::ENG")[0]
    metadata_list = [item.strip() for item in metadata.split(";")]
    latin_name = metadata_list[0]
    recording_place = metadata_list[1]
    recording_artist = metadata_list[2]
    recording_id = metadata_list[3]
    label_image.configure(image = bird_image)
    bird_name = (re.search(r'/([^/0-9]+)\s*\d', mp3_file_path))
    label_common_name.configure(text = f"{bird_name.group(1).strip()}")
    label_latin_name.configure(text = latin_name)
    label_credits.config(text = f"Recorded in {recording_place} by {recording_artist}. Source: Macaulay Library")

def next_bird():
    pygame.mixer.stop()
    label_common_name.configure(text ="")
    label_latin_name.configure(text = "")
    label_common_name.configure(text = "")
    label_credits.configure(text = "")
    global bird_list
    if len(bird_list) == 0:
        global original_bird_list
        bird_list = original_bird_list
    if len(bird_list) > 0:
        random_bird = random.choice(bird_list)
        bird_list.remove(random_bird)
        print(f"{len(bird_list)} birds left.")
        global image_shown
        image_shown = False
        quiz_bird(random_bird)

def quiz_bird(mp3_file_path):
    global image_shown
    audio = ID3(mp3_file_path)
    picture = None
    for tag in audio.getall("APIC"):
        picture = tag
        break
    if picture:
        # Convert image data to a format PIL can use
        image_data = io.BytesIO(picture.data)
        img = Image.open(image_data)
        # Convert PIL image to Tkinter format
        tk_img = ImageTk.PhotoImage(img)
        width, height = img.size
        blank_img = Image.new('RGBA', (width, height), (0, 0, 0, 0))  # Transparent image
        blank_tk_img = ImageTk.PhotoImage(blank_img)

        if image_shown:
            label_image.configure(image = tk_img)
        else:
            label_image.configure(image = blank_tk_img)

        next_button = tk.Button(text = "Next", command = next_bird)
        next_button.grid(row = 5, column = 2)

        repeat_button = tk.Button(text = "Repeat", command = lambda: repeat_bird(mp3_file_path))
        repeat_button.grid(row = 5, column = 0, pady = 10)

        reveal_button = tk.Button(text = "Reveal", command = lambda: reveal_bird(tk_img, mp3_file_path))
        reveal_button.grid(row = 5, column = 1)

        pygame.init()
        pygame.mixer.init()
        music = pygame.mixer.Sound(mp3_file_path)
        music.play()

    else:
        print("No embedded image found in " + mp3_file_path)


if __name__ == "__main__":

    root = tk.Tk()
    root.title("Birdsong Quiz")

    label_image = tk.Label(root, bg = "#FFFFFF")
    label_image.grid(row = 1, column = 0, columnspan = 3)
    label_common_name = tk.Label(text ="", font = ("Helvetica", 22, "bold"))
    label_common_name.grid(row = 2, column = 0, columnspan = 3, pady = (10, 0))
    label_latin_name = tk.Label(text = "", font = ("Helvetica", 15, "normal"))
    label_latin_name.grid(row = 3, column = 0, columnspan = 3, pady = (0, 12))
    label_credits = tk.Label(font = ("Helvetica", 10, "normal"))
    label_credits.grid(row = 4, column = 0, columnspan = 3, pady = (0, 5))

    root.focus_force()

    original_bird_list = sorted(glob.glob(os.path.join("sounds", '*.mp3')))
#    print("\n".join(original_bird_list))
    print(f"Soundfiles:\n  {"\n  ".join(original_bird_list)}\n{len(original_bird_list)} birds in total.")
    bird_list = original_bird_list.copy()

    bird = random.choice(bird_list)
    quiz_bird(bird)

    root.mainloop()
