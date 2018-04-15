import os
from utility import *
import time

from pythonosc import udp_client
import string
from classes.BaseThread import BaseThread
from classes.GifScraper import GifScraper
from classes.GoogleScraper import GoogleScraper
from classes.TextToSpeech import TextToSpeech

from pygame import mixer
# import spacy_nlp

ROBOT_SPEECH_ECHO_DELAY = 10
N_ECHO_WALKS = 0

# nlp_args = spacy_nlp.prepare_nlp(raw_text)

def scrape_line(query, dir_name):
    os.mkdir(dir_name)
    query = query.strip().lower()
    GoogleScraper(30).scrape(query, dir_name)

def run(client=None):
    mixer.init(channels=1, frequency=12100)
    text = input("Enter your text: ")

    dir_str = make_url_str(text)
    dir_name = "../Image/"+dir_str

    if os.path.exists(dir_name):
        print('path exists',text, dir_str)
        client.send_message("/swap", text+":"+dir_str)

    else:
        scrape_line(text, dir_name)
        if client:
            client.send_message("/swap", text+":"+dir_str)

        # TextToSpeech(mixer).play(line)
        # BaseThread(target=robot_speech_echoes, args=[speech_echoes_arr]).start()
    #

    #         TextToSpeech(mixer).play(line)
    # doc = nlp_args[0](raw_text)
    # lines = list(doc.sents)
    #
    # for line in lines:
    #
    #     line = line.text.rstrip(string.punctuation).strip()
    #     speech_echoes_arr = spacy_nlp.sentencewalk(line, *nlp_args, N_ECHO_WALKS)
    #
    #     s_time = N_ECHO_WALKS*ROBOT_SPEECH_ECHO_DELAY+ROBOT_SPEECH_ECHO_DELAY+5
    #
    #     if os.path.exists(dir_name):
    #         client.send_message("/swap", line+":"+dir_str)
    #         # BaseThread(target=robot_speech_echoes, args=[speech_echoes_arr]).start()
    #         s_time = N_ECHO_WALKS*ROBOT_SPEECH_ECHO_DELAY+ROBOT_SPEECH_ECHO_DELAY+5
    #
    #     else:
    #         scrape_line(line, dir_name)
    #         if client:
    #             client.send_message("/swap", line+":"+dir_str)
    #         TextToSpeech(mixer).play(line)
    #         # BaseThread(target=robot_speech_echoes, args=[speech_echoes_arr]).start()
    #
    #     time.sleep(s_time)
