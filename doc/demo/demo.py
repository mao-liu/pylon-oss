import functools
import logging
import os

import pylon

import openai

logging.basicConfig(
    level="INFO",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

OPENAI_API_KEY_PATH = "~/code/secrets/openai-api-key-demo"
OPENAI_MODEL = "gpt-3.5-turbo"


@functools.cache
def openai_client() -> openai.OpenAI:
    with open(os.path.expanduser(OPENAI_API_KEY_PATH), 'r') as fd:
        api_key = fd.read().strip()

    client = openai.OpenAI(api_key=api_key)
    return client


def chatgpt_text_generate(message: str, model: str=OPENAI_MODEL) -> str:
    client = openai_client()

    messages = [
      {
        "role": "system", "content": "You are an intelligent assistant. Please respond in single sentences."
      },
      {
        "role": "user", "content": message
      }
    ]
    chat = client.chat.completions.create(
        model=model,
        messages=messages
    )
    response = chat.choices[0].message.content
    return response


@pylon.PipelineComponent
def pipeline_task(message: pylon.models.messages.BaseMessage, config) -> pylon.models.messages.BaseMessage:
    print(f'\nMessage received: {message.body}\n')

    output = pylon.models.messages.RawContentMessage('text/plain')
    output.body = chatgpt_text_generate(message.body)

    print(f'\nOutput published: {output.body}\n')
    yield output


if __name__ == '__main__':
    pipeline_task.runForever()
