from GDesigner.dynamic.dytool import Dytool
from GDesigner.dynamic.dytool_registry import ToolRegistry


@ToolRegistry.register('RAG')
class Dyrag(Dytool):
    def __init__(self):
        # 方式描述映射
        self.mode_info_dict = {
            'dense': "Dense RAG 使用神经向量检索，适合语义匹配任务，但计算资源消耗较大。",
            'sparse': "Sparse RAG 基于关键词匹配，效率高，但可能遗漏语义相关文档。",
            'hybrid': "Hybrid RAG 结合 dense 与 sparse，兼顾召回率与精度，适用于综合型任务。",
            'retriever_reranker': "Retriever + Reranker 是一种两阶段检索方案，先召回再排序，适用于对精度要求较高的任务。",
        }

        # 知识源描述映射
        self.source_info_dict = {
            'PDF': "PDF 文档通常为结构化或半结构化文件，适合处理正式文档、研究报告等任务。",
            'Web': "Web 页面信息丰富但结构不一致，适合开放域问答与多源融合任务。",
            'Database': "结构化数据库中的数据准确性高，适用于数值分析、事实验证等任务。",
            'Wikipedia': "Wikipedia 内容覆盖广泛，适用于百科类、背景知识补充任务。",
            'SearchEngine': "搜索引擎作为动态信息源，适合实时性强、需要最新信息的任务。",
        }

    def get_info_by_mode(self, mode: str) -> str:
        return self.mode_info_dict.get(mode, f"未知的RAG方式：{mode}。请确认输入是否正确。")

    def get_info_by_source(self, source: str) -> str:
        return self.source_info_dict.get(source, f"未知的知识源类型：{source}。请确认输入是否正确。")

    def get_dynamic_info(self) -> str:
        return "Dyrag 是用于获取 RAG 配置相关动态信息的工具类。请通过 `get_info_by_mode(mode)` 和 `get_info_by_source(source)` 方法使用。"