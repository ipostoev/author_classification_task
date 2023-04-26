import os
import re
import pandas as pd

# Load data from files
def get_raw_text_from_dir(path):
    contents = []
    for filename in os.listdir(path):
        if not filename.endswith(".txt"):
            continue
        filepath = path + filename
        with open(filepath) as f:
            contents += f.readlines()
    return ' '.join(contents)

def get_raw_text_from(path):
    contents = []
    if not path.endswith(".txt"):
        return contents
        # read input, remove redudant escape chars
    with open(path) as f:
        contents += f.readlines()
    contents = ' '.join(contents)
    return contents


# Create dataframe
def filter_and_sentenize(raw_text, sentenizer):
    filtered_text = "".join([re.sub('[^А-Яа-я0-9 .,!?:;()]+,-', '', s) for s in raw_text])
    sentences = [s.text.replace('\xa0', '').replace('\n', '') for s in sentenizer(filtered_text)]
    return sentences

def create_datadarame(sentences, label):
    labels = [label for item in range(0, len(sentences))]
    df = pd.DataFrame({
        "sentence": sentences,
        "label": labels,
    })
    return df

# Working with lists
def train_val_sliced(list_to_slice, train_portion, validate_portion):
    assert train_portion >= 0 and train_portion <= 1
    assert train_portion + validate_portion <= 1
    train_amount = int(len(list_to_slice) * train_portion)
    val_amount = int(len(list_to_slice) * validate_portion)
    train = list_to_slice[:train_amount]
    val = list_to_slice[train_amount: train_amount + val_amount]
    test = list_to_slice[train_amount + val_amount:]
    return train, val, test