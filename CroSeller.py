import asyncio
import cryptocom.exchange as cro
import math
import time

api_key = "******************"
api_secret = "****************"

# Sell for USDT
# pair = cro.pairs.CRO_USDT

# or
# Sell for BTC
pair = cro.pairs.CRO_BTC

# CRO amount
threshold = 1

async def sell():
    account = cro.Account(api_key=api_key, api_secret=api_secret)
    data = await account.get_balance()
    cro_balance = data[cro.Coin(name="CRO")].available
    print(f'CRO balance {math.floor(cro_balance)}')
    if cro_balance > threshold:
        exchange = cro.Exchange()
        price = await exchange.get_price(cro.pairs.CRO_USDT)
        print(f'CRO price {price}')
        result = await account.create_order(pair=pair,side=cro.OrderSide.SELL,type_=cro.OrderType.MARKET,quantity=math.floor(cro_balance))
        print(result)

def main():
    while True:
        try:
            asyncio.run(sell())
            print("sleep 600s")
            time.sleep(600)
        except Exception as E:
            time.sleep(30)
            print(E)


if __name__ == '__main__':
    main()


