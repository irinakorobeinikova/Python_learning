int_item = 10  # todo 1)
comp_item = 18  # todo 2)
multi_int = int_item * 2  # todo 3)
item_2 = True  # todo 4)
item_3 = False  # todo 5)
item_4 = 0  # todo 6)
item_5 = 1  # todo 7)
usd_item = 'usd'  # todo 8)
usd_usd_rate = 1  # todo 9)
eur_item = 'eur'  # todo 10)
usd_eur_rate = 0.86  # todo 11)
uah_item = 'uah'  # todo 12)
usd_uah_rate = 26.23  # todo 13)
chf_item = 'chf'  # todo 14)
usd_chf_rate = 0.91  # todo 15)
rub_item = 'rub'  # todo 16)
usd_rub_rate = 71.88  # todo 17)
byn_item = 'byn'  # todo 18)
usd_byn_rate = 2.46  # todo 19)

if multi_int > comp_item:  # todo 20)
    print('multi_int more than comp_item')

div_int = int_item / 2  # todo 21)
if div_int >= comp_item:  # todo 22)
    print('div_in less than comp_item')

item_1 = 10 + int_item  # todo 23)
if item_1 < comp_item:  # todo 24)
    print('item_1 less than comp_item')
else:
    print('item_1 more or equal than comp_item')

if item_2:  # todo 25)
    print('item_2 =', item_2)
else:
    print('item_2 =', item_3)

if item_3:  # todo 26)
    print('item_3 =', item_2)
else:
    print('item_3 =', item_3)

if item_5:  # todo 27)
    print('item_5 =', item_5)
else:
    print('item_5 =', item_4)

if item_4:  # todo 28)
    print('item_4 =', item_5)
else:
    print('item_4 =', item_4)

currency_convertor = item_2  # todo 29)

if currency_convertor:  # todo 31
    currency_usd = usd_item  # todo 31.1)
    target_currency = eur_item  # todo 31.2)
    target_currency_amount = 50  # todo 31.3)
    currency_result = 0  # todo 31.4)

    if target_currency == 'eur':  # todo 31.5)
        currency_result = target_currency_amount / usd_eur_rate
        print('target_currency_amount, eur_item =', currency_result, usd_item)

    elif target_currency == 'uah':  # todo 31.5.1)
        currency_result = target_currency_amount / usd_uah_rate
        print('target_currency_amount, uah_item =', currency_result, usd_item)

    elif target_currency == 'chf':  # todo 31.6)
        currency_result = target_currency_amount / usd_chf_rate
        print('target_currency_amount, chf_item =', currency_result, usd_item)

    elif target_currency == 'rub':  # todo 31.6)
        currency_result = target_currency_amount / usd_rub_rate
        print('target_currency_amount, rub_item =', currency_result, usd_item)

    elif target_currency == 'byn':  # todo 31.6)
        currency_result = target_currency_amount / usd_byn_rate
        print('target_currency_amount, byn_item =', currency_result, usd_item)

    else:
        print('Unknow currency')    # todo 31.7

    print('currency_convertor =', item_3)   # todo 30)


