#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from typing import List, Optional

class Search(ABC):
    @abstractmethod
    def __init__(self):
        self.name = ""
        self.description = ""

    @abstractmethod
    def search(self, query: str) -> Optional[str]:
        """同步搜索方法"""
        pass

    @abstractmethod
    async def search_async(self, query: str) -> str:
        """异步搜索方法"""
        pass

    @abstractmethod
    async def search_batch(self, queries: List[str]) -> List[str]:
        """批量异步搜索方法"""
        pass