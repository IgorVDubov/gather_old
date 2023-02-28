CLIENT_VERSION=0.1
STATE_ARG='args.saved_status'
TECH_IDLE_ARG='args.tech_timeout'
STATE_TIME_ARG='args.saved_time'
CAUSEID_ARG='args.cause'
CAUSE_TIME_ARG='args.cause_time'
IDLE_HANDLERID_ARG='args.idle_handler_id'
IDLE_STATES=(1,2) # состояния при которых фиксируется простой
CAUSE_CHECK_TIMEOUT=120 # таймаут указания причины простоя
# IDLE_CAUSES={-1:'Не подтверждена',0:'Технологический простой',1:"Авария", 2:"Нет сырья", 3:"Нет задания", 4:"Плановый простой"}
IDLE_CAUSES={1:'Не подтверждена',2:'Технологический простой',3:"Авария", 4:"Нет сырья", 5:"Нет задания", 6:"Плановый простой"}
NOT_CHEKED_CAUSE=1  # причина простоя по умолсанию (если не указана)
TECH_IDLE_ID=2
STATES =['N/A', 'Откл', 'Простой', 'Работа']
TIME_FORMAT='%Y-%m-%dT%H:%M:%S'

DEFAULT_CAUSES=(1,2)
ALLOWED_MACHINES={2020:['192.168.1.200', '127.0.0.1']} # id каналов и разрешенные ip, к которым могут подключаться клиенты контроля простоя через запрос ?m=id

OPERATORS={1111:{'name':'Петров А.П.'},2222:{'name':'Попов-Петровский А.Р.'}}