from chat_elements import ACRONYMS, EMOTICONS
import pandas as pd
import numpy as np
import random
import json
import copy
import re
from multiprocessing import Pool
from functools import partial
import os
from tqdm.contrib.concurrent import process_map

import nltk

# import spacy
import string
from spellchecker import SpellChecker
from tqdm import tqdm

pd.options.mode.chained_assignment = None
tqdm.pandas()

spell = SpellChecker()

user2tag = {r"@\d+": "John", r"@[a-zA-z]+": "Agent"}


def remove_emojis(text):
    emoji_pattern = re.compile(
        "["
        u"\U0001F600-\U0001F64F"  # smileys
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        "]+",
        flags=re.UNICODE,
    )
    return emoji_pattern.sub(r"", text)


def remove_emoticons(text):
    emoticon_pattern = re.compile(u"(" + u"|".join(k for k in EMOTICONS) + u")")
    return emoticon_pattern.sub(r"", text)


def tag_urls(text):
    url_pattern = re.compile(r"https?://\S+|www\.\S+")
    return url_pattern.sub(r"(URL)", text)


def remove_html_tags(text):
    text = text.replace("&lt;", "<")
    text = text.replace("&gt;", ">")
    html_pattern = re.compile("<.*?>")
    return html_pattern.sub(r"", text)


def convert_acronyms(text):
    new_text = []
    for w in text.split():
        if w.upper() in ACRONYMS:
            new_text.append(ACRONYMS[w.upper()].lower())
        else:
            new_text.append(w)
    return " ".join(new_text)


"""
def correct_spelling(text):
    corrected_text = []
    misspelled_words = spell.unknown(text.split())
    for word in text.split():
        if word in misspelled_words:
            corrected_text.append(spell.correction(word))
        else:
            corrected_text.append(word)
    return " ".join(corrected_text)
"""


def correct_spelling(text):
    split_text = text.split()
    misspelled_words = set(spell.unknown(split_text))

    for i, word in enumerate(split_text):
        if word in misspelled_words:
            split_text[i] = spell.correction(word)

    return " ".join(split_text)


def tag_usernames(text):
    for user in user2tag:
        text = re.sub(user, user2tag[user], text)
    return text


def preprocess(
    in_filename,
    out_filename,
    emojis,
    emoticons,
    urls,
    html_tags,
    acronyms,
    spelling,
    usernames,
    max_workers,
    chunksize,
):
    df = pd.read_csv(in_filename)

    if chunksize == -1:
        if df.shape[0] < 1000:
            chunksize = 1
        else:
            chunksize = min(df.shape[0] // max_workers, 1000)

    if html_tags:
        print("Removing html tags...")
        df["text"] = process_map(
            remove_html_tags, df["text"], max_workers=max_workers, chunksize=chunksize
        )
    if urls:
        print("Tagging URLs...")
        df["text"] = process_map(
            tag_urls, df["text"], max_workers=max_workers, chunksize=chunksize
        )
    if usernames:
        print("Tagging usernames...")
        df["text"] = process_map(
            tag_usernames, df["text"], max_workers=max_workers, chunksize=chunksize
        )
    if acronyms:
        print("Converting acronyms...")
        df["text"] = process_map(
            convert_acronyms, df["text"], max_workers=max_workers, chunksize=chunksize
        )
    if emojis:
        print("Removing emojis...")
        df["text"] = process_map(
            remove_emojis, df["text"], max_workers=max_workers, chunksize=chunksize
        )
    if emoticons:
        print("Removing emoticons...")
        df["text"] = process_map(
            remove_emoticons, df["text"], max_workers=max_workers, chunksize=chunksize
        )
    if spelling:
        print("Spellchecking (it takes a while)...")
        df["text"] = process_map(
            correct_spelling, df["text"], max_workers=max_workers, chunksize=chunksize
        )

    df.to_csv(
        out_filename,
        index=False,
        header=True,
    )
