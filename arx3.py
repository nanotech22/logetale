import json
import feedparser
import datetime

class Paper:
    def __init__(self, arxiv_link):
        self.arxiv_link = arxiv_link
        self.arxiv_id = arxiv_link.split("/")[-1]
        self.authors = []
        self.title = ""
        self.summary = ""
        self.published = ""
        self.published_date = None
    
    def extract_info(self):
        arxiv_api_url = f"http://export.arxiv.org/api/query?id_list={self.arxiv_id}"

        feed = feedparser.parse(arxiv_api_url)
        entry = feed.entries[0]

        self.authors = [author['name'] for author in entry.authors]
        self.authors.remove("Leo Herr")

        if self.authors:
            self.authors_text = "With " + ", ".join(self.authors)


        self.title = entry.title
        self.summary = entry.summary.replace('\n', ' ')
        self.published = entry.published
        self.published_date = datetime.datetime.strptime(self.published, "%Y-%m-%dT%H:%M:%SZ")
        
    def display_info(self):
        print("arXiv Link:", self.arxiv_link)
        print("Authors:", self.authors)
        print("Title:", self.title)
        print("Summary:", self.summary)
        # print("Published:", self.published)
        print(f"Published Date: {self.published_date.month}/{self.published_date.day}/{self.published_date.year}")
        
    def to_json(self):
        data = {
            "arxiv_link": self.arxiv_link,
            "authors": self.authors,
            "title": self.title,
            "summary": self.summary,
            "published": self.published,
            "published_date": self.published_date.strftime("%Y-%m-%d")
        }
        return json.dumps(data, indent=4)
    
    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        paper = cls(data["arxiv_link"])
        paper.authors = data["authors"]
        paper.title = data["title"]
        paper.summary = data["summary"]
        paper.published = data["published"]
        paper.published_date = datetime.datetime.strptime(data["published_date"], "%Y-%m-%d").date()
        return paper





arxiv_link = "https://arxiv.org/abs/2305.10137"

paper = Paper(arxiv_link)
paper.extract_info()

# Convert the Paper object to JSON
paper_json = paper.to_json()
print(paper_json)

# Create a Paper object from JSON
new_paper = Paper.from_json(paper_json)
new_paper.display_info()
