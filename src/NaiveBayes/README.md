# Naive Bayes TWSS Classifier

Uses a Naive Bayes classifier to detect TWSS jokes

## Running

Simply run

```
python nbTWSS.py
```

## Results

Training and Testing Data:

| | TWSS (+) | FML (-) | TFLN (-) | Brown (-) | Total (-) |
| --- | --- | --- | --- | --- | --- |
| Training | 2000 | 666 | 666 | 666 | 1998 |
| Testing | 224 | 738 | 734 | 1584 | 3056 |

Precision: 30.43 %

Recall: 88.84 %

F1 Score: 0.4533
