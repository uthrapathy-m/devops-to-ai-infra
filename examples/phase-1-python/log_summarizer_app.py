from fastapi import FastAPI
from openai import OpenAI
from pydantic import BaseModel

app = FastAPI()
client = OpenAI()  # in Phase 3, point base_url at your own LLM gateway


class Logs(BaseModel):
    text: str


@app.post("/summarize")
def summarize(logs: Logs):
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an SRE. List the errors and the likely root cause in 5 bullets."},
            {"role": "user", "content": logs.text[-12000:]},  # keep the newest lines; tokens cost money
        ],
    )
    return {"summary": resp.choices[0].message.content, "tokens": resp.usage.total_tokens}
