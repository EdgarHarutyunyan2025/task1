#!/usr/bin/env python3

import requests

def convert_currency(qanak,gumar,arjeq):
    try:
        response=requests.get(f'https://v6.exchangerate-api.com/v6/217936093d74ee1fb37fa8f7/latest/{gumar}',params={'APPID':'217936093d74ee1fb37fa8f7'})
    except Exception as e:
        print(type(e))

    if response.status_code==200:
        try:
            data=response.json()
            valut=data['conversion_rates'][f'{arjeq}']
            return (valut*float(f'{qanak}'))
        except:
            print('value error')
    else:
        print('error',response.status_code)

def main():
    qanak= 100
    gumar= USD
    arjeq= EUR

    converted_amount = convert_currency(qanak,gumar,arjeq)
    if converted_amount is not None:
        print("\nConverted amount:")
        print(f"{qanak} {gumar} is equivalent to {converted_amount:.2f} {arjeq}")


if __name__=='__main__':
    main()
