import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Setup Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode (optional)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Load the page
url = "https://fbref.com/en/comps/27/schedule/Super-League-Greece-Scores-and-Fixtures"
driver.get(url)

# Use WebDriverWait to ensure the table is fully loaded
try:
    # Wait until the table is visible (or adjust the condition based on your needs)
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "table"))
    )
    print("✅ Page loaded successfully.")
except Exception as e:
    print(f"❌ Error loading the page: {e}")
    driver.quit()
    exit()

# Find all tables on the page
tables = driver.find_elements(By.TAG_NAME, "table")
print(f"🔍 Found {len(tables)} tables.")

# If no tables found, exit
if not tables:
    print("❌ No tables found on the page.")
    driver.quit()
    exit()

# Debugging: Print out the first 100 characters of each table's text to inspect
for i, t in enumerate(tables):
    print(f"Table {i+1}:")
    print(t.text[:100])  # Print only the first 100 characters of the table text
    print("-" * 50)

# Try to locate the correct table dynamically by checking for the presence of "Round"
table = None
for t in tables:
    if "Score" in t.text:  # Check for the headers we identified
        table = t
        print("✅ Table found!")
        break

if not table:
    print("❌ Couldn't find the correct table.")
    driver.quit()
    exit()

# Extract data
rows = table.find_elements(By.TAG_NAME, "tr")
data = []
for row in rows[1:]:  # Skip header row
    cols = row.find_elements(By.TAG_NAME, "td")
    if len(cols) >= 6:  # Ensure that the row has the expected number of columns
        wk = cols[0].text
        day = cols[1].text
        date = cols[2].text
        time_ = cols[3].text
        home_team = cols[4].text
        score = cols[5].text
        away_team = cols[6].text

        

        data.append([wk, day, date, time_, home_team, score, away_team])

# Close Selenium
driver.quit()

# Save to CSV
df = pd.DataFrame(data, columns=["Wk", "Day","Date", "Time", "Home_Team","Score", "Away Team"])
df.to_csv("super_league_greece_2024_25.csv", index=False, encoding="utf-8")

print("✅ CSV file saved")
