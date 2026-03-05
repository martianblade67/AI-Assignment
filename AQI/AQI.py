import requests

class AQIAgent:

    def __init__(self, city, api_key):
        self.city = city
        self.api_key = api_key


    def get_sensor_data(self):
        url = f"https://api.waqi.info/feed/{self.city}/?token={self.api_key}"
        response = requests.get(url)
        data = response.json()

        if data["status"] == "ok":
            return data["data"]["aqi"]
        else:
            return None




    def determine_category(self, aqi):

        if aqi <= 50:
            return "Good"
        elif aqi <= 100:
            return "Moderate"
        elif aqi <= 200:
            return "Poor"
        elif aqi <= 300:
            return "Very Poor"
        else:
            return "Severe"

    


    def act(self):
        aqi = self.get_sensor_data()

        if aqi is None:
            print("Unable to retrieve AQI data")
            return

        category = self.determine_category(aqi)

        print("Region:", self.city)
        print("AQI Value:", aqi)
        print("Air Quality Category:", category)





API_KEY = "9dc6499a387416abd3f553a0833e61397c6f5bbf"
city = input("Enter city name: ")

agent = AQIAgent(city, API_KEY)
agent.act()