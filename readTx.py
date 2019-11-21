import os
import glob

def readTx():

    cardio_dir = glob.glob('/Users/shreehari/Documents/Notes/ACA/MastersProj/Cardio/*.txt')
    phy_list = []
    for file in cardio_dir:
        with open(file, 'r') as f:
            content = f.readlines()
            # you may also want to remove whitespace characters like `\n` at the end of each line
            content = [x.strip() for x in content]
            phy_list = phy_list + content

    return phy_list