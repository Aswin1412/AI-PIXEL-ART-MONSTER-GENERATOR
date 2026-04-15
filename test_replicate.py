import replicate

output = replicate.run(
    "stability-ai/stable-diffusion",
    input={"prompt": "pixel art monster"}
)

print(output)