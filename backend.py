import requests

API_KEY = "34c92c80c4cdb80f623b0dea0c44138a"


def get_data(place, days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * days
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", days=3))


