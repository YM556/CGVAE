#!/usr/bin/env python
# -*- coding: utf-8 -*-

from duckduckgo_search import DDGS
import asyncio
import requests
import random
from bs4 import BeautifulSoup
from GDesigner.tools.search.search import Search
from GDesigner.tools.search.search_registry import SearchRegistry

@SearchRegistry.register('DuckDuckGo')
class DuckDuckGoSearch(Search):
    def __init__(self):
        super().__init__()
        self.name = "DuckDuckGo SearchEngine"
        self.description = "Search for text in DuckDuckGo"

    async def search(self, query: str, site: str = None) -> str:
        try:
            if site:
                site_query = self.search_sites.get(site.lower(), '')
                query = f"{site_query} {query}"
            
            with DDGS() as ddgs:
                results = list(ddgs.text(query[:300], max_results=1))
            
            if results and len(results) > 0:
                content = await self._get_page_content(results[0]['href'])
                return f'Search:{query}, get:{results[0]["title"]}\n {results[0]["body"]}\n {content}'
            return ''
        except Exception as e:
            print(f"DuckDuckGo搜索出错: {e}")
            return ''

    async def _get_page_content(self, url: str) -> str:
        try:
            response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0', 'Accept-Charset': 'utf-8'})
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                paragraphs = soup.find_all('p')
                content = '\n'.join([p.get_text() for p in paragraphs])
                return content
            return ''
        except Exception as e:
            print(f"获取页面内容出错: {e}")
            return ''

    async def search_async(self, query: str, site: str = None) -> str:
        return await self.search_summary(query, site)

    async def search_batch(self, queries: list[str], site: str = None) -> list[str]:
        tasks = [self.search_summary(query, site) for query in queries]
        return await asyncio.gather(*tasks)

    async def search_summary(self, query: str, site: str = None) -> str:
        try:
            if site:
                site_query = self.search_sites.get(site.lower(), '')
                full_query = f"{site_query} {query}"
            else:
                full_query = query
                
            # 增加请求间隔和重试机制
            max_retries = 3
            retry_delay = 1  # 初始延迟1秒
            results = []
            
            for attempt in range(max_retries):
                try:
                    await asyncio.sleep(retry_delay + random.uniform(0, 2))  # 随机等待1-3秒
                    with DDGS() as ddgs:
                        results = list(ddgs.text(full_query[:300], max_results=2))
                    break
                except Exception as e:
                    if attempt < max_retries - 1:
                        retry_delay *= 2  # 指数退避
                        continue
                    raise

            tasks = [self._get_page_summary(result, query) for result in results]
            summaries = await asyncio.gather(*tasks)
            
            return f'Search:{query}, get:{summaries}'
        except Exception as e:
            print(f"DuckDuckGo搜索出错: {e}")
            return ''

    async def _get_page_summary(self, result: dict, query: str = None) -> str:
        try:
            response = requests.get(result['href'], headers={'User-Agent': 'Mozilla/5.0', 'Accept-Charset': 'utf-8'})
            if response.status_code == 200:
                if response.encoding.lower() not in ['utf-8', 'utf8']:
                    return f'{result["title"]}\n{result["body"]}'
                
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # 获取所有可能包含主要内容的标签
                content_tags = (
                    soup.find_all(['h1', 'h2', 'h3']) +
                    soup.find_all('p') +
                    soup.find_all('article') +
                    soup.find_all(class_=['content', 'article', 'post-content'])
                )
                
                # 过滤和处理段落
                valid_contents = []
                keywords = query.lower().split() if query else []
                
                for tag in content_tags:
                    if len(valid_contents) >= 3:
                        break
                        
                    text = tag.get_text().strip()
                    if len(text) < 50:
                        continue
                    
                    # 检查关键词匹配
                    text_lower = text.lower()
                    if keywords and not any(keyword in text_lower for keyword in keywords):
                        continue
                    
                    # 限制单个段落最大长度
                    if len(text) > 300:
                        text = text[:300] + "..."
                    # 去除多余的空白字符
                    text = ' '.join(text.split())
                    valid_contents.append(text)
                
                summary = '\n'.join(valid_contents)
                return f'{result["title"]}\n{result["body"]}\n{summary}'
            return ''
        except Exception as e:
            print(f"获取页面摘要出错: {e}")
            return ''

if __name__ == "__main__":
    search_ddg = DuckDuckGoSearch()
    queries = ["Python", "Asyncio", "LLM"]
    result = asyncio.run(search_ddg.search_batch(queries,"reddit"))
    print(result)