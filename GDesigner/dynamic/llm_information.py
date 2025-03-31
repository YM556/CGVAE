class Dyllm:
    def __init__(self):
        self.llm_info = {
            # OpenAI 系列
            "GPT-4.5": """GPT-4.5 is a general-purpose large language model released by OpenAI, designed for complex tasks and multi-modal scenarios.
            The model has approximately 2 trillion parameters. It demonstrates strong performance in complex reasoning and contextual understanding.
            This model performs exceptionally well in tasks such as programming, mathematics, and language generation and understanding, especially in structured reasoning and code generation.
            """,
            "GPT-4": """GPT-4 is a high-performance general-purpose model launched by OpenAI, suitable for reasoning, conversation, and generation-intensive applications.
            The model has approximately 1.76 trillion parameters and supports various multi-modal inputs such as images and text, with excellent contextual understanding.
            It shows outstanding performance in programming, language comprehension, mathematical reasoning, and generation tasks, with notable stability and optimization capabilities.
            """,
            "GPT-3.5": """GPT-3.5 is a medium-sized language model released by OpenAI, suitable for text generation, conversation, and general language tasks.
            The model has 175 billion parameters and offers a balance between performance and cost-effectiveness.
            It performs well in generation, code writing, and other tasks but is relatively weaker in complex reasoning and mathematical tasks.
            """,
            "GPT-3.5-turbo": """GPT-3.5-turbo is an optimized version of GPT-3.5, designed for faster response and lower deployment costs.
            It also has 175 billion parameters, with system-level enhancements to improve inference speed and API call efficiency.
            This model is suitable for daily applications, lightweight programming, and summarization tasks, though it has some limitations in handling complex reasoning.
            """,
            "GPT-4o": """GPT-4o is a multi-modal optimized model launched by OpenAI that supports input forms such as text, speech, image, and video.
            The model has about 1.76 trillion parameters and features fast response times and strong multi-modal understanding.
            It performs strongly in generation and understanding tasks across various modalities, while maintaining low latency and high efficiency.
            """,
            "GPT-4o-mini": """GPT-4o-mini is a lightweight multi-modal model launched by OpenAI, suitable for edge devices and resource-constrained deployments.
            Its parameter scale is smaller than GPT-4o (exact figures not public), retaining multi-modal capabilities while optimizing for size.
            It performs decently in text generation and language understanding but is less capable in complex reasoning and mathematical tasks.
            """,

            # Meta LLaMA 系列
            "Llama-3.1-405B": """Llama-3.1-405B is a large-scale open-source model released by Meta, designed for multilingual processing and long-context applications.
            The model has 405 billion parameters, with stable reasoning structures and strong contextual retention ability.
            It performs very well in language generation, multilingual interaction, and logical reasoning tasks, and also shows good performance in mathematical and programming tasks.""",
            "Llama-3.3-70B-Instruct-Turbo": """Llama-3.3-70B-Instruct-Turbo is an instruction-tuned model launched by Meta, focused on improving answer accuracy and alignment.
            With 70 billion parameters, it supports long-context input and multi-turn dialogue optimization, suitable for multilingual usage scenarios.
            This model performs well in consistent language generation and dialogue. It also has good capabilities in code and mathematical tasks, making it suitable for complex interactions.
            """,
            "Llama-3.1-70B-Instruct-Turbo": """Llama-3.1-70B-Instruct-Turbo is a high-performance conversational model launched by Meta, suitable for knowledge Q&A and content generation.
            With 70 billion parameters, it has strong multilingual understanding and contextual retention capabilities.
            It excels in language understanding tasks such as generation and comprehension, and also shows good performance in code generation and mathematical reasoning.""",
            "Llama-2-13B": """Llama-2-13B is a medium-sized open-source model released earlier by Meta, suitable for on-device deployment and lightweight inference applications.
            The model has 13 billion parameters, with basic language generation and comprehension capabilities, and low resource requirements.
            It performs well in basic text generation and language tasks but is relatively weaker in complex reasoning and high-difficulty programming tasks.
            """,

            # Google Gemini 系列
            "Gemini-1.5-Pro": """Gemini-1.5 Pro is a general-purpose multimodal model released by Google DeepMind, supporting unified processing of text, images, audio, and video.
            The model’s parameter count is not publicly disclosed, but it features an ultra-long context window (over 200K tokens) and advanced cross-modal understanding capabilities.
            It demonstrates strong performance in multilingual understanding, complex text generation, programming tasks, and mathematical reasoning, making it especially suitable for tasks involving multimodal reasoning.
            """,
            "Gemini-2.0-flash": """Gemini-2.0 Flash is a high-performance multimodal model launched by Google, focused on response speed and context processing capabilities.
            Although the parameter size is undisclosed, it features a long context window and high processing efficiency, making it suitable for latency-sensitive tasks.
            It performs well in text generation and multimodal input processing. While its performance in mathematics and code reasoning is moderate, it excels in fast response and broad adaptability.
            """,
            
            # 阿里巴巴 Qwen 系列
            "QwQ-32B": """QwQ-32B is a medium-sized reasoning model launched by Alibaba’s Qwen series, with a focus on solving complex problems.
            The model has 32 billion parameters, using the QQA architecture, integrated with RoPE, SwiGLU, RMSNorm, and Attention QKV Bias technologies.
            It performs well in language understanding, scientific computing, and structured question answering, and shows solid capabilities in programming and mathematical reasoning. Suitable for high-complexity scenarios.
            """,
            "Qwen2.5-72B": """Qwen2.5-72B-Instruct is a large-scale language model released by Alibaba Cloud, focused on instruction-following, multilingual support, and long-context processing.
            With 72 billion parameters, it supports context lengths up to 128K and is optimized for structured output capabilities.
            It performs excellently in multilingual processing, language generation, mathematical reasoning, and structured tasks, making it a strong choice for high-performance general-purpose applications.
            """,
            "Qwen2.5-Coder-32B":"""Qwen2.5-Coder-32B-Instruct is a code-specialized model launched by Alibaba Cloud, optimized for code generation, understanding, and repair.
            The model has 32 billion parameters and is trained on 5.5 trillion tokens to enhance programming capabilities while retaining general-purpose functions.
            It excels in programming-related tasks, offering outstanding comprehensive coding capabilities, and also shows strong performance in mathematics and language understanding.
            """,
            "Qwen1.5-1.8B": """Qwen1.5-1.8B is a lightweight model released by Alibaba, suitable for edge deployment and local environment execution.
            It has 1.8 billion parameters, with a compact structure, fast response, and low resource consumption.
            It performs well in basic generation and simple dialogue tasks but is relatively weak in mathematical reasoning, programming, and long-context understanding.
            """,

            # DeepSeek 系列
            "DeepSeek-V3": """DeepSeek-V3 is a high-performance Mixture-of-Experts (MoE) model released by DeepSeek, focused on enhancing reasoning and training efficiency.
            With a total of 671 billion parameters, it adopts a MoE architecture, along with the MLA attention mechanism and load-balancing optimization strategies.
            The model performs exceptionally well in programming, mathematics, language generation, and scientific reasoning, offering comprehensive capabilities comparable to top-tier proprietary models.
            """,
            "DeepSeek-R1": """DeepSeek-R1 is a reinforcement learning-optimized model introduced by DeepSeek, aimed at reducing repetitive generation and improving output readability.
            The parameter count is undisclosed. It enhances reasoning ability and task completion through cold-start data and RL fine-tuning methods.
            This model shows strong performance in code generation, language generation, and mathematical reasoning, especially suitable for scenarios with high-quality generation requirements.
            """,

        }

    def get_llm_feature_information(self, llm_name):
        return self.llm_info.get(llm_name, "Model information not found.")
