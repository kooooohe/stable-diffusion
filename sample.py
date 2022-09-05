import torch
from diffusers import StableDiffusionPipeline
from torch import autocast
 
MODEL_ID = "CompVis/stable-diffusion-v1-4"
DEVICE = "cpu"
# DEVICE = "cuda"
YOUR_TOKEN = "YOUR TOKEN"
 
pipe = StableDiffusionPipeline.from_pretrained(MODEL_ID,  use_auth_token=YOUR_TOKEN)
pipe.to(DEVICE)

prompt = "A digital Illustration of Cloud shaped machines with a digital monkey, 4k, detailed, trending in artstation, fantasy vivid colors"
 
image = pipe(prompt, guidance_scale=7.5)["sample"][0]
image.save("test.png")

