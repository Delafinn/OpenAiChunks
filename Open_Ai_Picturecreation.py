import openai
import webbrowser

API_KEY = "Your API KEY"


HEADERS = {

    'Authorization': f'Bearer Authorization: Bearer {API_KEY}'

}


openai.api_key = API_KEY

response = openai.Image.create(
  prompt=" YOUR PROMPT HERE",
  n=4,
  size="1024x1024"
)

data = response['data']

url_list= []

image_urls = response['data'][0:]

for image in image_urls:
    url_list.append(image["url"])


for url in url_list:
    webbrowser.open(url)
