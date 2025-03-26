#!/usr/bin/env python
# -*- coding: utf-8 -*-

from baidusearch.baidusearch import search
import asyncio
import requests
from bs4 import BeautifulSoup
import time

class BaiduSearch:
    def __init__(self):
        self.name = "Baidu SearchEngine"
        self.description = "Search for an item in Baidu"

    def search(self, query):
        try:
            # 获取前1个搜索结果的URL
            results = search(query[:300], num_results=1)
            if results and len(results) > 0:
                # 获取网页内容
                return self._get_page_content(results[0]['url'])
            return None
        except Exception as e:
            print(f"百度搜索出错: {e}")
            return None
    
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

async def get_baidu_summary(query):
    try:
        # 获取前1个搜索结果的URL
        results = search(query, num_results=1)
        if results and len(results) > 0:
            # 获取网页内容摘要
            return await _get_page_summary(results[0]['url'])
        return ""
    except Exception as e:
        print(f"百度搜索出错: {e}")
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

async def search_baidu(query):
    ret = ""
    try:
        # 获取前2个搜索结果的URL
        results = search(query, num_results=2)
        tasks = []
        
        if results and len(results) > 0:
            for result in results:
                url = result['url']
                tasks.append(_get_page_summary(url))
            summaries = await asyncio.gather(*tasks)
            for i, summary in enumerate(summaries):
                if len(summary):
                    url = results[i]['url']
                    title = results[i]['title']
                    ret += f"百度搜索结果 [{title}]({url}) 的摘要是: {summary}\n"
        return ret
    except Exception as e:
        print(f"百度搜索出错: {e}")
        return f"百度搜索出错: {e}"

async def search_baidu_main(queries):
    tasks = [search_baidu(query) for query in queries]
    results = await asyncio.gather(*tasks)
    return results

if __name__ == "__main__":
    queries = ["Python", "Asyncio", "LLM"]
    result = asyncio.run(search_baidu_main(queries))
    print(result)