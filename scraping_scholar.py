# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.chrome.service import Service
# # from webdriver_manager.chrome import ChromeDriverManager
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC


# # import time
# # import pandas as pd

# # # 1. Open Chrome browser
# # driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))

# # # 2. Go to the website
# # url = "https://research.com/scientists-rankings/computer-science"
# # driver.get(url)

# # # 3. Wait for the page to load (because it's dynamic)
# # time.sleep(8)


# # # 4. Find all scientists on the page
# # scientists = driver.find_elements(By.CSS_SELECTOR , ".rankings-content.bg-white.shadow")

# # # 5. Create an empty list to store data
# # data = []

# # # 6. Loop through each scientist and extract rank, name, and country
# # for s in scientists:
# #     rank = s.find_element(By.CSS_SELECTOR , ".col.col--3.py-0.px-0.position").text
# #     name = s.find_element(By.TAG_NAME , "h4").text
# #     country = s.find_element(By.CSS_SELECTOR , ".rankings-country").text

# #     data.append({"Rank" : rank , "Name" : name , "Country" : country})

# # print(data)
# # # 7. Save data into a CSV file
# # df = pd.DataFrame(data)
# # csv_path = "/Users/apple/Downloads/New Projects/scientists.csv"
# # df.to_csv(csv_path, index=False)

# # # 8. Close the browser
# # driver.quit()

# # print("✅ Scraping complete! Saved to scientists.csv")

# # # 9. Automatically open the file
# # import os
# # os.system(f'open "{csv_path}"')


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import pandas as pd

# columns = ["World Rank", "National Rank", "Name", "Image URLs", "Affiliation", "Country", "H-Index", "Citations", "#DBLP"]

# def get_scholar_details(row):
#     details = row.text.split('\n')
#     contents = {}
#     contents["World Rank"] =    details[0]
#     contents["National Rank"] = details[1]
#     contents["Name"] =          details[2]
#     contents["Affiliation"] =   details[3].split(',')[0]
#     contents["Country"] =       details[3].split(',')[1].strip()
#     contents["H-Index"] =       details[4]
#     contents["Citations"] =     details[5].replace(',','')
#     contents["#DBLP"] =         details[6].replace(',','')
#     contents["Image URLs"] =    row.find_element(By.CLASS_NAME, 'lazyload').get_attribute('src')
#     return contents


# def main():
#     scholar_data = []

#     for page_id in range(1,11): 
#         driver = webdriver.Chrome()
#         url = f"https://research.com/scientists-rankings/computer-science?page={page_id}"
#         driver.get(url)
#         rankings = driver.find_element(By.ID, 'rankingItems')
#         rows = rankings.find_elements(By.CLASS_NAME, 'cols')
#         for idx, row in enumerate(rows):
#             if idx % 4 == 0:
#                 scholar_data.append(get_scholar_details(row))
#         driver.close()

#     df = pd.DataFrame(data=scholar_data, columns=columns)
#     df.to_csv("best_cs_scientist_details.csv", index=False)
#     return

# if __name__ == "__main__":
#     main()





#           new versiom


from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

columns = ["World Rank", "National Rank", "Name", "Image URLs", "Affiliation", "Country", "H-Index", "Citations", "#DBLP"]

def get_scholar_details(row):
    details = row.text.split('\n')
    contents = {}
    contents["World Rank"] =    details[0]
    contents["National Rank"] = details[1]
    contents["Name"] =          details[2]
    contents["Affiliation"] =   details[3].split(',')[0]
    contents["Country"] =       details[3].split(',')[-1].strip()
    contents["H-Index"] =       details[4]
    contents["Citations"] =     details[5].replace(',','')
    contents["#DBLP"] =         details[6].replace(',','')
    contents["Image URLs"] =    row.find_element(By.TAG_NAME, 'img').get_attribute('src')
    return contents


def main():
    scholar_data = []

    for page_id in range(1,21): 
        driver = webdriver.Chrome()
        url = f"https://research.com/scientists-rankings/computer-science?page={page_id}"
        driver.get(url)
        rankings = driver.find_element(By.CLASS_NAME, 'rankings-content')
        rows = rankings.find_elements(By.CLASS_NAME, 'cols.scientist-item.rankings-content__item')
        for row in rows:
            scholar_data.append(get_scholar_details(row))
        driver.close()

    df = pd.DataFrame(data=scholar_data, columns=columns)
    df.to_csv("best_cs_scientist_details.csv", index=False)
    return

if __name__ == "__main__":
    main()