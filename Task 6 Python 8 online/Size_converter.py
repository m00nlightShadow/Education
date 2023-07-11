print('\nThis program converts international clothes size in clothes size of other countries\n')


def convert(size, country):
    clothing = {
        'XXS': {'russia': '42', 'Germany': '36', 'USA': '8', 'France': '38', 'GB': '24'},
        'XS': {'russia': '44', 'Germany': '38', 'USA': '10', 'France': '40', 'GB': '26'},
        'S': {'russia': '46', 'Germany': '40', 'USA': '12', 'France': '42', 'GB': '28'},
        'M': {'russia': '48', 'Germany': '42', 'USA': '14', 'France': '44', 'GB': '30'},
        'L': {'russia': '50', 'Germany': '44', 'USA': '16', 'France': '46', 'GB': '32'},
        'XL': {'russia': '52', 'Germany': '46', 'USA': '18', 'France': '48', 'GB': '34'},
        'XXL': {'russia': '54', 'Germany': '48', 'USA': '20', 'France': '50', 'GB': '36'},
        'XXXL': {'russia': '56', 'Germany': '50', 'USA': '22', 'France': '52', 'GB': '38'}
    }
    if size in clothing:
        if country in clothing[size]:
            return clothing[size][country]


my_size = input('Choose your size (XXS, XS, S, M, L, XL, XXL, XXXL):\n')
my_country = input('Choose country you want to convert in (russia, Germany, USA, France, GB):\n')
my_choise = convert(my_size.upper(), my_country)

if my_choise:
    print(f'International size "{my_size}" in {my_country} is {my_choise}')
else:
    print('Please enter the options given in brackets. Try again')
