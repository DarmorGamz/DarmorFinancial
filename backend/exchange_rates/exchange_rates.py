import os
import requests
from dotenv import load_dotenv
load_dotenv()

class ExchangeRate():
    def __init__(self):
        self.api_key = os.getenv("CURRENCY_API_KEY")
        self.url = "https://api.freecurrencyapi.com/v1/latest"

    def ExchangeRateGsad(self, cmd, aVarsIn, aVarsOut):
        match cmd:
            case 'Get':
                if not aVarsIn.get('FromCurrency') or not aVarsIn.get('ToCurrency'):
                    return {"error": "Invalid input vars"}
                base_currency = aVarsIn.get('FromCurrency')
                target_currency = aVarsIn.get('ToCurrency')
                try:
                    # Set up request parameters
                    params = {
                        "apikey": self.api_key,
                        "base_currency": base_currency,
                        "currencies": target_currency
                    }
                    # Make the GET request
                    response = requests.get(self.url, params=params)
                    response.raise_for_status()  # Check for HTTP errors

                    # Parse the JSON response
                    data = response.json()
                    print(data)
                    aVarsOut['Rate'] = data["data"].get(target_currency)
                    return True
                
                except requests.exceptions.RequestException as e:
                    print(f"Error fetching exchange rate: {e}")
                    return False
            case _:
                # Set Response
                return False

        # Set Response
        return True