import requests


def call_api():
    api_url = "https://health.gov/myhealthfinder/api/v3/"
    endpoint = "/topicsearch.json"
    params = {
        'lang': 'en',
        'topicId': '350, 514, 536, 547, 30564, 30584, 30593, 30612, 30613, 30614',
        'categoryId': '15, 19, 27, 28, 91, 92',
        'keyword': 'chlamydia, gonnorhea, breast cancer, cervical cancer, doctor, ovarian cancer, HIV, genetic testing, mammograms, syphilis, std testing',
        }

    try:
        response = requests.get(api_url+endpoint, params=params)

        if response.status_code == 200:
            data = response.json()
            print("api response", data)
        else:
            print(f"error,{response.status_code} - {response.text}")
    except Exception as e:
        print(f"an error occurred, {e}")


call_api()
