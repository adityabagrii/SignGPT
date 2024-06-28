from image_gen import get_image
from sign_lang import get_prompts

# Getting prompt from user sending it to LLM to convert it into sign language instructions
prompt = 'I Love You'
image_prompts = get_prompts(prompt)
print(image_prompts)
for i, prompt in enumerate(image_prompts):
    get_image(prompt, i)