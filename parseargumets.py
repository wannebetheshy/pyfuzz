import json

def dictionary_payload(path_to_dict):

    payload = []
    try:
        with open(path_to_dict,'r') as file:
            for line in file:
                element = line.rstrip('\n')
                if element == '':
                    continue
                payload.append(element)
    except FileNotFoundError:
        raise FileNotFoundError(f'We couldn\'t find such file! {path_to_dict}')

    return payload


class info:

    def __init__(self, list_args):
        self.list_args = list_args

    def arguments_info(self, req_arg):
        fullnames_args = {
            '-u':'url',
            '-d':'dictionary',
            '-s':'specword',
            '-r':'reqspertime',
            '-P':'post_data'
        }
        return fullnames_args.get(req_arg, False)
    
    def check_arglist(self, dict_arg):
        
        # if command is empty
        if len(dict_arg) == 0:
            return [False, KeyError('Please specify at least 2 arguments ( url (-u) + dictionary (-d) )')]
        
        # wordlist errors
        if 'dictionary' not in dict_arg.keys():
            return [False, KeyError('Please specify dictionary (e.g. /home/kali/fuzzlist.txt on Linux Systems)')]
        
        # special word errors
        if 'specword' not in dict_arg.keys():
            special_word = 'PUFF'
        else:
            special_word = dict_arg['specword']
        
        # url errors
        if 'url' not in dict_arg.keys():
            return [False, KeyError('Please specify url (e.g. https://example.com/SPECWORD)')]
        if special_word not in dict_arg['url'] and 'post_data' not in dict_arg.keys():
            return [False, KeyError('Please write special word in the url or use default one (e.g. https://example.com/PUFF)')]
        
        # requests per sec errors
        if 'reqspertime' in dict_arg.keys():
            try:
                if int(dict_arg['reqspertime']) <= 0:
                    return [False, ValueError('Please write positive number of requests (e.g. -r 5)')]
            except ValueError:
                raise ValueError('Please write integers (e.g. -r 10)')
            except Exception as Exception_:
                raise Exception_
            
        return [True,'no mistakes']

    def create_arglist(self):

        # i didn't want to write self.list_args multiple times
        list_arg = self.list_args
        correctdict_arg = {}
        len_arg = len(self.list_args)

        for i in range(1, len_arg, 2):

            argument_fullname = self.arguments_info(list_arg[i])

            if not argument_fullname:
                raise KeyError('Please specify proper arguments (e.g. -u https://example.com for url)')

            try:
                correctdict_arg[argument_fullname] = list_arg[i+1]
            except IndexError:
                raise IndexError('Please write data to all arguments (e.g. -u https://example.com etc.)')
        
        if not self.check_arglist(correctdict_arg)[0]:
            raise self.check_arglist(correctdict_arg)[1]
        
        return correctdict_arg
    
    @property
    def assign_args(self):
        URL, WORDLIST, SPECWORD, MAXREQSPERTIME, POST_DATA = 'False', 'False', 'PUFF', 10000000000000000, False
        
        arguments_information = self.create_arglist()

        for el in arguments_information.keys():
            if el == 'url':
                URL = arguments_information[el]
            if el == 'dictionary':
                WORDLIST = dictionary_payload(arguments_information[el])
            if el == 'specword':
                SPECWORD = arguments_information[el]
            if el == 'reqspertime':
                MAXREQSPERTIME = int(arguments_information[el])
            if el == 'post_data':
                POST_DATA = json.loads(arguments_information[el])

        return URL, WORDLIST, SPECWORD, MAXREQSPERTIME, POST_DATA 

# a = info(['file','-d','dictionary.txt:sssd','-u','https://youtube.com/sssd']).assign_args