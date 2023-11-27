from openai import OpenAI
import json

OPENAI_API_KEY = "sk-"
OPENAI_MODEL = "gpt-3.5-turbo"
TEMPERATURE = 0 # Value between 0 and 2

client = OpenAI(api_key=OPENAI_API_KEY)

def get_response(prompt):
    messages = [
        { "role": "user", "content": prompt }
    ]
    completions = client.chat.completions.create(
        model = OPENAI_MODEL,
        temperature = TEMPERATURE,
        messages = messages,
    )
    return completions.choices[0].message.content
    

def britishize(text):
    """
    Returns the British English version of the passed-in American
    English text.
    """
    propmt_template = """I will give you an american english version of a text, it will be delimited by three backticks ```. 
Just give me the translation and no other surronunding symbols.
Please give me the translation of the following text into British English \
in the shape of a JSON document with keys "language" and "content".

```
{text}
```
        """

    prompt = propmt_template.format(text=text)

    text = get_response(prompt)

    text = json.loads(text)["content"]

    return text