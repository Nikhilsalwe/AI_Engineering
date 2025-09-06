import os
import requests
from dotenv import load_dotenv

load_dotenv()

def scrap_linkin_profile(profile_url: str, mock:  bool = False):
    """Scrape LinkedIn profile data using requests library."""

    if mock:
        profile_url = "https://gist.githubusercontent.com/Nikhilsalwe/2dc653f34adf4735f81f8010848d03da/raw/72cb9e758d8afa3a67855b2dd9b7f4dbd0f20cef/nikhil-salwe-scrapin.json"
        response = requests.get(profile_url, timeout=10)
    else:
        print("Using real Scrapin API to fetch data", os.getenv('SCRAPIN_API_KEY'))
        api_enpoint = "https://api.scrapin.io/v1/enrichment/profile"

        headers = {
            "Content-Type": "application/json",
            "x-api-key": os.getenv('SCRAPIN_API_KEY')   # ✅ Correct way
        }

        payload = {
            "linkedInUrl": profile_url
        }

        response = requests.post(api_enpoint, json=payload, headers=headers, timeout=10)

        if response.status_code != 200:
            raise Exception(f"Scrapin API error {response.status_code}: {response.text}")

    print("==============================================")
    data = response.json().get('person')
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None) 
        and k not in ["certifications"]
    }
    # print("Fetched data from Scrapin API:", data)
    return data


if __name__ == "__main__":
    # print("LinkedIn Profile Data:")
    print(
        scrap_linkin_profile("https://www.linkedin.com/in/nikhil-salwe-526a5335/", mock=True)
    )