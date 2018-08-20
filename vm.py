class VendingMachine:
    def __init__(self):
        self._change = 0

    def run(self, raw):
        tokens = raw.split(" ")
        cmd, params = tokens[0], tokens[1:]

        if cmd == "잔액":
            return "잔액은 " + str(self._change) + "원입니다"
        elif cmd == "동전":
            valid_coins = "10,50,100,500".split(",")
            coin = params[0]

            if coin not in valid_coins:
                return "알 수 없는 동전입니다"

            self._change += int(coin)
            return coin + "원을 넣었습니다"
        elif cmd == "음료":
            known_beverage = "커피"
            price = 150

            beverage = params[0]
            if beverage != known_beverage:
                return "알 수 없는 음료입니다"
            if self._change < price:
                return "잔액이 부족합니다"
            self._change = self._change - price
            return beverage + "가 나왔습니다"
        else:
            return "알 수 없는 명령입니다"
