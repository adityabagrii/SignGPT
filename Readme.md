# SignGPT
SignGPT is a web application that converts input text prompts to sign language instructions using Llama 3 for Natural Language Processing (NLP) and Stable Diffusion XL for generating images based on the descriptions. The application is built using Flask, Python, HTML, CSS, and JavaScript.

## Features
- Converts text prompts to sign language instructions.
- Uses Llama 3 for NLP to generate descriptions of sign language instructions.
- Uses Stable Diffusion XL to generate images from descriptions.
- User-friendly web interface.

## Workflow
1. **Entering the prompt:** You start by entering the prompt in the Text Area given on the home page. After you enter the prompt click the button to submit your request.
2. **Generating instructions:** After you have submitted the request your prompt is sent to a remotely hosted Llama 3 model hosted using **HuggingFace Spaces** to convert the given prompt into sign language instructions.
3. **Receiving Prompts:** After the prompts are converted to sign language instructions, these are further refined to extract just the instructions from the additional texts.
4. **Forwarding Prompts to Image Generation Model:** Once we have the refined prompts we forward them to remotely hosted **Stable Diffusion XL Model** to generate and receive images.
5. **Displaying Images:** Once we receive the generated images fromt the **SDXL** we pass them dynmaically from backend to frontend and display them with the prompts respectively.
## Prerequisites
- Python
- Flask
- Hugging Face Transformers
- Stable Diffusion XL
- HTML, CSS, JavaScript

## Technologies Used
- Llama 3 API from HuggingFace
- Stable Diffusion XL API from HuggingFace
- Flask Library
- HuggingFace Spaces
- HTML
- CSS
- JavaScript

## Note
The accuracy of the images and the prompts are totally dependent on the model used and the fine-tuning of the model. If you want better results from the model you can fine-tune the model on local storage and use them for better results.

## Demo

https://github.com/adityabagrii/SignGPT/assets/130608893/c3ad0032-5327-44eb-a150-7672f377459e

