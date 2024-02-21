import requests
from bs4 import BeautifulSoup


url = "https://www.klubsumica.com/manje-privatne-zabave/"
response = requests.get(url)
html_content = response.text


soup = BeautifulSoup(html_content, "html.parser")


paragraphs = soup.find_all("p")


filename_txt = "odlomci.txt"
with open(filename_txt, "w") as file:
    for paragraph in paragraphs:
        file.write(paragraph.text + "\n")

    
email = soup.select_one("a[href^='mailto:']").get("href")[7:]
phone = soup.select_one("a[href^='tel:']").text



print("Kontakt informacije:")
print("E-mail:", email)
print("Broj mobitela:", phone)