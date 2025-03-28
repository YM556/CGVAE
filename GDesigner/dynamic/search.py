from GDesigner.dynamic.dytool import Dytool
from GDesigner.dynamic.dytool_registry import ToolRegistry

# search
@ToolRegistry.register('Search')
class Dysearch(Dytool):
    def __init__(self):
        super().__init__()
        self.search_mode_info_dict = {
           "Google": "Google是最受欢迎的搜索引擎，适合搜索广泛的信息和资源",
           "Baidu": "百度是全球最大的中文搜索引擎，适合搜索中文信息和资源",
           "DuckDuckGo": "DuckDuckGo是隐私保护的搜索引擎，适合搜索特定信息和资源",
           "Wiki": "Wiki是一个维基百科平台，适合搜索维基百科页面和相关信息", 
        }
        
        # 搜索源描述映射表
        self.search_source_info_dict = {
            # 技术社区
            "stackoverflow": "Stack Overflow是全球最大的程序员问答社区，适合搜索编程问题的解决方案和最佳实践",
            "github": "GitHub是最大的代码托管平台，适合搜索开源项目、代码示例和技术实现",
            "medium": "Medium是高质量的技术博客平台，适合搜索深度技术文章和经验分享",
            "dev": "Dev.to是现代化的开发者社区，提供最新的技术趋势和实践经验",
            "hashnode": "Hashnode是开发者写作平台，提供个人技术博客和经验分享",
            
            # 学术资源
            "arxiv": "arXiv是最大的预印本论文平台，适合搜索最新的研究论文，特别是计算机科学和人工智能领域",
            "sciencedirect": "ScienceDirect是Elsevier的主要文献平台，提供高质量的同行评议论文",
            "springer": "Springer是著名的科技出版商，提供全面的科研文献资源",
            "ieee": "IEEE是电气电子工程师学会的数据库，适合搜索计算机科学和电子工程领域的论文",
            "acm": "ACM数字图书馆提供计算机科学领域的权威文献",
            "nature": "Nature是世界顶级科学期刊，提供突破性研究成果",
            "science": "Science是顶级科学期刊，提供重要科研发现和综述",
            
            # 开发文档
            "python": "Python官方文档，提供Python语言的标准库和使用指南",
            "mozilla": "MDN Web文档，提供Web技术的详细文档和教程",
            "microsoft": "Microsoft Learn平台，提供微软技术栈的学习资源",
            "aws": "AWS文档，提供亚马逊云服务的官方指南",
            "google": "Google开发者文档，提供Google各种API和服务的使用指南",
            
            # 知识百科
            "wikipedia": "维基百科是最大的在线百科全书，提供广泛的知识概念解释",
            "geeksforgeeks": "GeeksforGeeks提供计算机科学教程和面试准备资源",
            "w3schools": "W3Schools提供Web技术的入门教程和参考",
            "tutorialspoint": "TutorialsPoint提供各种技术的详细教程",
            
            # AI/ML相关
            "huggingface": "Hugging Face是最大的AI模型和数据集平台，提供最新的AI模型和工具",
            "pytorch": "PyTorch官方文档，提供深度学习框架的使用指南",
            "tensorflow": "TensorFlow官方文档，提供机器学习框架的完整文档",
            "paperswithcode": "Papers with Code提供AI论文及其实现代码",
            "distill": "Distill提供高质量的机器学习可视化解释文章",
            
            # 问答社区
            "quora": "Quora是国际性问答平台，提供专业人士的见解",
            "zhihu": "知乎是中文问答社区，提供中文技术讨论和解答",
            "reddit": "Reddit包含多个专业技术社区，提供最新讨论和资源"
        }
        
        
    def get_info_by_mode(self, mode: str) -> str:
        return self.search_mode_info_dict.get(mode, f"未知的搜索模式：{mode}。请确认输入是否正确。")

    def get_info_by_source(self, source: str) -> str:
        return self.search_source_info_dict.get(source, f"未知的搜索源类型：{source}。请确认输入是否正确。")

    def get_dynamic_info(self) -> str:
        return "Dysearch 是用于获取搜索引擎/搜索源相关动态信息的工具类。请使用 `get_info_by_source(source)` 方法获取具体描述。"