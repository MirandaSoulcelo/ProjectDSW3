
import requests

def get_defeat_joke():
    url = 'https://v2.jokeapi.dev/joke/Programming'  
    params = {
        'type': 'single'  
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  
        joke = response.json()
        if 'joke' in joke:
            return joke['joke']
        else:
            return "No joke found."
    except requests.RequestException as e:
        print(f"Error fetching joke: {e}")
        return "Failed to get joke."

#def translate_text(text, target_lang='pt'):
    #url = f'https://api.mymemory.translated.net/get?q={text}&langpair=en|{target_lang}'
    #try:
     #   response = requests.get(url)
      #  response.raise_for_status()  
      #  data = response.json()
      #  if 'responseData' in data and 'translatedText' in data['responseData']:
       #     return data['responseData']['translatedText']
        #else:
         #   return 'Error in translation.'
    #except requests.RequestException as e:
     #   print(f"Error fetching translation: {e}")
      #  return 'Error fetching translation.'
    






