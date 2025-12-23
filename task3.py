
import requests
import datetime
import matplotlib.pyplot as plt


if __name__ == '__main__':
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(7)
    end_date_req  = end_date.strftime("%Y%m%d")
    start_date_req = start_date.strftime("%Y%m%d")

    params = {
        "start": start_date_req,
        "end": end_date_req,
        "valcode": "usd",
        "sort": "exchangedate",
        "order": "desc",
        "json": ''
    }

    response = requests.get("https://bank.gov.ua/NBU_Exchange/exchange_site", params)
    data = response.json()

    x = [item["exchangedate"] for item in data]
    y = [item["rate"] for item in data]

    plt.plot(x, y)
    plt.xlabel("Дата")
    plt.ylabel("Курс USD (грн)")

    plt.show()









