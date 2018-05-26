# urdu_sentiment_NLP_analysis
python project which will take input as urdu sentence and give output as it "positive" or "negitive" sentiment sentence.
Main Demo File name as input.py (but urdu_sentiment_NLP_analysis_lib.py should put in your project folder)

```
from urdu_sentiment_NLP_analysis_lib import get_urdu_sentiment
urdu_input_sentence="""
آپ جیسا اچھا بندہ نہیں دیکھا میں نے   
"""
urdu_sentiment_output=get_urdu_sentiment(urdu_input_sentence)
print(urdu_sentiment_output)
```

**---------------------------------------
Output:postive/nautral/non-sentimental
---------------------------------------**
```
another exmple 
urdu_input_sentence="""
آپ بہت باتمیز انسان ہو    
"""
```
**---------------------------------------
Output:negative
---------------------------------------**

**Note:** This is Possible with negative and positive keywrod list in urdu_sentiment_NLP_analysis_lib.py
this is depend on your requirement if your recomend treat any other word as postive then you can add in negative and positive keywrod list array.and it show sentimat result wrt to your keywrods.
Speical Thanks to Mr.awaisathar whcih has list of urdu keywrod in his other html/javascript project(https://github.com/awaisathar/urdu-sentiment-lexicon)
