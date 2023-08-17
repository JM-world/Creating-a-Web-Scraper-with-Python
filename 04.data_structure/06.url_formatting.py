websites = [
    "google.com",
    "airbnb.com",
    "https://twitter.com",
    "facebook.com",
    "https://tiktok.com"
]

for website in websites:   
    if website.startswith ("https://"):
        print("good to go")
    else:
        print("we have to fix it")
