from GDesigner.dynamic.dytool import Dytool
from GDesigner.dynamic.dytool_registry import ToolRegistry

# search
@ToolRegistry.register('Search')
class Dysearch(Dytool):
    def __init__(self):
        super().__init__()

        # 搜索源描述映射表
        self.search_source_info_dict = {
            'Google': "Google 是全球最大的通用搜索引擎，覆盖广、更新快，适合开放领域信息检索。",
            'Bing': "Bing 是微软的搜索引擎，界面清爽，结果结构化，适合中英文检索任务。",
            'PubMed': "PubMed 是生物医学文献数据库，适合学术搜索、生物医学任务中的知识增强。",
            'Arxiv': "Arxiv 提供预印本论文搜索，适合科研、技术趋势分析任务。",
            'Reddit': "Reddit 是社交新闻社区，适合获取舆情信息、用户观点和实时讨论内容。",
            '知乎': "知乎是中文问答社区，适合中文任务中获取大众经验、讨论、教程等信息。",
            'Twitter': "Twitter 上的信息高度实时，适合获取突发事件、新闻头条和热门话题。",
            'YouTube': "YouTube 可作为视频内容搜索源，适合多模态任务、教程检索等。",
        }

    def get_info_by_source(self, source: str) -> str:
        return self.search_source_info_dict.get(source, f"未知的搜索源类型：{source}。请确认输入是否正确。")

    def get_dynamic_info(self) -> str:
        return "Dysearch 是用于获取搜索引擎/搜索源相关动态信息的工具类。请使用 `get_info_by_source(source)` 方法获取具体描述。"