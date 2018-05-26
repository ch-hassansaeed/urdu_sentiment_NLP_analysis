from urdu_sentiment_NLP_analysis_lib import get_urdu_sentiment
urdu_input_sentence="""
آپ جیسا اچھا بندہ نہیں دیکھا میں نے   
"""
urdu_sentiment_output=get_urdu_sentiment(urdu_input_sentence)
print(urdu_sentiment_output)
