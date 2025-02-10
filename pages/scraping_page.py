from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

class ScrapingPage:
    def __init__(self,driver):
        self.driver=driver
        self.url="https://demoqa.com/books"

    def open(self):
        self.driver.get(self.url)

    def scrape_books(self):
        WebDriverWait(self.driver,15).until(
            EC.presence_of_element_located((By.CLASS_NAME,"rt-tr-group"))
        )

        books=self.driver.find_elements(By.CLASS_NAME,"rt-tr-group")
        data=[]

        for book in books:
            try:
                title=book.find_element(By.CLASS_NAME,"mr-2").text
                author=book.find_element(By.XPATH,"//div[position()=4]").text
                data.append({"Title":title,"Author":author})
            except:
                continue

        return data
    def save_to_csv(self,data,filename="books.csv"):
        df=pd.DataFrame(data)
        df.to_csv(filename,index=False)
        

