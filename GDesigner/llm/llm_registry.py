from typing import Optional
from class_registry import ClassRegistry

from GDesigner.llm.llm import LLM


class LLMRegistry:
    registry = ClassRegistry()
    MODEL_NAME_MAP = {
        None: "Pro/deepseek-ai/DeepSeek-V3",
        "": "Pro/deepseek-ai/DeepSeek-V3",
        "DeepSeek-V3": "Pro/deepseek-ai/DeepSeek-V3",
        "DeepSeek-R1": "Pro/deepseek-ai/DeepSeek-R1",
        "QwQ-32B": "Qwen/QwQ-32B",
        "Qwen2.5-Coder-32B": "Qwen/Qwen2.5-Coder-32B-Instruct",
        "Qwen2.5-72B": "Qwen/Qwen2.5-72B-Instruct-128K",
    }

    @classmethod
    def register(cls, *args, **kwargs):
        return cls.registry.register(*args, **kwargs)
    
    @classmethod
    def keys(cls):
        return cls.registry.keys()

    @classmethod
    def get(cls, model_name: Optional[str] = None) -> LLM:
        model_name = cls.MODEL_NAME_MAP.get(model_name)

        if model_name == 'mock':
            model = cls.registry.get(model_name)
        else: 
            model = cls.registry.get('TogetherChat', model_name)

        return model
