# Note: DALL-E 3 requires version 1.0.0 of the openai-python library or later
import os
from openai import AzureOpenAI
import json
from . import config

client = AzureOpenAI(
    api_version="2024-05-01-preview",
    azure_endpoint="https://forecastai.openai.azure.com/",
    api_key=config.OPENAI_KEY,
)

def generate(q):
    result = client.images.generate(
        model="Dalle3", # the name of your DALL-E 3 deployment
        prompt=q,
        n=1
    )

    image_url = json.loads(result.model_dump_json())['data'][0]['url']

    return image_url
