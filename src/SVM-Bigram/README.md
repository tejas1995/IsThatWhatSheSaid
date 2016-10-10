# SVM TWSS Classifier with Bigrams

Uses an SVM classifier with bigram features to detect TWSS jokes

## Running

Simply run

```
python svmTWSS.py
```

## Results

Training and Testing Data:

| | TWSS (+) | FML (-) | TFLN (-) | Brown (-) | Total (-) |
| --- | --- | --- | --- | --- | --- |
| Training | 2000 | 666 | 666 | 666 | 1998 |
| Testing | 224 | 738 | 734 | 1584 | 3056 |

Results:

| Features | Precision | Recall | F1 Score |
| --- | --- | --- | --- |
| Only unigram | 40.48 % | 89.29 % | 0.5571 |
| Only bigram | 39.25 % | 79.91 % | 0.5265 |
