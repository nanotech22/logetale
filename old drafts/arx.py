import feedparser

def extract_paper_info(arxiv_link):
    arxiv_id = arxiv_link.split("/")[-1]
    arxiv_api_url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"

    feed = feedparser.parse(arxiv_api_url)
    entry = feed.entries[0]
    print(entry)

    authors = [author['name'] for author in entry.authors]
    title = entry.title
    summary = entry.summary
    published = entry.published
    categories = entry.tags
    
    print("Authors:", authors)
    print("Title:", title)
    print("Summary:", summary)
    print("Published:", published)
    print("Categories:", categories)

# Example usage:
arxiv_link = "https://arxiv.org/abs/2305.10137"
extract_paper_info(arxiv_link)
