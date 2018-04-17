'''
    Za Wikipedią:

    programowanie proceduralne – paradygmat programowania zalecający 
    dzielenie kodu na procedury, czyli fragmenty wykonujące ściśle określone 
    operacje. Procedury nie powinny korzystać ze zmiennych globalnych (w miarę 
    możliwości), lecz pobierać i przekazywać wszystkie dane (czy też wskaźniki 
    do nich) jako parametry wywołania.

    Czyli to co robiliśmy do tej pory. Zwróćcie uwagę, że dane i procedury (funkcje)
    nie są ze sobą ściśle powiązane!
'''


def process_data(data):
    '''
        Does something with data and returns result
    '''
    return data * 2


def process_data_in_another_way(data):
    '''
        Does another thing with data and returns result
    '''
    return data % 2


if __name__ == '__main__':
    data = int(input('A number, please?'))
    processed_data = process_data(data)
    processed_data = process_data_in_another_way(processed_data)
    print('Processed data, result: {result}'.format(result=processed_data))
