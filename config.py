import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 配置变量
api_key = os.getenv('API_KEY')
base_url = "https://open.bigmodel.cn/api/paas/v4/"
chat_model = "glm-4-flash"
emb_model = "embedding-3"