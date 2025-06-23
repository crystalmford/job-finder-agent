# Remote Job Finder Agent

A Python-based automation tool that scrapes remote job listings from the Remote OK API, filters for data analyst and data scientist roles, and exports the results to a CSV file for easy browsing and tracking.

## Features

- Connects to the public Remote OK JSON API
- Filters for roles containing "data analyst" or "data scientist"
- Includes job title, company, location, salary (if listed), and direct link
- Applies a salary floor of ~$60,000/year when data is available
- Outputs a clean, structured CSV file

## Technologies Used

- Python 3
- Requests (for API access)
- Pandas (for data organization and export)

## How to Run

1. Clone the repository:
   git clone https://github.com/crystalmford/job-finder-agent.git

2. Navigate to the project folder:
   cd job-finder-agent

3. Install dependencies:
   pip install requests pandas

4. Run the script:
   python remoteok_api_scraper.py

## Output

The script will generate a file named `remoteok_data_jobs.csv` that contains:

- Title
- Company
- Location
- Tags
- Salary
- Link

## Author

Crystal Ford
GitHub: https://github.com/crystalmford
LinkedIn: https://www.linkedin.com/in/crystalmford
