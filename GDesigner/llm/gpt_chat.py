import aiohttp
from typing import List, Union, Optional
from tenacity import retry, wait_random_exponential, stop_after_attempt
from typing import Dict, Any
from dotenv import load_dotenv
import os

from GDesigner.llm.format import Message
from GDesigner.llm.price import cost_count
from GDesigner.llm.llm import LLM
from GDesigner.llm.llm_registry import LLMRegistry


OPENAI_API_KEYS = ['']
BASE_URL = ''

load_dotenv()
MINE_BASE_URL = os.getenv('BASE_URL')
MINE_API_KEYS = os.getenv('API_KEY')
MINE_BASE_URL = 'https://api.deepseek.com/chat/completions'
MINE_API_KEYS = 'sk-0a3494ee0ae344b8905416f8d0b74053'

@retry(wait=wait_random_exponential(max=100), stop=stop_after_attempt(3))
async def achat(
    model: str,
    msg: List[Dict],):
    request_url = MINE_BASE_URL
    authorization_key = MINE_API_KEYS
    headers = {
        'Content-Type': 'application/json',
        'authorization': f'Bearer {MINE_API_KEYS}' 
    }
    # data = {
    #     "name": model,
    #     "inputs": {
    #         "stream": False,
    #         "msg": repr(msg),
    #     }
    # }

    data = {
        "model": model,  
        "messages": msg,  
        "stream": False
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(request_url, headers=headers ,json=data) as response:
            
            response_data = await response.json()
              # ✅ 解析 DeepSeek API 的返回格式
            choices = response_data.get('choices', [])
            if choices:
                reply = choices[0].get('message', {}).get('content', '')  # ✅ 确保获取到文本内容
            else:
                reply = "API 没有返回有效内容"

            prompt = "".join([item['content'] for item in msg])

            # 这里好像deepseek 计算不了
            # cost_count(prompt, reply, model)

            return reply 

            # prompt = "".join([item['content'] for item in msg])
            # cost_count(prompt,response_data['data'],model)
            # return response_data['data']

@LLMRegistry.register('GPTChat')
class GPTChat(LLM):

    def __init__(self, model_name: str):
        self.model_name = model_name

    async def agen(
        self,
        messages: List[Message],
        max_tokens: Optional[int] = None,
        temperature: Optional[float] = None,
        num_comps: Optional[int] = None,
        ) -> Union[List[str], str]:

        if max_tokens is None:
            max_tokens = self.DEFAULT_MAX_TOKENS
        if temperature is None:
            temperature = self.DEFAULT_TEMPERATURE
        if num_comps is None:
            num_comps = self.DEFUALT_NUM_COMPLETIONS
        
        if isinstance(messages, str):
            messages = [Message(role="user", content=messages)]
        return await achat(self.model_name,messages)
    
    def gen(
        self,
        messages: List[Message],
        max_tokens: Optional[int] = None,
        temperature: Optional[float] = None,
        num_comps: Optional[int] = None,
    ) -> Union[List[str], str]:
        pass