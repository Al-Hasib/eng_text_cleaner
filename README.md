# Text Cleaning of English Language Python Package

Text Cleaning is a common preprocessing technique for almost all NLP task. Mainly I have designed the package for Text Classification Task. Also You can use it for other NLP task also. You are welcome to contribute the package.

**Install the package**

```bash
pip install eng_text_cleaner
```

There has number of methods to clean the text such as removing emoji, punctuation, html_tags, urls, characters not words or digits or underscore, digits, stopwords, spell correction, lemmatize the words. One Method named clean text will apply all the methods to clean the text at a glance. Let's explore the simple package.
```python
from eng_text_cleaner import preprocessing 
```
Start by removing punctuation
```python
text = "Neither too small nor too large, and nice resolution at a good price."
# create textcleaner instance
textcleaner = preprocessing.TextCleaner()
# remove punctuation
textcleaner.remove_punctuation(text)
```
Output:
```bash
Neither too small nor too large and nice resolution at a good price
```
For Clean the text totally
```python
# fully clean the text
textcleaner.clean_text(text)
```
Output:
```bash
neither small large nice resolution good price
```

Author:
* **Md Abdullah Al Hasib**
