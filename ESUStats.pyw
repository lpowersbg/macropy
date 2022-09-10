import requests

URL = "https://esu0-my.sharepoint.com/personal/rlong15_esu_edu/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Frlong15%5Fesu%5Fedu%2FDocuments%2FBlue%20Ridge%2F1%2Exml&parent=%2Fpersonal%2Frlong15%5Fesu%5Fedu%2FDocuments%2FBlue%20Ridge"

response = requests.get(URL)
with open('ESUStats.xml', 'wb') as file:
    file.write(response.content)