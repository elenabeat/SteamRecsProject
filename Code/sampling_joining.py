import numpy as np
import pandas as pd
import string
import math

def drop_10_sample(data,rate):
    """
    Inputs: data = numpy array with data, of the form [steam_id, app_id, 1]
            rate = float in [0,1], percentage of users to sample
    Output: numpy array of sampled users who rated at least 10 games
    """
    df = pd.DataFrame(data, columns=['steam_id', 'app_id', 'interact'])

    # Drop users that interact with < 10 games
    grouped = df.groupby('steam_id').aggregate(np.count_nonzero)
    keep_ids = grouped[grouped['app_id'] >= 10].index
    df = df[df['steam_id'].isin(keep_ids)]

    #Sample users
    if rate <1:
        steam_ids = df['steam_id'].unique()
        sample_ids = np.random.choice(steam_ids, size= math.floor(len(steam_ids)*rate))
        df = df[df['steam_id'].isin(sample_ids)]
    return df.values

if __name__=="__main__":
    path = "/Volumes/Samsung_T5/Data/"
    file_paths = [path+'Split_lines/seg_{}.npy'.format(letter) for letter in string.ascii_lowercase[:23]]

    data = np.load(file_paths[0])
    data = drop_10_sample(data, rate=0.05)
    print('Completed ', file_paths[0])

    for file in file_paths[1:]:
        d = np.load(file)
        d = drop_10_sample(d, rate=0.05)
        data = np.vstack((data, d))
        print('Completed ', file)

    with open('/Volumes/Samsung_T5/Data/little_array.npy', 'wb') as f:
        np.save(f, data)
