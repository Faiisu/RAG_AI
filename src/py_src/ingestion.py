import arxiv, os, requests

def download_pdfs(pdf_links, download_folder="documents", filename = ""):
    # Create the download folder if it doesn't already exist.
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
        print(f"Created directory: {download_folder}")

    url = pdf_links
    try:
        response = requests.get(url, stream=True)
        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status()

        # Extract the filename from the URL
        # filename = os.path.join(download_folder, url.split("/")[-1])
        filename = os.path.join(download_folder, filename+'.pdf')

        # Save the content to a local file
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Successfully downloaded: {filename}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred for {url}: {e}")
        
def arxiv_ingestion():
    #API connect
    client = arxiv.Client()
    #search
    search = arxiv.Search(
        query=f"cat:q-fin*", #q-fin is finance topic
        max_results=20,
        sort_by=arxiv.SortCriterion.SubmittedDate #Date sort
    )
    results = client.results(search)
    for result in client.results(search):
        # print(f"Title: {result.title}")
        # print(f"   All Categories (Subqueries): {result.categories}")
        # print(f"   PDF Link: {result.pdf_url}")
        for categorie in result.categories:
            if('q-fin' not in categorie): continue
            download_folder = f"./data/{categorie}/"
            download_pdfs(pdf_links=result.pdf_url, download_folder=download_folder, filename=result.title.replace(" ",""))
        print("-" * 30)
        
if __name__ == "__main__":
    arxiv_ingestion()