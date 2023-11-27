import arxiv
import datetime

# Keywords for search
keywords = ['gpt-4', 'software']

# Get the papers from arxiv
try:
    search = arxiv.Search(query=" AND ".join(keywords),
                          max_results=100,
                          sort_by=arxiv.SortCriterion.LastUpdatedDate)
except Exception as e:
    print(f"Error occurred while fetching data from arxiv API: {str(e)}")
    exit(1)

# To keep track of the latest paper
latest_paper = None
latest_date = datetime.datetime.min

# Go through each paper
for result in search:
    # If it's more recent than the latest so far
    if result.updated > latest_date:
        latest_date = result.updated
        latest_paper = result

# Write the results to a file
with open('latest_paper.txt', 'w') as f:
    if latest_paper:
        f.write(f"Latest paper is '{latest_paper.title}' and it's updated on {latest_date}\n")
        f.write(f"Abstract: {latest_paper.summary}\n")
        f.write(f"URL: {latest_paper.entry_id}\n")
    else:
        f.write('No papers found.')