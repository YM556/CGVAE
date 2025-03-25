class Dyllm:
    def __init__(self):
        self.llm_info = {
            # OpenAI Series
            "GPT-4.5": {
                "size": "Unknown (estimated ~2T parameters)",
                "features": ["Enhanced reasoning", "Improved coding", "Better multilingual support"],
                "company": "OpenAI"
            },
            "GPT-4": {
                "size": "1.76T parameters",
                "features": ["Strong reasoning", "Code generation", "Multi-modal capabilities"],
                "company": "OpenAI"
            },
            "GPT-3.5": {
                "size": "175B parameters",
                "features": ["Text generation", "Code completion", "Translation"],
                "company": "OpenAI"
            },

            # xAI (Grok Series)
            "Grok-3": {
                "size": "314B parameters",
                "features": ["Real-time knowledge", "Sarcasm detection", "X platform integration"],
                "company": "xAI"
            },
            "Grok-2": {
                "size": "Unknown (smaller than Grok-3)",
                "features": ["Basic reasoning", "Conversational AI", "Limited context length"],
                "company": "xAI"
            },

            # Google (Gemini Series)
            "Gemini 2.0": {
                "size": "Unknown (multi-modal)",
                "features": ["Advanced reasoning", "Long-context processing", "Multi-modal (text, image, audio)"],
                "company": "Google"
            },
            "Gemini 1.5 Pro": {
                "size": "Unknown",
                "features": ["200K+ context window", "Multi-modal", "Efficient fine-tuning"],
                "company": "Google"
            },

            # Anthropic (Claude Series)
            "Claude-3.5-Sonnet": {
                "size": "Unknown",
                "features": ["Strong reasoning", "Safety alignment", "Optimized for long conversations"],
                "company": "Anthropic"
            },
            "Claude-3.7": {
                "size": "Unknown",
                "features": ["Faster inference", "Long-context handling", "Complex task optimization"],
                "company": "Anthropic"
            },
            "Claude 3 Opus": {
                "size": "Unknown",
                "features": ["Top-tier reasoning", "200K+ context", "Human-like understanding"],
                "company": "Anthropic"
            },

            # DeepSeek Series
            "DeepSeek-V3": {
                "size": "671B parameters (37B active)",
                "features": ["MoE architecture", "Efficient inference", "Low training cost"],
                "company": "DeepSeek"
            },
            "DeepSeek-R1": {
                "size": "Unknown (optimized for inference)",
                "features": ["Reinforcement learning", "Low-cost inference", "Open-source"],
                "company": "DeepSeek"
            },

            # Alibaba (Qwen Series)
            "Qwen2-72B": {
                "size": "72B parameters",
                "features": ["Open-source", "128K context", "Multilingual (27+ languages)"],
                "company": "Alibaba"
            },
            "Qwen2.5-Max": {
                "size": "Unknown (MoE-based)",
                "features": ["Multi-modal", "Long-context", "Open-source"],
                "company": "Alibaba"
            },

            # 01.AI (Yi Series)
            "Yi-Large": {
                "size": "Unknown (Preview)",
                "features": ["Strong benchmarks", "200K+ context", "Vision-language support"],
                "company": "01.AI"
            },

            # Meta (Llama Series)
            "Llama-3.1-405B": {
                "size": "405B parameters",
                "features": ["Open-source", "Multilingual", "Long-context handling"],
                "company": "Meta"
            },
        }
    
    def get_llm_size_information(self, model_name):
        if model_name in self.llm_info:
            return self.llm_info[model_name]["size"]
        return "Model information not found"
    
    def get_llm_feature_information(self, model_name):
        if model_name in self.llm_info:
            return self.llm_info[model_name]["features"]
        return "Model information not found"
    
    def get_llm_company_information(self, model_name):
        if model_name in self.llm_info:
            return self.llm_info[model_name]["company"]
        return "Model information not found"
