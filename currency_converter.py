#Create a module currency_converter.py which contains a function 
#that converts one currency to another based on a dictionary of exchange rates. 
#The dictionary should be part of the module.

exchange_rates = {    
    "USD": 37.40,
    "EUR": 39.85,
    "PLN": 8.97,
    "CZK": 1.62,
    "GBP": 46.25,
    "DKK": 5.37,
    "CHF": 42.12,
    "UAN": 1.,
}

def convert_currency(amount, from_currency, to_currency):
    if from_currency not in exchange_rates:
        raise ValueError(f"Unsupported currency: {from_currency}")
    if to_currency not in exchange_rates:
        raise ValueError(f"Unsupported currency: {to_currency}")
 
    converted_amount = amount * exchange_rates[from_currency] / exchange_rates[to_currency]
    return converted_amount


