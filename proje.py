import tweepy
import time
class ApiGiris:
    def __init__(self):
        self.__api_key=""
        self.__api_secret=""
        self.__accest_token=""
        self.__access_secret=""
        self.auth=tweepy.OAuthHandler(self.__api_key,self.__api_secret)
        self.auth.set_access_token(self.__accest_token,self.__access_secret)
        self.api=tweepy.API(self.auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
    def hometimeline(self):
        giris = self.api
        home = giris.home_timeline(count=20,include_entities=False,include_rts=False)
        b=1
        for a in home:
          if a.favorited == False:
            if "@" not in a.text:
                giris.create_favorite(a.id)
                print(str(b),a.text)
                time.sleep(1)
                b+=1
islem = ApiGiris()

if __name__ =="__main__":
    islem.hometimeline()