from brownie import educoin
from scripts.helpful_scripts import get_account
from web3 import web3 


initial_supply = web3.toWei(10000, 'ether')

defmain():
    account = getaccount()
    Edu_Coin = EduCoin.deploy(initial_supply, {"from": account})

print(Edu_Coin.name())