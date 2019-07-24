''' working with CoinMarketCap API data
This test data is in file CoinMarketCapApi.txt file, just for understanding purpose,
otherwise on each run a request is made to api by (requests.get) which send all the data in response, and by json.loads() it get
stores in api var
'''


import requests
import json

api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?sort=market_cap&start=1&limit=10&cryptocurrency_type=tokens&convert=USD&CMC_PRO_API_KEY=792b9ab5-e448-4b28-8e4d-7fa4c4596f79") #getting api request

api = json.loads(api_request.content) #all data comes in api var

print(api['status']['error_message']) #we can easily fetch satus data in this way because its just a dict with
                                      # status as a key and all other as values
print(api['status']['credit_count'])

#work with data key, whose values are inside a list

print(api['data'][0]['name']) # we enter into key data, now it has values in form of list, therefoe we enter into 0th item
                              # of the list and this 0th item is again a dict, and we print one of its key ("name").

print(api["data"][0]["platform"]["name"]) # we enter into 0th element of data which is in form of dict, it has a key("platform"),
                                          #is again a dict, and here we print one of its key("name").

print(api["data"][0]["cmc_rank"])

print(api["data"][0]["quote"]["USD"]["price"]) #we entered 0th element of data, under quote(dict), under USD(dict), we print its key(price)

print("------------Let us create our portfolio-----------")

coins = [
    {
    "symbol": "LEO",
    "amount_owned" : 2,
    "price_per_coin": 1.35
    },
    {
    "symbol": "CRO",
    "amount_owned" : 5,
    "price_per_coin": 0.04
    }
]
total_pl = 0
for i in range (0,5):
    for coin in coins:
        if api["data"][i]["symbol"] == coin["symbol"]:
            print(api['data'][i]['name']+" - "+api['data'][i]['symbol'])
            total_paid = coin["amount_owned"]*coin["price_per_coin"]
            current_value =  coin["amount_owned"]*api["data"][i]["quote"]["USD"]["price"]
            pl_percoin = api["data"][i]["quote"]["USD"]["price"] - coin["price_per_coin"]
            total_pl_coin = coin["amount_owned"] *  pl_percoin
            total_pl = total_pl + total_pl_coin

            print("Price - ${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]))
            print("total paid amount = ${0:.2f} ".format(total_paid))
            print("No of coins owned", coin["amount_owned"])
            print("current amount = ${0:.2f}".format(current_value))
            print("P/L per coin = ${0:.2f}".format(pl_percoin))
            print("Total profit loss = ${0:.2f}".format(total_pl_coin))
            print("--------------------------- -------")

print("Total profit loss in portfolio = ${0:.2f}".format(total_pl))