import csv
import glob
import pandas as pd
import json
import ast

def combine():

    # states abbreviations
    states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
              "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
              "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
              "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
              "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]



    cardio_dict = {}

    # reading all the CSV in Cardio folder
    for file_name in glob.glob('/Users/shreehari/Documents/Notes/ACA/MastersProj/Mpro/CSV/neuro/' + '*.csv'):
        df = pd.read_csv(file_name)
        json1 = df.to_json()
        json_data = json.loads(json1)
        for state in states:
            if state in json_data:
                if state in cardio_dict:
                    cardio_dict[state].extend(ast.literal_eval(json_data[state]['0']))
                else:
                    cardio_dict[state] = []
            else:
                pass

    with open('neuro.json', 'w') as fp:
        json.dump(cardio_dict, fp)


combine()
