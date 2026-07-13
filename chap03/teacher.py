# teacher.py
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
        {"role": "system", "content": "당신은 초보자를 가르치는 친절한 파이썬 강사입니다. 어려운 용어를 쉽게 설명하세요."},
        {"role": "user", "content": "변수가 뭐야?"}, 
    ]
)

print(response.choices[0].message.content)   # response의 내용만 출력
