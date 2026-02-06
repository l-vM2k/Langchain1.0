from langchain_community.embeddings import DashScopeEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()
print("API Key 是否加载:", bool(os.getenv("DASHSCOPE_API_KEY")))

embeddings = DashScopeEmbeddings(
    model="text-embedding-v3"
)

re = embeddings.embed_query("我喜欢你")
print(re)

re2 = embeddings.embed_documents(["我喜欢你", "原神启动"])

print(re2)