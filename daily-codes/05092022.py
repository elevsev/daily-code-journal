import pandas as pd
import json
import glob

def load_data(file):
    with open(file=file, mode="r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def write_data(file, data):
    with open(file=file, mode="w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    return data

trc_file = "/Users/Kerryn/daily-code-journal/daily-codes/DATA/trc_dn.json"

trc = load_data(file=trc_file)

print(trc.keys())

names, descriptions = trc['names'], trc['descriptions']

print(descriptions[0])