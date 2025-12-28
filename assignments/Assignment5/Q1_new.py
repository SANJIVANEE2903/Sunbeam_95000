from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

# increase page load timeout
driver.set_page_load_timeout(300)

driver.get("https://www.sunbeaminfo.in/internship")

wait = WebDriverWait(driver, 30)

print("\n_____________Page Title_____________\n", driver.title)

# scroll down
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# wait for plus button and click
plus_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//a[@href='#collapseSix']"))
)
driver.execute_script("arguments[0].scrollIntoView(true);", plus_button)
plus_button.click()

print("\n_____________Internship Information_____________\n")
paras = wait.until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".main_info.wow.fadeInUp"))
)

for p in paras:
    print(p.text)

print("\n______________Internship Batches_____________\n")

rows = driver.find_elements(By.TAG_NAME, "tr")

batches = []

for row in rows:
    cols = row.find_elements(By.TAG_NAME, "td")
    if len(cols) < 8:
        continue

    batches.append({
        "sr": cols[0].text,
        "batch": cols[1].text,
        "batch duration": cols[2].text,
        "start date": cols[3].text,
        "end date": cols[4].text,
        "time": cols[5].text,
        "fees": cols[6].text,
        "download": cols[7].text
    })

print(json.dumps(batches, indent=4))

driver.quit()
