def clean_request(response):
    temp_kelvin = response ['main']['temp']
    temp_celsius = temp_kelvin-273.15
    return temp_celsius
        