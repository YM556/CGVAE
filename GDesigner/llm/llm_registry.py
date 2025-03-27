from typing import Optional
from class_registry import ClassRegistry

from GDesigner.llm.llm import LLM
from dotenv import load_dotenv
import os

load_dotenv()
MY_SERVER = os.getenv("SERVER")

class LLMRegistry:
    registry = ClassRegistry()
    MODEL_NAME_MAP = {
        "siliconflow":{
            None: "Pro/deepseek-ai/DeepSeek-V3",
            "": "Pro/deepseek-ai/DeepSeek-V3",
            "DeepSeek-V3": "Pro/deepseek-ai/DeepSeek-V3",
            "DeepSeek-R1": "Pro/deepseek-ai/DeepSeek-R1",
            "QwQ-32B": "Qwen/QwQ-32B",
            "Qwen2.5-Coder-32B": "Qwen/Qwen2.5-Coder-32B-Instruct",
            "Qwen2.5-72B": "Qwen/Qwen2.5-72B-Instruct-128K",
        },
        "together":{
            None: "deepseek-ai/DeepSeek-V3",
            "": "deepseek-ai/DeepSeek-V3",
            "DeepSeek-V3": "deepseek-ai/DeepSeek-V3",
            "DeepSeek-R1": "deepseek-ai/DeepSeek-R1",
            "Llama 3.3 70B Instruct Turbo": "meta-llama/Llama-3.3-70B-Instruct-Turbo",
            "Llama 3.1 70B Instruct Turbo": "meta-llama/Llama-3.1-70B-Instruct-Turbo",
            "QwQ-32B-Preview": "Qwen/QwQ-32B-Preview",
            "Qwen2.5-Coder-32B":"Qwen/Qwen2.5-Coder-32B-Instruct"
        }
    }

    @classmethod
    def register(cls, *args, **kwargs):
        return cls.registry.register(*args, **kwargs)
    
    @classmethod
    def keys(cls):
        return cls.registry.keys()

    @classmethod
    def get(cls, model_name: Optional[str] = None) -> LLM:
        model_name = cls.MODEL_NAME_MAP.get(MY_SERVER).get(model_name)

        if MY_SERVER == 'together':
            model = cls.registry.get('together')
        else: 
            model = cls.registry.get('GPTChat', model_name)

        return model
