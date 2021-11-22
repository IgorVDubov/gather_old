# from collections import namedtuple
# consts = namedtuple('contst',['MODBUS'])
# consts.MODBUS='ModBus'
import consts

HTTPServer=True

ModuleList=[ #{'id':'e41e0a011adc','type':'ModbusTcp','ip':'192.168.1.99','port':'502','unit':0x1, 'address':51, 'regNumber':2, 'function':4, 'period':0.5},
            #{'id':'000de065a65f','type':'ModbusTcp','ip':'192.168.1.98','port':'502','unit':0x1, 'address':0, 'regNumber':16, 'function':2, 'period':0.5}
            #{'id':'Test1','type':'ModbudRS','ip':'','port':'2','unit':0x1, 'address':0, 'regNumber':16, 'function':2, 'period':0.5},
            {'id':'ModuleA','type':'ModbusTcp','ip':'192.168.1.200','port':5020,'unit':0x1, 'address':0, 'count':16, 'function':2, 'format':consts.DI, 'period':0.5,'preprocess':''},
            {'id':'ModuleB','type':'ModbusTcp','ip':'192.168.1.200','port':5020,'unit':0x1, 'address':0, 'count':2, 'function':4, 'format':consts.AI,'period':0.5}
            ]    
'''
Список опрашиваемых модулей
id->str: для идентификации
type->str: тип устройства, реализовано: ModbusTcp
ip->str: ip или testN, тест - эммулятор сигнала с алгоритмом работы задающимся N
port->int: порт модуля
unit->int: номер устройства (в ТСР обычно 1, если ТСР конвертер в 485 - номер в 485-й сети)
address->int: с какого адреса начинаес читать данные
count->int: кол-во адресов для чтения
function->int: модбас функция: реализованы: 2-read_discrete_inputs, 3-read_holding_registers, 4-read_input_registers  
format->str: di - массив бит, ai - массив чисел длинной count
period->float: период опроса в сек
preprocess->str: функция предобработки данных 

''' 
machinesList=[  
            #{'id':4205,'moduleId':'e41e0a011adc','type':'DI','bits':[0,1]},
            #{'id':4206,'moduleId':'e41e0a011adc','type':'DI','bits':[3]},
            {'id':4207,'moduleId':'ModuleA','type':'DI','sourceIndexList':[0,1],'handler':'func_1'},
            {'id':4208,'moduleId':'ModuleB','type':'AI','sourceIndexList':[0]},
            #{'id':4208,'moduleId':'Test2','type':'DI','result':[2]},
            #{'id':4209,'moduleId':'Test2','type':'AI','result':[0]}
            ]
'''
список привязки входов к объекту контроля
id->int: id объекта контроля
moduleId->str: модуль с входами датчиков от  объекта контроля
type->str: di биты состояния, ai- аналоговые данные - одно значение, нет группового чтения
sourceIndexList->list: позиции (индексы с 0) данных массива результата чтения модуля moduleId
handler->str: имя функции обработчика результата (в модуле handler_funcs)
'''            
#
MBServerAdrMap=[
    {'unit':0x1, 'map':{
            'di':[{'id':4207,'addr':0,'len':16}
                  #,{'id':4208,'addr':3,'len':5}
                ],
            'ir':[{'id':4208,'addr':0,'type':'float'}
                  #,{'id':4210,'addr':1,'type':'float'}
                ]
            }
    }]
'''
разметка адресов Модбас сервера для внешнего доступа
unit->int: номер unit-а по умолчанию 1
map ->dict: общее:
                id->int: id объекта контроля
                addr->int: адрес (смещение) первого регистра

            di - discrete_inputs чтение функцией 2
                len->int: кол-во регистров
            hr - holding_registers чтение функцией 3
            ir - input_registers чтение функцией 4
                type->str:      float - 2xWord CD-AB(4Byte);
                                int - 1xWord (2Byte)
                                
                                
'''

MBServerParams={'host':'192.168.1.200','port':5021}
'''
параметры Модбас сервера для внешнего доступа
host, port->str: An optional (interface, port) to bind to.
'''

MySQLServerParams={
    'host': '192.168.1.200',
    'database': 'utrack_db',
    'user': 'utrack',                       #TODO зашифровать!!!!!
    'password' : 'Adm_db78'
}
'''
параметры MySQLServer
'''

