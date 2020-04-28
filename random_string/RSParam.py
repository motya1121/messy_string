RSP_PW_LOW = {
    'string_type': {
        'hex': False,
        'decimal': True,
        'character': True,
        'symbol': False
    },
    'option': 'lowercase',
    'length': 8,
    'number': 1
}

RSP_PW_MIDDLE = {
    'string_type': {
        'hex': False,
        'decimal': True,
        'character': True,
        'symbol': False
    },
    'option': 'loweruppercase',
    'length': 12,
    'number': 1
}

RSP_PW_HIGH = {
    'string_type': {
        'hex': False,
        'decimal': True,
        'character': True,
        'symbol': True
    },
    'option': 'loweruppercase',
    'length': 16,
    'number': 1
}

RSP_ID = {
    'string_type': {
        'hex': True,
        'decimal': False,
        'character': False,
        'symbol': False
    },
    'option': 'lowercase',
    'length': 8,
    'number': 1
}