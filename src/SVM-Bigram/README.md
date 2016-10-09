# Naive Bayes TWSS Classifier

Uses a Naive Bayes classifier to detect TWSS jokes

## Running

Simply run

```
python nbTWSS.py
```

## Results

Number of training examples: 4000 (2000 negative, 2000 positive)

Number of testing examples: 474 (250 negative, 224 positive)

| Features | Precision | Recall | F1 Score |
| --- | --- | --- | --- |
| Only unigram | 94.3 % | 95.98 % | 0.9513 |
| Only bigram | | | |
