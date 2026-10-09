1.项目结构
P4_RAG项目案例/
├─ app_qa.py               # 智能客服聊天网页
├─ app_file_uploader.py    # 知识库文件上传网页
├─ knowledge_base.py       # 文档切块、向量化、写入 Chroma、去重
├─ rag.py                  # RAG 检索问答链路
├─ vector_stores.py        # Chroma 向量库封装
├─ file_history_store.py   # 自定义会话历史存储
├─ config_data.py          # 全局配置
├─ data/                   # 原始知识文档
├─ chroma_db/              # Chroma 本地向量数据库
├─ chat_history/           # 聊天历史 JSON 文件
└─ md5.text                # 已入库内容的 MD5 记录
2.技术栈
- Python：主要开发语言。
- Streamlit：快速搭建网页聊天 UI 和文件上传页面。
- LangChain：负责提示词模板、文档切分、链式调用、会话历史。
- Chroma：本地向量数据库，存储知识片段和向量。
- 通义千问 DashScope：
  - text-embedding-v4：把文本转成向量。
  - qwen3-max：生成最终回答。
- MD5 + 文件存储：对上传内容去重；聊天记录保存为 JSON 文件。
- RecursiveCharacterTextSplitter：把长文档按段落、句子递归切块。
3.核心流程
(1) 知识库入库
入口：app_file_uploader.py
用户上传 TXT 文件后：
1. 读取文件文本。
2. 计算文本 MD5。
3. 如果 MD5 已存在，说明内容已经处理过，直接跳过。
4. 长文本会被 RecursiveCharacterTextSplitter 切块。
5. 每个文本块附带元数据，例如来源文件名、时间、操作人。
6. 调用通义千问 embedding 模型向量化。
7. 写入 Chroma 向量数据库。
对应代码在 knowledge_base.py:66 的 upload_by_str()。
(2)用户提问
入口：app_qa.py
用户在网页输入问题后，app_qa.py 会调用 rag.py 中的 RAG 链路。
(3)检索增强
核心在 rag.py:41 的 __get_chain()。
用户提问后：
1. 先把用户问题转成向量。
2. 去 Chroma 中检索最相关的知识片段。
3. 把检索到的文档片段格式化成上下文。
4. 组装提示词，包含：
   - 系统要求：根据参考资料回答。
   - 参考资料：知识库检索结果。
   - 历史对话。
   - 当前用户问题。
5. 调用通义千问生成回答。
6. 通过 Streamlit 流式输出到页面。
4. 会话历史
file_history_store.py 实现了自定义的 FileChatMessageHistory。
每个会话通过 session_id 区分，例如 user_001。历史消息会保存到 chat_history/user_001 中，格式是 JSON。
