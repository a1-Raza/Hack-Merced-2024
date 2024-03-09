
import dotenv
import requests

dotenv.load_dotenv()

NASA_API_KEY="PoptCcoOSqAe4porNulk0WfWuGqkd8afZWRtGmKq"
lat=str(37.38)
lon=str(-120.43)
date="2021-01-01"
dim=str(0.10)
#37.366389, -120.424167


response = requests.get(f"https://api.nasa.gov/planetary/earth/assets?lon={lon}&lat={lat}&date={date}&dim={dim}&api_key={NASA_API_KEY}")

if response.status_code == 200:
    try:
        # Try to parse the response as JSON
        data = response.json()
        image_url = data['url']

        # Now make a request to the image URL to check the Content-Type header
        image_response = requests.get(image_url)

        if image_response.status_code == 200:
            # Check the Content-Type header to determine the image format
            content_type = image_response.headers.get("Content-Type", "")
            print(f"Image Format: {content_type}")
        else:
            print(f"Error {image_response.status_code}: {image_response.text}")

    except requests.exceptions.JSONDecodeError:
        print("Error: Response content is not in JSON format")
else:
    print(f"Error {response.status_code}: {response.text}")
