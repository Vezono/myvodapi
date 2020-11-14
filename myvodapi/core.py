from requests import request


class Session:
    def __init__(self):
        self.api_url = 'https://cscapp.vodafone.ua/eai_smob/start.swe?SWEExtSource=JSONConverter&SWEExtCmd=Execute'
        self.version = "1.9.0"
        self.language = 'ru'
        self.source = "WebApp"
        self.token = None

    @property
    def params(self):
        return {"version": self.version, "language": self.language, "source": self.source, "token": self.token}

    def request(self, method="", params=None, json=None):
        if not params:
            params = {}
        if not json:
            json = {"params": self.params, "requests": {method: params}}
        return request('POST', url=self.api_url, json=json).json()

    def login(self, number: str):
        tempToken = self.callSmsWithTempToken(number)
        self.token = self.enterCodeAndGetAccessToken(number, input('Enter your code: '), tempToken)
        print(f'Congrats! You are logged in! Your access token: \n{self.token}')

    def callSmsWithTempToken(self, number: str):
        return self.callSmsCode(number)["loginV2"]["values"]['tempToken']

    def enterSmsCode(self, number: str, code: str, tempToken: str):
        json = {"params": self.params, "requests": {
                "getToken": {"id": number, "tpass": code, "puk": "", "rememberMe": None,
                "tempToken": tempToken, "action": "0", "parentToken": ""}}}
        return self.request(json=json)

    def enterCodeAndGetAccessToken(self, number: str, code: str, tempToken: str):
        return self.enterSmsCode(number, code, tempToken)['getToken']['values']['token']

    def getLinks(self):
        return self.request('getLinks')

    def getSettings(self):
        return self.request('settings')

    def callSmsCode(self, number: str):
        return self.request('loginV2', {'id': number})

    def getRelPhone(self):
        return self.request("getRelPhone")

    def getActiveOffer(self):
        return self.request("getActiveOffer")

    def getBalance(self):
        return self.request("balance")

    def getInternetCounters(self):
        return self.request("countersMainDPIv3")

    def getCallsAndSmsCounters(self):
        return self.request("countersMainV2")

    def getCurrentPlan(self):
        return self.request("currentPlan")

    def getBonus(self):
        return self.request("getBonus")

    def getCreditBalance(self):
        return self.request("getAMACreditBalance")
