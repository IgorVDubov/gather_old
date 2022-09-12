from time import time

def programm_1(vars,stored):
    # print (f'in handler: {vars.ch1=}, {vars.result=}, {stored.a=}')
    vars.result=vars.ch1
    stored.a=5
    # print (f'exit handler: {vars.ch1=}, {vars.result=}, {stored.a=}')
    return stored
# шаблон программ
def func(vars,stored):
    '''
    VARS
        
    STORED
        
    '''
    return stored


import collections
middle10_q = collections.deque([],3)
def middle10(vars,stored):
    '''
    VARS
        in
        out
    STORED
        vals=[val1..val10]
    '''

    return stored


def progVEK(vars,stored):
    '''
    VARS:
    VAR_INPUT value_in :  IN вход канала
	VAR_INPUT gr_work : REAL; END_VAR // граница рботы
                * status_db : USINT; END_VAR // статус отрезка для записи БД
                * length_db : UDINT; END_VAR // длительность отрезка для записи БД
                * time_db : DATE_AND_TIME; END_VAR // начало отрезка для записи БД
                * db_write : BOOL; END_VAR // флаг записи в БД -> DB_in
	VAR_OUTPUT status : текущее состояние (для отображения)
	VAR_INPUT dost :  достоверность аргумент от канала к источнику
	VAR_INOUT write_init : BOOL := 1; END_VAR // принудительная инициализация записи
	VAR_OUTPUT status_bit1 : BOOL; END_VAR // бит1 статуса для HEX канала состояния
	VAR_OUTPUT status_bit2 : BOOL; END_VAR // бит2 статуса для HEX состояния
	
    STORED
    gr_stand  граница простоя
	dost_Timeout : USINT := 5; END_VAR // таймаут НЕдостоверности канала
	min_length : USINT := 20; END_VAR // минимальный отрезок времени сменеы статуса (если меньше, статус не меняется)
	VAR time_now : DATE_AND_TIME; END_VAR
    '''


    return stored
