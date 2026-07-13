# king.py
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="gpt-4o",
    temperature=0.9,
    messages=[
        {"role": "system", "content": "당신은 세종대왕입니다. 지혜롭고 백성을 생각하는 어조로 답변하세요."},
        {"role": "user", "content": "변수가 뭐야?"}, 
    ]
)

print(response.choices[0].message.content)   # response의 내용만 출력

#######################################################

# no_prompting.py
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="gpt-4o",
    temperature=0.9,
    messages=[
        {"role": "system", "content": "너는 유치원 학생이야. 유치원생처럼 답변해줘."},
        {"role": "user", "content": "오리"},
    ]
)

print(response.choices[0].message.content) 
