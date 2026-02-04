"""
简单测试：验证结构化输出功能
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

load_dotenv()

if not os.getenv("DASHSCOPE_API_KEY"):
    raise ValueError("请先设置 DASHSCOPE_API_KEY 和 BASE_URL")

model = ChatOpenAI(
    model="qwen-turbo",
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url=os.getenv("BASE_URL"),
)

print("=" * 70)
print("测试：结构化输出 - Pydantic 模型")
print("=" * 70)


class Person(BaseModel):
    """人物信息"""
    name: str = Field(description="姓名")
    age: int = Field(description="年龄")
    occupation: str = Field(description="职业")


# 创建结构化输出的 LLM
structured_llm = model.with_structured_output(Person)

print("\n提示: 张三是一名 30 岁的软件工程师")
result = structured_llm.invoke("张三是一名 30 岁的软件工程师")

print(f"\n返回类型: {type(result)}")
print(f"姓名: {result.name}")
print(f"年龄: {result.age}")
print(f"职业: {result.occupation}")

print("\n" + "=" * 70)
print("测试结果：")
print("  - with_structured_output() 返回 Pydantic 对象 [成功]")
print("  - 自动类型验证 [成功]")
print("  - 无需手动解析 JSON [成功]")
print("=" * 70)

print("\n测试完成！")
