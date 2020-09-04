import requests

class RestAPIConsumingUtilities():

    @staticmethod
    def rest_response_fetch(url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.json(),True,"Success"
        elif response.status_code == 404:
            return None,False,f"API {url} Not Found"
        elif response.status_code == 500:
            return None,False,f"API {url} Internal Server Error"
        