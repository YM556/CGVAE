#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from typing import List, Optional

class Search(ABC):
    @abstractmethod
    def __init__(self):
        self.name = ""
        self.description = ""
        # 添加默认的搜索源
        self.search_sites = {
            # 技术社区
            "stackoverflow": "site:stackoverflow.com",
            "github": "site:github.com",
            "medium": "site:medium.com",
            "dev": "site:dev.to",
            "hashnode": "site:hashnode.com",
            
            # 学术资源
            "arxiv": "site:arxiv.org",
            "sciencedirect": "site:sciencedirect.com",
            "springer": "site:springer.com",
            "ieee": "site:ieee.org",
            "acm": "site:dl.acm.org",
            "nature": "site:nature.com",
            "science": "site:science.org",
            
            # 开发文档
            "python": "site:python.org",
            "mozilla": "site:developer.mozilla.org",
            "microsoft": "site:learn.microsoft.com",
            "aws": "site:docs.aws.amazon.com",
            "google": "site:developers.google.com",
            
            # 知识百科
            "wikipedia": "site:wikipedia.org",
            "geeksforgeeks": "site:geeksforgeeks.org",
            "w3schools": "site:w3schools.com",
            "tutorialspoint": "site:tutorialspoint.com",
            
            # AI/ML相关
            "huggingface": "site:huggingface.co",
            "pytorch": "site:pytorch.org",
            "tensorflow": "site:tensorflow.org",
            "paperswithcode": "site:paperswithcode.com",
            "distill": "site:distill.pub",
            
            # 问答社区
            "quora": "site:quora.com",
            "zhihu": "site:zhihu.com",
            "reddit": "site:reddit.com"
        }

    @abstractmethod
    def search(self, query: str) -> Optional[str]:
        """同步搜索方法"""
        pass

    @abstractmethod
    async def search_async(self, query: str, site: str = None) -> str:
        """异步搜索方法"""
        pass

    @abstractmethod
    async def search_batch(self, queries: list[str], site: str = None) -> list[str]:
        """批量异步搜索方法"""
        pass