
"""
DO NOT CHECK THE IMAGE LINK BEFORE CHATGPT PROCESSES IT! IT WILL BREAK!!!
On the first view of the link from a certain ip, it will give a direct image link, but
on all future visits, it will link to the imgur page, not the direct image!
"""
import dotenv
import os
from openai import OpenAI
from satelliteApi import get_image

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def new_gpt(lat1, lon1, date1, dim1, lat2, lon2, date2, dim2: float, special_instructions: str = None):

    completion = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text",
                     "text": "What's the difference between these two satellite images?"
                             "The point of interest is the body of water centered in the middle of the picture."
                             "Please disregard factors such as color, seasonal changes, and image quality; "
                             "these images may have been taken at different times of day, and times of year."
                             "Likewise, please ignore land use changes. There may be changes in nearby"
                             "buildings. Please focus your area on the body of water and the things related to it."
                             "If there is an issue with the images, please say so in your reply. Please"
                             "also state if the issue is with one or both images. These images will likely be dark"
                             "or low quality. Please try and do the best you can with the images provided,"
                             "and only state issues if the images are not available at all. In the event that"
                             "one or both of the images are mostly or entirely white, *always* state that analysis is"
                             "not possible because of thick cloud cover, and attempt to analyze the unobstructed"
                             "image if possible. In the event of thick cloud cover, advise the user to 'change the"
                             "date by one month for a crisper image' in your reply."
                     },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": get_image(lat1, lon1, date1, dim1),
                        },
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": get_image(lat2, lon2, date2, dim2),
                        },
                    },
                    {
                        "type": "text",
                        "text": f"What follows will be any special instructions to guide your analysis. If 'None'"
                                f"or left blank, please ignore:{special_instructions}"
                    }
                ],
            }
        ],
        max_tokens=2048,
    )
    print(completion.choices[0])
    print(completion.choices[0].message)
    print(completion.choices[0].message.content)


if __name__ == "__main__":
    dotenv.load_dotenv()
    client = OpenAI()

    while True:
        user_input = input("input here: ")
        if user_input in ["stop", "exit", "quit"]:
            break
        new_gpt(37.38, -120.43, "2016-01-01", 0.10, 37.38, -120.43, "2015-01-01", 0.10)
