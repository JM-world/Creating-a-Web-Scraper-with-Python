from requests import get

websites = [
    "google.com",
    "airbnb.com",
    "https://twitter.com",
    "facebook.com",
    "https://tiktok.com"
]

# for website in websites:   
#     if not website.startswith ("https://"):
#         website = f"https://{website}"
#     response = get(website)
#     if response.status_code == 200:
#         print(f"{website} is OK")
#     else:
#         print(f"{website} not OK")

results = {
}

for website in websites:   
    if not website.startswith ("https://"):
        website = f"https://{website}"
    response = get(website)
    if response.status_code < 200:
        results[website] = "1xx / Information responses"
    elif response.status_code < 300:
        results[website] = "2xx / Successful responses"
    elif response.status_code < 400:
        results[website] = "3xx / Redirection messages"
    elif response.status_code < 500:
        results[website] = "4xx / Client error responses"
    else:
        results[website] = "5xx / Server error responses"

print(results)