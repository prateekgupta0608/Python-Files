## 3. Tokenization ##

tokenized_headlines = []
for item in submissions["headline"]:
    tokenized_headlines.append(item.split(" "))

## 4. Preprocessing ##

punctuation = [",", ":", ";", ".", "'", '"', "’", "?", "/", "-", "+", "&", "(", ")"]
clean_tokenized = []
for item in tokenized_headlines:
    tokens = []
    for token in item:
        token = token.lower()
        for punc in punctuation:
            token = token.replace(punc, "")
        tokens.append(token)
    clean_tokenized.append(tokens)

## 5. Assembling a matrix ##

import numpy as np
unique_tokens = []
single_tokens = []
for tokens in clean_tokenized:
    for token in tokens:
        if token not in single_tokens:
            single_tokens.append(token)
        elif token in single_tokens and token not in unique_tokens:
            unique_tokens.append(token)

counts = pd.DataFrame(0, index=np.arange(len(clean_tokenized)), columns=unique_tokens)

## 6. Counting tokens ##

# clean_tokenized and counts have been loaded in.
for i, item in enumerate(clean_tokenized):
    for token in item:
        if token in unique_tokens:
            counts.iloc[i][token] += 1

## 7. Removing extraneous columns ##

# clean_tokenized and counts have been loaded in.
word_counts = counts.sum(axis=0)

counts = counts.loc[:,(word_counts >= 5) & (word_counts <= 100)]
print(counts.shape)

## 9. Making predictions ##

from sklearn.linear_model import LinearRegression

clf = LinearRegression()
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)

## 10. Calculating error ##

mse = sum((y_test - predictions) ** 2) / len(predictions)