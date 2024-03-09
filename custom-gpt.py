
import dotenv
from openai import OpenAI


# todo add async that awaits call from frontend

# todo add function that returns messages from gpt


def compare_images_from_url_with_message(url1: str, url2: str, user_input: str = None):
    return [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": user_input},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": url1,
                    },
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": url2
                    },
                },
            ],
        }
    ]


def compare_images_from_url_without_message(url1: str, url2: str):
    return [
        {
            "role": "user",
            "content": [
                {"type": "text", "text":
                    "What’s the difference between these 2 images of the Aral Sea? Is the "
                    "lake more full in the first or second image?"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": url1,
                    },
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": url2
                    },
                },
            ],
        }
    ]


def new_gpt():
    dotenv.load_dotenv()
    client = OpenAI()

    while True:
        user_input = input("input here: ")
        if user_input == "stop":
            break
        completion = client.chat.completions.create(
            model="gpt-4-vision-preview",
            messages=compare_images_from_url_without_message("https://upload.wikimedia.org/wikipedia/"
                                                          "commons/a/a5/Aralsea_tmo_2014231_lrg.jpg",
                                                          "https://upload.wikimedia.org/wikipedia/"
                                                          "commons/2/23/Aral_Sea_August_2017.jpg"
                                                          ),
            max_tokens=2048
        )

        print(completion.choices[0])
        print(completion.choices[0].message)
        print(completion.choices[0].message.content)


if __name__ == "__main__":
    new_gpt()
