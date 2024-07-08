import requests
from twilio.rest import Client

OWM_Endpoint="https://api.openweathermap.org/data/2.5/forecast"#go to this website and get all the information like api key
api_key=""#enter api key
accout_sid=""#enter account ssid
auth_token=""#enter authencation token
weather_params={
    "lat":15.815447,#enter the desired latitude and longitude
    "lon":74.490323,
    "appid":api_key,
    "cnt":4,
}
response=requests.get(OWM_Endpoint,params=weather_params)
# print(response.status_code)
weather_data=response.json()
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain=False
for hour_data in weather_data["list"]:
    condition_code=hour_data["weather"][0]["id"]
    if int(condition_code)<700:
        will_rain=True
if will_rain:
    client=Client(accout_sid,auth_token)
    message=client.messages \
        .create(
        body = "It's going to rain.",
        from_= '',#enter twilio number
        to="",#enter the phone number with country code
    )
    print(message.status)