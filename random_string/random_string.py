# coding: utf-8
'''
-hex : 11234567890abcde

-decimal: 1234567890
-character: qwertyuiopasdfghjklzxcvbnm
-symbol: !"#$%&'()

-length: 10
'''

import argparse
import random
from . import RSError

BASE_FORMAT = {
    'string_type': {
        'hex': bool,
        'decimal': bool,
        'character': bool,
        'symbol': bool
    },
    'option': str,
    'length': int,
    'number': int
}


def base_string(param: dict):
    HEX_lowercase = "1234567890abcdef"
    DECIMAL = "1234567890"
    CHARACTER_lowercase = "abcdefghijklmnopqrstuvwxyz"
    SYMBOL = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    strings = ''

    st_type = param['string_type']
    st_opt = param['option']

    if st_type['hex'] is True:
        strings += HEX_lowercase
    if st_type['character'] is True:
        strings += CHARACTER_lowercase

    if st_opt == 'lowercase':
        pass
    elif st_opt == 'uppercase':
        strings = strings.upper()
    elif st_opt == 'loweruppercase':
        strings = ''.join(list(set(list(strings + strings.upper()))))

    if st_type['symbol'] is True:
        strings += SYMBOL
    if st_type['decimal'] is True:
        strings += DECIMAL

    return strings


def param_format_check(param: dict, base_param):
    if set(param.keys()) != set(base_param.keys()):
        raise RSError.ParamFormatError

    for key, value in base_param.items():
        if type(value) is dict:
            param_format_check(param=param[key], base_param=base_param[key])
        elif isinstance(param[key], value) is False:
            raise RSError.ParamFormatError


def param_val_check(param: dict):
    st_type = param['string_type']
    st_opt = param['option']

    if st_type['hex'] is True and (st_type['decimal'] is True or st_type['character'] is True or
                                   st_type['symbol'] is True):
        raise RSError.ParamValError('hexとその他のオプションは共用できません')
    elif st_type['hex'] is True:
        pass
    elif st_type['decimal'] is True or st_type['character'] is True or st_type['symbol'] is True:
        pass
    else:
        raise RSError.ParamValError('hexもしくはその他のオプションの中から最低1つ選択してください')

    if st_opt in ['lowercase', 'uppercase', 'loweruppercase']:
        pass
    else:
        raise RSError.ParamValError("'lowercase', 'uppercase', 'loweruppercase'の中から1つ選択してください")

    if 1 <= param['length'] and isinstance(param['length'], int):
        pass
    else:
        raise RSError.ParamValError("文字列の長さが正しくありません")
    if 1 <= param['number'] and isinstance(param['number'], int):
        pass
    else:
        raise RSError.ParamValError("生成数の値が正しくありません")


def random_string(parameter: dict):
    param_format_check(param=parameter, base_param=BASE_FORMAT)
    param_val_check(param=parameter)
    strings = base_string(param=parameter)
    number = parameter['number']
    length = parameter['length']
    ret_str_list = []

    for i in range(0, number):
        temp_string = ""
        for i in range(0, length):
            temp_string += strings[random.randint(0, len(strings) - 1)]
        ret_str_list.append(temp_string)

    return ret_str_list


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='radioの管理を行うプログラム')
    parser.add_argument('--hex', help='16進数(default)', action='store_true')

    parser.add_argument('-d', '--decimal', help='数値を使用する', action='store_true')
    parser.add_argument('-c', '--character', help='文字列を使用する', action='store_true')
    parser.add_argument('-s', '--symbol', help='記号を使用する', action='store_true')

    parser.add_argument('-lo', '--lowercase', help='小文字にする(default)', action='store_true')
    parser.add_argument('-up', '--uppercase', help='大文字にする', action='store_true')
    parser.add_argument('-lu', '--loweruppercase', help='大文字と小文字を両方使う', action='store_true')

    parser.add_argument('-l', '--length', help='長さ', type=int, default=16)
    parser.add_argument('-n', '--number', help='出力する個数', type=int, default=1)
    args = parser.parse_args()

    parameter = {
        'string_type': {
            'hex': False,
            'decimal': False,
            'character': False,
            'symbol': False
        },
        'option': 'lowercase',
        'length': 10,
        'number': 1
    }

    if args.hex is True:
        parameter['string_type']['hex'] = True
    if args.decimal is True:
        parameter['string_type']['decimal'] = True
    if args.character is True:
        parameter['string_type']['character'] = True
    if args.symbol is True:
        parameter['string_type']['symbol'] = True

    if args.lowercase is True:
        parameter['option'] = 'lowercase'
    elif args.uppercase is True:
        parameter['option'] = 'uppercase'
    elif args.loweruppercase is True:
        parameter['option'] = 'loweruppercase'

    if 1 <= args.length and isinstance(args.length, int):
        parameter['length'] = args.length
    if 1 <= args.number and isinstance(args.number, int):
        parameter['number'] = args.number

    strs = random_string(parameter)
    for s in strs:
        print(s)
