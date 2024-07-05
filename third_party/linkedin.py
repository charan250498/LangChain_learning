import os
import requests
from dotenv import load_dotenv

load_dotenv()

def scarpe_linekdin_profile(linkedin_profile_url: str, mock: bool=True):
    # Scrape information from Linkedin profiles.
    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/charan250498/19cc6e7d34556afe9a1cf3feb31fbea1/raw/125df2fdf4460e3796f158c0543bac224bd5dd2e/linkedin_profile.json"
        response = requests.get(linkedin_profile_url, timeout=10)

    else:
        api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
        headers = {'Authorization': 'Bearer ' + os.environ['PROXYCURL_API_KEY']}
        params = {'linkedin_profile_url': linkedin_profile_url}
        response = requests.get(api_endpoint, params=params, headers=headers, timeout=10)

    data = response.json()

    # Get rid of empty and unwanted fields.
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", " ", None)
        and k not in ["people_also_viewed", "certifications"]
    }

    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data

if __name__ == "__main__":
    data = scarpe_linekdin_profile("", True)
    print(data)