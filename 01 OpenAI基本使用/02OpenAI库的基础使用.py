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
    ]
)

#3.处理结果
print(response.choices[0].message.content)