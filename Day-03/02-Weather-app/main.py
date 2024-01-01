import requests
import os
import json

def main():
	cite = input("Enter your cite :- ")

	data = requests.get(f"https://api.weatherapi.com/v1/current.json?key=c474c2f2796f4144b4635020230310&q={cite}&aqi=no")
	data = data.text
	data = json.loads(data)

	temp = data['current']['temp_c']

	os.system(f'say "The current weather in {cite} is {temp} degrees"')
if __name__ == '__main__':
	main()