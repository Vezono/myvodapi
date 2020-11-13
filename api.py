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

    def login(self, number: str):
        tempToken = self.callSmsWithTempToken(number)
        self.token = self.enterCodeAndGetAccessToken(number, input('Enter your code: '), tempToken)
        print(f'Congrats! You are logged in! Your access token: \n{self.token}')

    def getLinks(self):
        json = {"params": self.params, "requests": {"getLinks": {}}}
        return request('POST', url=self.api_url, json=json).json()

    def getSettings(self):
        json = {"params": self.params, "requests": {"settings": {}}}
        return request('POST', url=self.api_url, json=json).json()

    def callSmsCode(self, number: str):
        json = {"params": self.params, "requests": {"loginV2": {"id": number}}}
        return request('POST', url=self.api_url, json=json).json()

    def callSmsWithTempToken(self, number: str):
        return self.callSmsCode(number)['tempToken']

    def enterSmsCode(self, number: str, code: str, tempToken: str):
        json = {"params": self.params, "requests": {
                "getToken": {"id": number, "tpass": code, "puk": "", "rememberMe": None,
                "tempToken": tempToken, "action": "0", "parentToken": ""}}}
        return request('POST', url=self.api_url, json=json).json()

    def enterCodeAndGetAccessToken(self, number: str, code: str, tempToken: str):
        return self.enterSmsCode(number, code, tempToken)['getToken']['values']['token']

    def getRelPhone(self):
        json = {"params": self.params, "requests": {"getRelPhone": {}}}
        print(json)
        return request('POST', url=self.api_url, json=json).json()

    def getActiveOffer(self):
        json = {"params": self.params, "requests": {"getActiveOffer": {}}}
        return request('POST', url=self.api_url, json=json).json()

    def getBalance(self):
        json = {"params": self.params, "requests": {"balance": {}}}
        return request('POST', url=self.api_url, json=json).json()

    def getInternetCounters(self):
        json = {"params": self.params, "requests": {"countersMainDPIv3": {}}}
        return request('POST', url=self.api_url, json=json).json()

    def getCallsAndSmsCounters(self):
        json = {"params": self.params, "requests": {"countersMainV2": {}}}
        return request('POST', url=self.api_url, json=json).json()

    def getCurrentPlan(self):
        json = {"params": self.params, "requests": {"currentPlan": {}}}
        return request('POST', url=self.api_url, json=json).json()

    def getBonus(self):
        json = {"params": self.params, "requests": {"getBonus": {}}}
        return request('POST', url=self.api_url, json=json).json()

    def getCreditBalance(self):
        json = {"params": self.params, "requests": {"getAMACreditBalance": {}}}
        return request('POST', url=self.api_url, json=json).json()
