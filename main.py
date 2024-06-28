from image_gen import get_image
from sign_lang import get_prompts

def run_model(prompt):
    image_prompts = get_prompts(prompt)
    for i, prompt in enumerate(image_prompts):
        get_image(prompt, i)
    return image_prompts