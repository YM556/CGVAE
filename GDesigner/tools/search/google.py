#!/usr/bin/env python
# -*- coding: utf-8 -*-

from googlesearch import search
import asyncio
import requests
from bs4 import BeautifulSoup
from GDesigner.tools.search.search import Search
from GDesigner.tools.search.search_registry import SearchRegistry

@SearchRegistry.register('Google')
class GoogleSearch(Search):
    def __init__(self):
        super().__init__()
        self.name = "Google SearchEngine"
        self.description = "Search for an item in Google"

    def search(self, query: str) -> str:
        try:
            # 获取前1个搜索结果的URL
            result = list(search(query[:300], num_results=1))
            if len(result) > 0:
                # 获取网页内容
                return self._get_page_content(result[0])
            return None
        except Exception as e:
            print(f"Google搜索出错: {e}")
            return None
            
    async def search_async(self, query: str) -> str:
        return await search_google(query)
        
    async def search_batch(self, queries: list[str]) -> list[str]:
        return await search_google_main(queries)
    
    def _get_page_content(self, url):
        try:
            response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                # 提取正文内容
                paragraphs = soup.find_all('p')
                content = '\n'.join([p.get_text() for p in paragraphs])
                return content
            return None
        except Exception as e:
            print(f"获取页面内容出错: {e}")
            return None

async def get_google_summary(query):
    try:
        # 获取前1个搜索结果的URL
        result = list(search(query, num_results=1))
        if len(result) > 0:
            # 获取网页内容摘要
            return await _get_page_summary(result[0])
        return ""
    except Exception as e:
        print(f"Google搜索出错: {e}")
        return ""

async def _get_page_summary(url):
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # 提取前几段作为摘要
            paragraphs = soup.find_all('p')
            summary = '\n'.join([p.get_text() for p in paragraphs[:3]])
            return summary
        return ""
    except Exception as e:
        print(f"获取页面摘要出错: {e}")
        return ""

async def search_google(query):
    ret = ""
    try:
        # 获取前2个搜索结果的URL
        results = list(search(query, num_results=2))
        tasks = []
        
        if len(results) > 0:
            for url in results:
                tasks.append(_get_page_summary(url))
            summaries = await asyncio.gather(*tasks)
            for url, summary in zip(results, summaries):
                if len(summary):
                    ret += f"Google搜索结果 {url} 的摘要是: {summary}\n"
        return ret
    except Exception as e:
        print(f"Google搜索出错: {e}")
        return f"Google搜索出错: {e}"

async def search_google_main(queries):
    tasks = [search_google(query) for query in queries]
    results = await asyncio.gather(*tasks)
    return results

if __name__ == "__main__":
    queries = ["Python", "Asyncio", "LLM"]
    result = asyncio.run(search_google_main(queries))
    print(result)