from openai import OpenAI

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
    propmt_template = "Q: What is the British English version of this text?\nA: "
    prompt = propmt_template + text

    text = get_response(prompt)

    return text