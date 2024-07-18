
import requests 

def WeatherUpdate():
        city = input("Which city weather you want to know?\n")
        url = "http://api.weatherapi.com/v1/current.json?key=67f09c2b704542b6b5881435242605&q="+city+"&aqi=yes"
        response = requests.get(url)
        weather_json = response.json()
        temp = weather_json.get('current').get('temp_c')
        description = weather_json.get('current').get('condition').get('text')
        tempFeel = weather_json.get('current').get('feelslike_c')
        humdity = weather_json.get('current').get('humidity')
        currentTime = weather_json.get('location').get('localtime')
        print("Current weather in",city,"at",currentTime,"is ",description, "and the temprature is ",temp,"C and feels like",tempFeel,"C, with humidity", humdity,"%")
def main(): 
    user_Choice = "yes"
    while user_Choice.lower().__contains__("yes"):
        WeatherUpdate()
        user_Choice = input("Do you want to search for another city's weather? (Yes or No)\n")
 
main()



