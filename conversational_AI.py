import os
from dotenv import load_dotenv

from langchain_community.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))
memory = ConversationBufferMemory()

chain = ConversationChain(
    llm=llm,
    memory=memory
)

while True:
    input_text = input('You: ')
    if input_text.lower() in ['exit', 'quit']:
        break
    result = chain.invoke(input_text)
    print(f'AI: {result["response"]}')
