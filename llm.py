import instructor
from openai import OpenAI
import BaseResponse

client = instructor.from_openai(OpenAI(
  organization='org-1RKpzvEArSyvC6mFuTq5daAA',
  project='proj_8EJ9RzVQ22rJnaGb1hNYgUYW',
  api_key="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"
))

stream = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "I've been feeling unwell for the past week. It started with a mild fever, around 100 degrees Fahrenheit, and a sore throat that makes it difficult to swallow. Over the next few days, I developed a persistent dry cough, which worsens at night. I've also experienced some shortness of breath, especially after walking for a while. Recently, I've started feeling fatigue and body aches, particularly in my lower back and legs. Occasionally, I feel lightheaded, and I’ve noticed that my appetite has decreased. Despite resting, the symptoms haven't improved much. Based on this, provide a well-detailed diagnosis of the most likely illness and explain why in detail start by giving the Introduction(Briefly summarize the symptoms),Diagnosis Explanation(Discuss the most likely illness, why it fits the symptoms.) without adding heading or section or consideration or giving the next action In 102 words. Also, give the top 3 possible illnesses with confidence percentages without numbering or heading but in a new line. Recommend 3 over-the-counter medications with purpose, with dosages, typically used to treat it."}],
     response_model=BaseResponse.Analysis
)

print(stream.model_dump_json())

