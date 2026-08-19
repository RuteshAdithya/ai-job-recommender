from apify_client import ApifyClient
import os
from urllib.parse import quote_plus
from dotenv import load_dotenv

load_dotenv()


def get_client():
    api_token = os.getenv("APIFY_API_TOKEN")
    if not api_token:
        raise RuntimeError("APIFY_API_TOKEN is missing. Add it to your environment or .env file.")
    return ApifyClient(api_token)


def fetch_linkedin_jobs(keyword, rows=25):
    client = get_client()
    keyword = keyword.strip()
    if not keyword:
        raise ValueError("A job-search keyword is required.")

    run_input = {
        "urls": [f"https://www.linkedin.com/jobs/search/?keywords={quote_plus(keyword)}"],
        "scrapeCompany": True,
        "count": rows,
        "splitByLocation": False,
    }
    run = client.actor("curious_coder/linkedin-jobs-scraper").call(run_input=run_input)
    return list(client.dataset(run["defaultDatasetId"]).iterate_items())


def fetch_naukri_jobs(search_query, rows=25):
    client = get_client()
    search_query = search_query.strip()
    if not search_query:
        raise ValueError("A job-search keyword is required.")

    run_input = {
        "keyword": search_query,
        "maxJobs": rows,
        "freshness": "all",
        "sortBy": "relevance",
        "experience": "all",
    }
    run = client.actor("alpcnRV9YI9lYVPWk").call(run_input=run_input)
    return list(client.dataset(run["defaultDatasetId"]).iterate_items())
