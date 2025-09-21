import requests
from bs4 import BeautifulSoup
from pathlib import Path


def scrape_example(url: str) -> str:
    """Fetch the title of the given webpage.

    If the request fails (for example due to lack of internet
    connectivity), a fallback message is returned instead of
    raising an exception.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.title.string.strip() if soup.title else "No title found"
    except Exception as exc:  # pragma: no cover - network dependent
        return f"Could not fetch title: {exc}"


def main():
    url = 'https://example.com'
    title = scrape_example(url)
    print(f"Title of {url}: {title}")

    # Save the title to data/example.txt
    data_dir = Path(__file__).resolve().parent.parent / 'data'
    data_dir.mkdir(exist_ok=True)
    output_file = data_dir / 'example.txt'
    output_file.write_text(f"{url} -> {title}\n")
    print(f"Saved results to {output_file}")


if __name__ == '__main__':
    main()
