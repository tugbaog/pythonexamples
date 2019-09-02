import requests
import logging


def client_method(func):
    def wrapper():
        res = func()
        if res.status_code != 200:
            return None
        else:
            return res.json()

    return wrapper


@client_method
def make_request():
    return requests.get('https://randomuser.me/api/?results=200')


def print_response(json):
    i = 1
    new_dict = {}
    for key, values in json.items():
        if key == 'results':
            for v in values:
                new_dict['title'] = v['name']['title']
                new_dict['first'] = v['name']['first']
                new_dict['last'] = v['name']['last']
                new_dict['username'] = v['login']['username']
                new_dict['password'] = v['login']['password']

                print('User' + str(i) + ': ' + f"title: {new_dict['title']}, first name: {new_dict['first']}, "
                f"last name: {new_dict['last']}, user name: {new_dict['username']}, "
                f"password: {new_dict['password']}")
                i += 1
                logging.basicConfig(filename='dict_logging.log', filemode='w', level=logging.INFO,
                                    format='%(asctime)s - %(message)s')
                logging.info(new_dict)


print_response(make_request())
