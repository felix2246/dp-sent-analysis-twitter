# Sentiment Analysis on Twitter using Differential Privacy
 
## Dataset: https://www.kaggle.com/datasets/kazanova/sentiment140 

- ```notebooks/baseline``` contains non-private Sentiment Analyis
- ```notebooks/dp``` contains private Sentiment Analyis
- code in ```notebooks/learning rate``` is used to obtain the learning rate of the LR-Model
- code in ```notebooks/preprocessing``` is used for the preprocessing techniques and for the procesdure of saving the resulting datasets to CSV files.


## How to run:

- Download dataset (test- and train dataset) from https://www.kaggle.com/datasets/kazanova/sentiment140
- run ```notebooks/preprocessing/remove_tweets.pynb``` (set TRAINDATA_PATH to the filepath of the downloaded train dataset)
- run ```notebooks/preprocessing/all-preprocessing.ipynb`` (set TESTDATA_PATH to the filepath of the downloaded test dataset)
- run the desired experiments on the preprocessed datasets (they will be saved in ```notebooks/preprocessing/data/csv_rows```, so you might want to change the FILES_DIRECTORY variable leading towards the folder ```csv_rows```)
