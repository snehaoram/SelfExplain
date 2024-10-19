# SelfExplain
- This is course project on implementation of the paper [1], in CS772: Deep Learning with Natural Language Processing in IIT Bombay.
- For various text classification tasks (sentiment analysis, emotion analysis), the model gives prediction along with words or phrases that supports its predicted output.
- Here, interpretability is evaluated in models - BERT, XLMR, Roberta with datasets - GoEmotion, Banking with different fine-tuning setting like LoRa, and quantized version.
- The observations made during the implementation, the interpretability of the models does not affected much with LoRA and quantized fine-tuning. Given a text, the model is giving it's classification result, along with the phrases helping the model for the classification.
- The performance of RoBerta remains at par in the interpretability task.
- The interpretability layer is not ad hoc (add on to the output layer) but an inbuilt with the training architecture, and hence is more efficient.


# References
[1] Rajagopal, D., Balachandran, V., Hovy, E., & Tsvetkov, Y. (2021). Selfexplain: A self-explaining architecture for neural text classifiers. arXiv preprint arXiv:2103.12279.

  
