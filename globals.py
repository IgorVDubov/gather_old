import os.path

from consts import Consts

machines_idle=dict() #временная замена БД словарь id_станка:текущая_Idle
# PROJECT={'name':'Empty','path':'empty','comment':''}
PROJECT={'name':'Idle demo machines','path':'idledemo','comment':''}
PATH_TO_PROJECT=os.path.join(os.path.dirname(__file__),'projects',
                            PROJECT.get('path','/'))
# project_path= os.path.join(PROJECT.get('path','/'),  'templates'),

# HTTPServerParams={'host':'127.0.0.1','port':8870,'wsserver':'ws://127.0.0.1:8870/ws'}
HTTPServerParams={'host':'127.0.0.1','port':8870,'wsserver':'ws://127.0.0.1:8870/ws'}
CHECK_AUTORIZATION=True

users=[
    {'id': 1, 'first_name': 'Igor', 'middle_name': '', 'second_name': 'Dubov', 'login': 'div', 'pass': '123'},
    {'id': 2, 'first_name': 'Igor', 'middle_name': '', 'second_name': 'Dubov', 'login': 'div1', 'pass': '123'},
    {'id': 3, 'first_name': '5001', 'middle_name': '', 'second_name': '', 'login': 'm_5001', 'pass': 'm777'},
    ]
idle_causes={1:"Авария", 2:"Нет сырья", 3:"Нет задания", 4:"Плановый простой"}

DB_PERIOD=3    #период опроса очереди сообщений для БД DBQuie


CHANNELBASE_CALC_PERIOD=1 #период пересчета каналов в секундах (float) 

MBServerParams={'host':'127.0.0.1','port':5021}
'''
параметры Модбас сервера для внешнего доступа
host, port->str: An optional (interface, port) to bind to.
'''
MBServerParams_E={'host':'127.0.0.1','port':5022}
'''
параметры эмулятора Модбас сервера 
host:str, port:itn  An optional (interface, port) to bind to.
'''
DB_TYPE=Consts.MYSQL        #тип используемой СУБД (доступные в dbclassfactory)
MySQLServerParams={
    'host': '127.0.0.1',
    'database': 'utrack_demo',
    'user': 'utrack',                       #TODO в переменные окружения!!!!!
    'password' : 'Adm_db78'
}
'''
параметры MySQLServer
'''
DB_PARAMS=MySQLServerParams     #параметры для инициализации текущей СУБД
