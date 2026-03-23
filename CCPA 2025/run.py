import json
from transformers import AutoModelForCausalLM, AutoTokenizer

from tqdm import tqdm  # 用于显示进度条
def load_json(file_path):
    """Load JSON data from a file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data, file_path):
    """Save JSON data to a file."""
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def query_qwen(prompt, model, tokenizer):
    """Generate a response from the Qwen model given a prompt."""
    messages = [
        {"role": "system", "content": "你是一个擅长古诗词的专家。"},
        {"role": "user", "content": prompt}
    ]
    
    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )   
    
    model_inputs = tokenizer([text], return_tensors="pt").to(model.device)
    generated_ids = model.generate(
        **model_inputs,
        max_new_tokens=520
    )
    
    # Extract only newly generated tokens
    generated_ids = [
        output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
    ]
    
    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return response.strip()


def process_poetry_data(data, model, tokenizer):
    """Process poetry data and generate responses using the Qwen model with a progress bar."""
    results = []
    
    # 使用 tqdm 进度条
    for item in tqdm(data, desc="Processing Poems", unit="poem"):
        prompt = f"""
        我会给你提供一个 JSON 数据，格式如下：
        - **"title"**：古诗词的标题  
        - **"author"**：古诗词的作者  
        - **"content"**：古诗词的内容  
        - **"qa_words"**：古诗词中需要翻译的词语  
        - **"qa_sents"**：古诗词中需要提供白话文译文的句子  
        - **"choose"**：一个包含多个选项的字典，每个选项代表该诗词可能表达的情感  

        这是我的数据：
        ```json
        {json.dumps(item, ensure_ascii=False, indent=4)}
        ```

        ### 你的任务：
        请你根据提供的数据，生成如下 JSON 格式的结果：
        - **"ans_qa_words"**：对 `"qa_words"` 词语的含义进行解释  
        - **"ans_qa_sents"**：对 `"qa_sents"` 句子提供白话文译文  
        - **"choose_id"**：从 `"choose"` 选项中选择最符合该古诗词情感的标号，仅输出对应的字母  

        ### **输出格式示例：**
        {{
            "idx": {item.get("idx", 0)},
            "ans_qa_words": {{
                "词语1": "词语1的含义",
                "词语2": "词语2的含义",
                "词语3": "词语3的含义"
            }},
            "ans_qa_sents": {{
                "句子1": "句子1的白话文翻译",
                "句子2": "句子2的白话文翻译"
            }},
            "choose_id": ""
        }}
        ### **注意事项：**
        1. **仅返回 JSON 结果，不需要额外解释或输出其他内容。**  
        2. **请确保 `"choose_id"` 只输出选项的字母，不要附加其他文本。**  
        3. **请保持输出格式整洁，符合 JSON 规范。**
        """

        response = query_qwen(prompt, model, tokenizer)
        
        # 清理返回的 JSON 数据
        response = response.strip()
        
        try:
            parsed_response = json.loads(response)
            results.append(parsed_response)
        except json.JSONDecodeError:
            print(f"Warning: Failed to parse JSON for item {item.get('idx', 'unknown')}. Response: {response}")
    
    return results, response




    """Main function to load data, process it, and save results."""
input_file = "input.json"
output_file = "tang_output.json"

data = load_json(input_file)
print("Loaded data successfully.")

model_name = ""# 模型名称
print("Loading model and tokenizer...")

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

print("Model loaded successfully!")

result_data,raw_data = process_poetry_data(data, model, tokenizer)
save_json(result_data, output_file)

print("Processing completed. Results saved to output.json")

