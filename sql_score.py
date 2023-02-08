import pyodbc
from time import sleep

server = 'servername'
database = 'database'

def score_SQL(queue, alive, lock):
    while alive():
        try:
            pyodbc.connect('Driver{SQL Server};'
                           f'Server={server};'
                           f'Database={database};'
                           'Trusted_Connection=yes;'
                           'Timeout=5;')
            
            # SQL Server connects sucessfully 
            lock.aquire()
            queue.put({'service': 'sql', 'status': 'UP', 'host':server})
            lock.release()

        # SQL Server failed to respond
        except:
            lock.acquire()
            queue.put({'service': 'sql', 'status': 'DOWN', 'host':server})
            lock.release()
        sleep(60)