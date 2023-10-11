#######################################################################################################################
import requests
import os


def main():
    # url = "https://api.apilayer.com/exchangerates_data/convert?to=USD&from=EUR&amount=30"
    #
    # payload = "2023-07-05"
    # headers = {"apikey": "232rbNPipRrj0SEYKxuGP4MIGudecNiI"}
    #
    # response = requests.request("GET", url, headers=headers, data=payload)
    #
    # status_code = response.status_code
    # result = response.text
    # print(f"{status_code}\n{result}")

    value = os.getenv("API_KEY")
    print(value)


if __name__ == '__main__':
    main()

#######################################################################################################################
