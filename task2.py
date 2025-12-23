
import requests
import datetime

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
    print(response.text)







