import torch
from modelscope import snapshot_download
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
torch.random.manual_seed(0)
class QA:
    def __init__(self, model_manager):
        self.model = model_manager.get_model()
        self.tokenizer = model_manager.get_tokenizer()

    def __call__(self, role, content):
        role_content = {"role": role, "content": content}
        messages = [
            {"role": "system",
             "content": "You are a helpful digital assistant. Please provide safe, ethical and accurate information to the user."},
            {"role": "user", "content": "Can you provide ways to eat combinations of bananas and dragonfruits?"},
            {"role": "assistant",
             "content": "Sure! Here are some ways to eat bananas and dragonfruits together: 1. Banana and dragonfruit smoothie: Blend bananas and dragonfruits together with some milk and honey. 2. Banana and dragonfruit salad: Mix sliced bananas and dragonfruits together with some lemon juice and honey."},
            # {"role": "user", "content": "What about solving an 2x + 3 = 7 equation?"},
        ]
        messages.append(role_content)
        pipe = pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
        )
        generation_args = {
            "max_new_tokens": 500,
            "return_full_text": False,
            "temperature": 0.0,
            "do_sample": False,
        }

        output = pipe(messages, **generation_args)
        print(output[0]['generated_text'])
        return output[0]['generated_text']


# def QA(role, content,model_manager):
#     # model_dir = snapshot_download("LLM-Research/Phi-3-mini-128k-instruct")
#     # model_dir ="C:/Users/LOGAN/.cache/modelscope/hub/LLM-Research/Phi-3-mini-128k-instruct"
#     # model = AutoModelForCausalLM.from_pretrained(
#     #     model_dir,
#     #     device_map="cuda",
#     #     torch_dtype="auto",
#     #     trust_remote_code=True,
#     # )
#     model=model_manager.get_model()
#     # tokenizer = AutoTokenizer.from_pretrained(model_dir)
#     tokenizer = model_manager.get_tokenizer()
#
#     role_content = {"role": role, "content": content}
#     messages = [
#         {"role": "system", "content": "You are a helpful digital assistant. Please provide safe, ethical and accurate information to the user."},
#         {"role": "user", "content": "Can you provide ways to eat combinations of bananas and dragonfruits?"},
#         {"role": "assistant", "content": "Sure! Here are some ways to eat bananas and dragonfruits together: 1. Banana and dragonfruit smoothie: Blend bananas and dragonfruits together with some milk and honey. 2. Banana and dragonfruit salad: Mix sliced bananas and dragonfruits together with some lemon juice and honey."},
#         # {"role": "user", "content": "What about solving an 2x + 3 = 7 equation?"},
#     ]
#     messages.append(role_content)
#     pipe = pipeline(
#         "text-generation",
#         model=model,
#         tokenizer=tokenizer,
#     )
#     generation_args = {
#         "max_new_tokens": 500,
#         "return_full_text": False,
#         "temperature": 0.0,
#         "do_sample": False,
#     }
#
#     output = pipe(messages, **generation_args)
#     print(output[0]['generated_text'])
#     return output[0]['generated_text']
