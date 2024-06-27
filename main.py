from image_gen import get_image

prompts = ["A beautiful sunset over the ocean", "A beautiful sunrise over the mountains", "A beautiful sunset over the mountains", "A beautiful sunrise over the ocean"]
for i, prompt in enumerate(prompts):
    get_image(prompt, i)