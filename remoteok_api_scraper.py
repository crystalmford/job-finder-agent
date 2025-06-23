import requests
import pandas as pd

# Step 1: Fetch Remote OK API data
url = "https://remoteok.com/api"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
data = response.json()

# Step 2: Filter for relevant jobs
target_keywords = ["data analyst", "data scientist"]
jobs = []

for job in data:
    if "id" not in job:
        continue

    title = job.get("position") or job.get("title") or ""
    tags = job.get("tags", [])
    salary = job.get("salary", "")
    description = job.get("description", "").lower()
    raw_link = job.get("url", "")
    link = "https://remoteok.com" + raw_link if raw_link.startswith("/") else raw_link

    if any(keyword in title.lower() or keyword in description for keyword in target_keywords):
        # Apply salary filter (estimate: $60K/year minimum)
        if salary and any(s in salary for s in ["$60", "$65", "$70", "$75", "$80", "$90", "$100"]):
            pass  # include jobs with good salary
        elif not salary:
            pass  # include jobs with no listed salary
        else:
            continue  # skip low salary listings

        jobs.append({
            "Title": title,
            "Company": job.get("company"),
            "Location": job.get("location") or "Remote",
            "Tags": ", ".join(tags),
            "Salary": salary or "Not listed",
            "Link": link
        })

# Step 3: Save to CSV
df = pd.DataFrame(jobs)
print(df[["Title", "Company", "Salary", "Link"]].head(3))  # Preview top 3 jobs
df.to_csv("remoteok_data_jobs.csv", index=False)
print(f"\nSaved {len(df)} jobs to remoteok_data_jobs.csv")
