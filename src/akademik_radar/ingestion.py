import urllib.request
import urllib.parse
import feedparser
import time
from colorama import Fore, Style

class ArxivIngestor:
    """
    Connects to the ArXiv API to fetch real-time academic papers.
    Base URL: http://export.arxiv.org/api/query
    """
    
    def __init__(self):
        self.base_url = "http://export.arxiv.org/api/query"

    def fetch_papers(self, topic, max_results=3):
        """
        Fetches papers related to a specific topic.
        Encryption: None (Public API)
        """
        # Clean query
        clean_topic = urllib.parse.quote(topic)
        query_url = f"{self.base_url}?search_query=all:{clean_topic}&start=0&max_results={max_results}"
        
        try:
            # Simulate "Satellite Connection" delay for effect, but keep it brief
            # time.sleep(0.5) 
            
            with urllib.request.urlopen(query_url) as url:
                response = url.read()
            
            feed = feedparser.parse(response)
            
            papers = []
            for entry in feed.entries:
                papers.append({
                    "title": entry.title.replace('\n', ' '),
                    "published": entry.published,
                    "link": entry.link,
                    "summary": entry.summary[:200] + "..."
                })
                
            return papers
            
        except Exception as e:
            print(f"{Fore.RED}[!] UPLINK ERROR: {e}{Style.RESET_ALL}")
            return []

if __name__ == "__main__":
    # Test stub
    ingestor = ArxivIngestor()
    print("Testing connection...")
    results = ingestor.fetch_papers("Quantum Computing", 1)
    print(results)
