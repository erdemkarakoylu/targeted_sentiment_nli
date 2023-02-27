### Targeted  Sentiment Using Natural Language Inference
The goal of this project is the development of a Deep Learning Model (DLM) to identify sentiment expressed toward a target entity embedded in a piece of text. The backbone of the DLM is a Huggingface Model Natural Language Inference Model trained for detecting entailment between two subsequent sentences
Inputs the model expects therefore include a piece of text or a tweet, and the target entity. 
Training sets include ACL-14, newsMTSC and SentFin. These feature ternary sentiment polarity; negative, neutral, positive.
All 3 data sets are loaded and cleaned such  that the cleane data contains five  columns: Context (str), Target(str), Polarity (int.)