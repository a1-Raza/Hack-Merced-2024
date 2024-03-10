import webbrowser
import dotenv
import os
import requests

dotenv.load_dotenv()

NASA_API_KEY = os.getenv("NASA_API_KEY")


def force(lat, lon, dim):
    for year in range(2015, 2023):
        for month in ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]:
            date = f"{year}-{month}-01"

            response = requests.get(f"https://api.nasa.gov/planetary/earth/assets?lon={lon}"
                                    f"&lat={lat}&date={date}&dim={dim}&api_key={NASA_API_KEY}").json()
            webbrowser.open(response["url"])
            print(date, response["url"])


if __name__ == "__main__":
    # force()
    pass
