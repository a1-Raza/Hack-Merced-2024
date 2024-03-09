
import dotenv
from openai import OpenAI


# todo add async that awaits call from frontend

# todo add function that returns messages from gpt

def new_gpt():
    dotenv.load_dotenv()
    client = OpenAI()

    while True:
        user_input = input("input here: ")
        if user_input == "stop":
            break
        completion = client.chat.completions.create(
          model="gpt-3.5-turbo",  # todo change to gpt 4
          messages=[
            {"role": "user", "content": user_input}
          ]
        )

        print(completion.choices[0].message)
        print(completion.choices[0].message.content)


if __name__ == "__main__":
    new_gpt()
