import requests
import os
# import pprint
# pr_pr = pprint.PrettyPrinter(indent=4)

crypto_pairs_to_watch = ["BTCEUR"]
# Additional fees set from exchange
# to set environment variables use: export M_API_KEY=000000
m_buy_fee = float(os.getenv("M_BUY_FEE", 0))  # float percentage, eg 10 == 10 %, max 100.0
m_sell_fee = float(os.getenv("M_SELL_FEE", 0))  # float percentage, eg 10 == 10 %, max 100.0

base_url = "https://api.kraken.com/0/public/Ticker"
# m_agent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0"
m_agent = "My Price Checker"
m_headers = {"User-Agent": m_agent}
m_params = {"pair": crypto_pairs_to_watch}  # ?key=value
m_timeout = 10  # in sec


m_resp = requests.get(base_url, headers=m_headers, params=m_params, timeout=m_timeout)
# print(m_resp.url)

if m_resp.status_code == requests.codes.ok:
    # print(m_resp.text)

    m_resp_json = m_resp.json()  # class 'dict'
    # pr_pr.pprint(m_resp_json)  # pretty print response data

    current_price = float(m_resp_json["result"]["XXBTZEUR"]["c"][0])
    print("Current BTC price: " + str(current_price))
    # do something with the data here ...
    real_buy = current_price + (m_buy_fee * 0.01) * current_price
    real_sell = current_price - (m_sell_fee * 0.01) * current_price

    print("Current BUY price: " + str(real_buy) + " EUR (incl fee)")
    print("Current SELL price: " + str(real_sell) + " EUR (incl fee)")

else:
    print("Sorry something went wrong...")
    print("Status code: " + str(m_resp.status_code))

print("Done, exiting now ...")
