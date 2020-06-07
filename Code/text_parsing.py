import numpy as np
import string

def clean_text(path):
    """
    Input: path to .txt file containing the data
    Output: list of lists, each row containing a data point of the form: Steam Id, App Id, Playtime
    """
    # Read File
    with open(path, "r") as f:
        text = f.read()

    # Delete SQL commands
    text = text.replace("INSERT INTO `Games_1` VALUES ", '')

    # Split by "("
    b = "),"
    lines = [w + ')' for w in text.split(b) if w]

    # Split each line into it's elements
    lines = [l.replace("(", "").split(",") for l in lines]

    # Only keep elements we want: steam_id, app_id, add 1 for pivoting later
    lines = np.array([ [np.int64(l[0]), np.int64(l[1]), 1] for l in lines])

    return lines

if __name__=="__main__":

    path = "/Volumes/Samsung_T5/Data/"
    file_paths = [path+'Games_Txt/seg_{}.txt'.format(letter) for letter in string.ascii_lowercase[:23]]

    for file in file_paths:
        print('Processing Next File...')

        lines = clean_text(file)
        with open('/Volumes/Samsung_T5/Data/Split_lines/{}.npy'.format(name), 'wb') as f:
            np.save(f, lines)
        print('Processed {} !'.format(file))
