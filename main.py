from queue import Queue
from http_score import score_HTTP
from ssh_score import score_SSH
from ftp_score import score_FTP
from sql_score import score_SQL
from smtp_score import score_SMTP
from icmp_score import score_ICMP
from dns_score import score_DNS
from smb_score import score_SMB
import threading

shared_queue = Queue()


def main():
    lock = threading.Lock()
    alive_bool = True
    alive = lambda : alive_bool
   # spawn the threads
    t1 = threading.Thread(target=score_HTTP, args=(shared_queue, alive, lock, 'http://google.com'))
    t1.start()
    t2 = threading.Thread(target=score_SMTP, args=(shared_queue, alive, lock, 'localhost'))
    t2.start()
    t3 = threading.Thread(target=score_ICMP, args=(shared_queue, alive, lock, 'localhost'))
    t3.start()
    t4 = threading.Thread(target=score_DNS, args=(shared_queue, alive, lock, '8.8.8.8'))
    t4.start()
    t5 = threading.Thread(target=score_SSH, args=(shared_queue, alive, lock, 'localhost'))
    t5.start()
    t6 = threading.Thread(target=score_SQL, args=(shared_queue, alive, lock))
    t6.start()
    t7 = threading.Thread(target=score_FTP, args=(shared_queue, alive, lock, 'localhost'))
    t7.start()
    t8 = threading.Thread(target=score_SMB, args=(shared_queue, alive, lock, 'localhost'))
    t8.start()

    # main loop
    try:
        while(True):
            print(shared_queue.get())
    except KeyboardInterrupt:
        print('exiting')

    alive_bool = False
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()


if __name__ == '__main__':
    main()

