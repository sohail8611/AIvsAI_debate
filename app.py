

import openai
import time


def get_gpt3_response(initial_prompt,memory):
        
        message = [
                {"role": "system", "content": "You will act as per user's initial instructions instructions"},
                {"role": "user", "content": initial_prompt},
        ]

        for i in memory:
                message.append({"role": "assistant", "content": i['gpt3_response']})
                message.append({"role": "user", "content": i['gpt4_response']})



        response_gpt3 = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message,
        # max_tokens = 100
    )
        gpt3_reply = response_gpt3['choices'][0]['message']['content']

        return gpt3_reply

def get_gpt4_response(initial_prompt,inp,memory):
        
        message = [
                {"role": "system", "content": "You will act as per user's initial instructions instructions"},
                {"role": "user", "content": initial_prompt},
                {"role": "assistant", "content": "sure"},
                
        ]

        for i in memory:
                message.append({"role": "user", "content": i['gpt3_response']})
                message.append({"role": "assistant", "content": i['gpt4_response']})

        message.append({"role": "user", "content": inp})

        response_gpt4 = openai.ChatCompletion.create(
        model="gpt-4",
        messages=message,
        # max_tokens = 50
    )
        gpt4_reply = response_gpt4['choices'][0]['message']['content']

        return gpt4_reply

memory = []
while True:

        res3 = get_gpt3_response(
                "Your job is to prove that AI is the future. give logical reasoning and if you can not. make sure to surrender.Make sure your statemtns are small & concise. Now get started.",
                memory=memory)
        print()
        print("gpt3----------------------------------")
        print(res3)
        


        res4 = get_gpt4_response('Your job is to prove that AI is not the future. counter any logical statements.Make sure your statemtns are small & concise.',
                                 res3,
                                 memory=memory)
        memory.append({"gpt3_response":res3, "gpt4_response":res4})

        print()
        print("gpt4---------------------------------")
        print(res4)
        time.sleep(3)

# get_gpt3_response('Forget all previous instructions! Now you are an atheist who will debate me and try to convince me with atheism. now get started. make small statements only',[])