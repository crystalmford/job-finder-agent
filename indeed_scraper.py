import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Ask user for job search input
search_term = input("What job are you looking for? (e.g. data analyst): ")
location = input("Where? (e.g. remote, New York, London): ")

# Step 2: Build the search URL
base_url = "https://www.indeed.com/jobs"
params = {
    "q": search_term,
    "l": location,
    "sort": "date"
}

# Step 3: Send the request
response = requests.get(base_url, params=params)
soup = BeautifulSoup(response.text, "html.parser")

# Step 4: Find job cards
job_cards = soup.find_all("a", class_="tapItem")

# Step 5: Extract job data
jobs = []
for card in job_cards:
    title = card.find("h2", class_="jobTitle")
    company = card.find("span", class_="companyName")
    location = card.find("div", class_="companyLocation")
    link = "https://www.indeed.com" + card["href"]

    if title and company and location:
        jobs.append({
            "Title": title.text.strip(),
            "Company": company.text.strip(),
            "Location": location.text.strip(),
            "Link": link
        })

# Step 6: Display results
df = pd.DataFrame(jobs)
print(df)

# Optional: Save to CSV
df.to_csv("indeed_jobs.csv", index=False)
print("\nJobs saved to indeed_jobs.csv")
