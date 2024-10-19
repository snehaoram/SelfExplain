# from datasets import load_dataset
import pandas as pd
import numpy as np

# dataset = load_dataset("go_emotions", "raw")

# dataset = pd.DataFrame(dataset['train'])
from sklearn.model_selection import train_test_split

dataset = pd.read_csv("goemtion.tsv", sep='\t')

# dataset['label'] = dataset['sadness']

# for index, row in dataset.iterrows():
#     dataset.loc[index,'label'] = np.argmax(row.iloc[9:])


# data = dataset[["text", "label"]]

train, test = train_test_split(dataset, test_size=0.1, stratify=dataset["label"])


test.to_csv("text.tsv", sep = "\t")
train.to_csv("tran.tsv", sep = "\t")


# print(dataset['label'])



