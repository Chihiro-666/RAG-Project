from openai import OpenAI
#1.获取client对象，OpenAI类对象
client = OpenAI(
    base_url="https://ws-g7m52sorzrau8189.cn-beijing.maas.aliyuncs.com/compatible-mode/v1"
)

#2.调用模型
response = client.chat.completions.create(
    model="qwen3.8-max",
    messages=[
        {"role": "user", "content": "你是一个Python编程专家，并且不说废话"},
        {"role": "assistant", "content": "好的，我是编程专家，并且话不多"},
        {"role": "user", "content": "输出1-10的数字，用Python语言代码实现"},
    ],
    stream = True
)

#3.处理结果
for chunk in response:
    # 先判断choices不为空，再取0号元素，再判断content不为None
    if chunk.choices:
        if chunk.choices[0].delta.content is not None:
            print(
                chunk.choices[0].delta.content,
                end=" ",  #每段以空格分隔；
                flush=True  #立刻刷新缓冲区
            )
# for chunk in response:
#     print(
#         chunk.choices[0].delta.content,
#         end=" ",  #每段以空格分隔；
#         flush=True  #立刻刷新缓冲区
#     )