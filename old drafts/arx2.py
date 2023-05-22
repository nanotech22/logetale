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
        self.categories = []

    def extract_info(self):
        arxiv_api_url = f"http://export.arxiv.org/api/query?id_list={self.arxiv_id}"

        feed = feedparser.parse(arxiv_api_url)
        entry = feed.entries[0]

        self.authors = [author['name'] for author in entry.authors]
        self.title = entry.title
        self.summary = entry.summary
        self.published = entry.published
        self.categories = [tag['term'] for tag in entry.tags]
# Extract year, month, and day from the published timestamp
        self.published_date = datetime.datetime.strptime(self.published, "%Y-%m-%dT%H:%M:%SZ")
        
    def display_info(self):
        print("arXiv Link:", self.arxiv_link)
        print("Authors:", self.authors)
        print("Title:", self.title)
        print("Summary:", self.summary)
        print("Published:", self.published)
        
        # Display the extracted date components
        print("Published Date:")
        print("Year:", self.published_date.year)
        print("Month:", self.published_date.month)
        print("Day:", self.published_date.day)











arxiv_link = "https://arxiv.org/abs/2305.10137"

paper = Paper(arxiv_link)
paper.extract_info()
paper.display_info()