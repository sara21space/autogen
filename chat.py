import os
import asyncio
from autogen_ext.models.openai import OpenAIChatCompletionClient, AzureOpenAIChatCompletionClient
from autogen_core.models import ModelInfo, ModelFamily, SystemMessage, UserMessage, AssistantMessage

async def main():
    # model_client_openai = OpenAIChatCompletionClient(model="mathstral-7b-v0.1")
    # model_client_azure = AzureOpenAIChatCompletionClient(model="mathstral-7b-v0.1")
    model_client_lmstudoi = OpenAIChatCompletionClient(
        model="mathstral-7b-v0.1",
        base_url=os.environ["LMSTUDIO_BASE_URL"],
        model_info=ModelInfo(
            vision=False,
            function_calling=False,
            json_output=False,
            family=ModelFamily.UNKNOWN
        )
    )
    
    model_client_ollama = OpenAIChatCompletionClient(
        model="llama3.2",
        base_url=os.environ["OLLAMA_BASE_URL"],
        model_info=ModelInfo(
            vision=False,
            function_calling=False,
            json_output=False,
            family=ModelFamily.UNKNOWN
        )
    ) 


    #preparing the message
    msg = []
    msg.append(SystemMessage(content="you are language model (LLM), tell your model name as first respond."))

    #list the available models
    while True:
        print("Available models: ")
        print("1. Llama")
        print("2. LMStudio")
        input_model = input("Choose the model: ")
        if input_model == "1":
            model_client = model_client_ollama
            break
        elif input_model == "2":
            model_client = model_client_lmstudoi
            break
        else:
            print("Invalid model")
    

    #chat loop
    while True:
        user_input = input("You: ")
        if user_input == "exit":
            break
        
        msg.append(UserMessage(content=user_input, source="user"))  
        response = await model_client.create(messages=msg)

        print(f"{response.content}\n{response.usage}")
        msg.append(AssistantMessage(content=response.content, source="assistant"))

asyncio.run(main())