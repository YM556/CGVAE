#!/usr/bin/env python
# -*- coding: utf-8 -*-

from GDesigner.tools.search.search import Search
from GDesigner.tools.search.search_registry import SearchRegistry
from GDesigner.tools.search.arXiv import ArxivSearch
from GDesigner.tools.search.google import GoogleSearch
from GDesigner.tools.search.baidu import BaiduSearch
from GDesigner.tools.search.duckduckgo import DuckDuckGoSearch

__all__ = [
    'Search',
    'SearchRegistry',
    'ArxivSearch',
    'GoogleSearch',
    'BaiduSearch',
    'DuckDuckGoSearch'
]