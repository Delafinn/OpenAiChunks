import openai


API_KEY = "Your API_KEY"


openai.api_key = API_KEY

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="give me a linkedIn post about the difficulty of learning the Python programming langauge?",
  temperature=0.2,
  max_tokens=120,
  top_p=0.5,
  frequency_penalty=1,
  presence_penalty=0.5
)

print(response)
