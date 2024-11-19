import llama_cpp.llama_tokenizer
from llama_cpp import Llama
# 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
# Model
###Qwen2 ==> 
# repo_id="Qwen/Qwen2-0.5B-Instruct-GGUF",
# filename="qwen2-0_5b-instruct-fp16.gguf",



# llama = llama_cpp.Llama.from_pretrained(

#     # repo_id="bartowski/c4ai-command-r-08-2024-GGUF",
# 	# filename="c4ai-command-r-08-2024-IQ2_M.gguf",

#     # repo_id="Qwen/Qwen2-0.5B-Instruct-GGUF",
#     # filename="qwen2-0_5b-instruct-fp16.gguf",
# 	repo_id="bartowski/Reflection-Llama-3.1-70B-GGUF",
# 	filename="Reflection-Llama-3.1-70B-IQ2_M.gguf",


#     verbose=False,
# )

llama = llama_cpp.Llama.from_pretrained(
    	repo_id="google/gemma-2b",
	filename="gemma-2b.gguf",
	# repo_id="SanctumAI/Meta-Llama-3.1-8B-Instruct-GGUF",
	# filename="meta-llama-3.1-8b-instruct.Q2_K.gguf",
    #   repo_id="Qwen/Qwen2-0.5B-Instruct-GGUF",
    # filename="qwen2-0_5b-instruct-fp16.gguf",
        verbose=False,

)

response = llama.create_chat_completion(
    messages=[{"role": "user", "content": "I've been feeling unwell for the past week. It started with a mild fever, around 100 degrees Fahrenheit, and a sore throat that makes it difficult to swallow. Over the next few days, I developed a persistent dry cough, which worsens at night. I've also experienced some shortness of breath, especially after walking for a while. Recently, I've started feeling fatigue and body aches, particularly in my lower back and legs. Occasionally, I feel lightheaded, and I’ve noticed that my appetite has decreased. Despite resting, the symptoms haven't improved much. give a diagnosis of the most likely illness and why in long sentence,  provide the top 3 possible illnesses with confidence rates with percentage , and recommend 3 medications that are typically used to treat it with dosage ?"}],
    stream=True,
     
)

for chunk in response:
    delta = chunk["choices"][0]["delta"]
    if "content" not in delta:
        continue
    print(delta["content"], end="", flush=True)

print()