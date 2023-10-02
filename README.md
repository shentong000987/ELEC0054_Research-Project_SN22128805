This is the project for ELEC0054 IMLS Msc Research Project 22-23
Project Title: Companion Digital Assistant using Natural Language Processing

The aim of this project is to develop a private chatbot working like some other world famous human-interact machine learning model, such as Chatgpt, but could read personal data saved locally in advance and provide appropriate responds with those personal data.

The whole system consists with 3 parts - chatbot, database, database_interact model

To build the chatbot, a pretrained large language model (LLM) - Falcon LLM_7B is downloaded and included in this project. Falcon LLM_7B is a causal decoder-only model which has been finetuned on a mixture of chat/instruct datasets to do the NLP task.

The database is built by MySQL to store some personal information of a few people locally

database_interact works like a information processing centre. It uses pymysql package to search and insert data to database and appends perossnal information as LLM prompt to chatbot. Also, its provides input and output channel to the user.

To run this model, please ensure your working place has enough RAM and disk space to avoid problem. There is also a alternative online version of this project published on Google Colab written in Jupyter notebook which can run on the GPU freely provided by Google. You can access to it by the following link:
https://colab.research.google.com/drive/1oPiyNsVfXPQ3e06WvCtksk49VcBhDeou?usp=sharing

avoid RAM and disk space problem.