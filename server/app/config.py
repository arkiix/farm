import os

# import validators.volgactf
FIRST_NUM = 1
LAST_NUM = 160

CONFIG = {
    # Don't forget to remove the old database (flags.sqlite) before each competition.
    'DEBUG': os.getenv('DEBUG') == '1',

    'TEAMS': {
        f'Team #{i}': f'10.32.{i}.2'
        for i in range(FIRST_NUM, LAST_NUM + 1)
    },
    # 'FLAG_FORMAT': r'CTF\.Moscow\{[a-zA-Z\.0-9_-]+\}',
    # 'FLAG_FORMAT': r'VolgaCTF{[\w-]*\.[\w-]*\.[\w-]*}',
    'FLAG_FORMAT': r'SAAR\{[A-Za-z0-9-_]{32}\}',

    # 'SYSTEM_PROTOCOL': 'ructf_http',
    # 'SYSTEM_URL': 'http://monitor.ructfe.org/flags',
    # 'SYSTEM_TOKEN': '275_17fc104dd58d429ec11b4a5e82041cd2',

    'SYSTEM_PROTOCOL': 'forcad_tcp',
    'SYSTEM_HOST': 'submission.ctf.saarland',
    'SYSTEM_PORT': '31337',
    'TEAM_TOKEN': '4fdcd6e54faa8991',
    # 'SYSTEM_PROTOCOL': 'volgactf',
    # 'SYSTEM_VALIDATOR': 'volgactf',
    # 'SYSTEM_HOST': 'final.volgactf.ru',
    # 'SYSTEM_SERVER_KEY': validators.volgactf.get_public_key('https://final.volgactf.ru'),

    # The server will submit not more than SUBMIT_FLAG_LIMIT flags
    # every SUBMIT_PERIOD seconds. Flags received more than
    # FLAG_LIFETIME seconds ago will be skipped.
    'SUBMIT_FLAG_LIMIT': 100,
    'SUBMIT_PERIOD': 2,
    'FLAG_LIFETIME': 2 * 60 * 10,

    # VOLGA: Don't make more than INFO_FLAG_LIMIT requests to get flag info,
    # usually should be more than SUBMIT_FLAG_LIMIT
    # 'INFO_FLAG_LIMIT': 10,

    # Password for the web interface. This key will be excluded from config
    # before sending it to farm clients.
    # ########## DO NOT FORGET TO CHANGE IT ##########
    'SERVER_PASSWORD': '1234',

    # For all time-related operations
    'TIMEZONE': 'Europe/Omsk',
}
