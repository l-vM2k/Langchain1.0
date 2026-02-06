import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_openai import ChatOpenAI

load_dotenv()


model = ChatOpenAI(
        model="qwen-turbo",
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        base_url=os.getenv("BASE_URL"),
    )

# 非流式(一次性返回完整结果)：
# response = model.invoke("你好！请用一句话介绍什么是人工智能。")

#流式（流式）：
res = model.stream("你是谁？你能做什么")
#print(response.content)
for chunk in res:
    print(chunk.content, end="", flush=True)