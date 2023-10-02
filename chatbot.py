from langchain import HuggingFacePipeline
from transformers import AutoTokenizer, pipeline
import torch

from langchain import PromptTemplate,  LLMChain

def chatbot_interact():

    # load falcon=7b-instruct model
    model = "tiiuae/falcon-7b-instruct" #tiiuae/falcon-40b-instruct

    tokenizer = AutoTokenizer.from_pretrained(model)

    pipeline = pipeline(
        "text-generation", #task
        model=model,
        tokenizer=tokenizer,
        torch_dtype=torch.bfloat16,
        trust_remote_code=True,
        device_map="auto",
        max_length=200,
        do_sample=True,
        top_k=10,
        num_return_sequences=1,
        eos_token_id=tokenizer.eos_token_id
    )

    llm = HuggingFacePipeline(pipeline = pipeline, model_kwargs = {'temperature':0})

    # 

    template = """
    Question: {question}
    Answer:"""
    prompt = PromptTemplate(template=template, input_variables=["question"])

    llm_chain = LLMChain(prompt=prompt, llm=llm)


    #key_word will be the key word sent into database_interact file for searching corresponding fun Fact of the person later
    #fun_fact is the fun fact returned from database_interact file after searching in database. Here we input it as the pretended result
    #the chat bot will be always in mode "on" in this loop 
    while(1):

        #test the 3 person
        for x in range(3):
            user_name = input("Hi! What is your name? \n")
            #test the 4 loops for each person - Alice, Bob, Charlic
            for x in range(4):
                question_initial = input("Hi! What do you want to ask me?\n")
                key_word = input("Can u summarize with a key word?\n")
                fun_fact = input("The is the pretended fun_fact result input by the user. \n")

                #This information gets appended to the original LLM prompt
                question = user_name + question_initial + key_word + fun_fact

                answer = llm_chain.run(question)
                #feed into llm machine waiting for response
                print("Falcon-7B Chat Bot is answering your question: " + answer)

                #ask if the answer should be also insert into database as an fun fact for future use
                choice = input("If you want to save the answer to database for future use (Y/N)? \n")
                if choice == 'Y':
                    print('Answer has been inserted to database')

if __name__ == "__main__" :
    chatbot_interact()
                