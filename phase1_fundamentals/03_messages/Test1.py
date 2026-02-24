long_conversation = [
        {"role": "system", "content": "你是助手"},
        {"role": "user", "content": "第1个问题"},
        {"role": "assistant", "content": "第1个回答"},
        {"role": "user", "content": "第2个问题"},
        {"role": "assistant", "content": "第2个回答"},
        {"role": "user", "content": "第3个问题"},
        {"role": "assistant", "content": "第3个回答"},
        {"role": "user", "content": "第4个问题"},
        {"role": "assistant", "content": "第4个回答"},
        {"role": "user", "content": "第5个问题"}]

system_msgs = [m for m in long_conversation if m.get("role") == "system"]
print(system_msgs)

conversation_msgs = [m for m in long_conversation if m.get("role") != "system"]
print(conversation_msgs)

max_messages = 4
recent_msgs = conversation_msgs[-max_messages:]
print(recent_msgs)


for index, context in enumerate(long_conversation, 1) :
        print(f"{index} {context}")

