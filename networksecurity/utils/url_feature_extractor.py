import re
from urllib.parse import urlparse

def extract_url_features(url: str) -> dict:
    parsed = urlparse(url)

    return {
        "having_IP_Address": int(bool(re.search(r"\d+\.\d+\.\d+\.\d+", url))),
        "URL_Length": len(url),
        "Shortining_Service": int(any(x in url for x in ["bit.ly", "tinyurl", "goo.gl"])),
        "having_At_Symbol": int("@" in url),
        "double_slash_redirecting": int(url.count("//") > 1),
        "Prefix_Suffix": int("-" in parsed.netloc),
        "having_Sub_Domain": parsed.netloc.count(".") - 1,
        "SSLfinal_State": int(parsed.scheme == "https"),
        "Domain_registeration_length": -1,
        "Favicon": 1,
        "port": int(parsed.port is not None),
        "HTTPS_token": int("https" in parsed.netloc),
        "Request_URL": -1,
        "URL_of_Anchor": -1,
        "Links_in_tags": -1,
        "SFH": -1,
        "Submitting_to_email": int("mailto:" in url),
        "Abnormal_URL": 0,
        "Redirect": int(url.count("http") > 1),
        "on_mouseover": -1,
        "RightClick": -1,
        "popUpWidnow": -1,
        "Iframe": -1,
        "age_of_domain": -1,
        "DNSRecord": 1,
        "web_traffic": -1,
        "Page_Rank": -1,
        "Google_Index": 1,
        "Links_pointing_to_page": -1,
        "Statistical_report": -1
    }
