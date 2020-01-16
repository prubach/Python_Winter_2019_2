from knotprot_download import get_proteins, setup_download_dir, download_link, time_it
from threading import Thread
from queue import Queue
from multiprocessing.pool import Pool
from functools import partial

def run_single_thread(dir):
    proteins = get_proteins()
    print(len(proteins))
    print(proteins)
    for p in proteins:
        download_link(dir, p)

### Download using separate threads ###
class DownloadWorker(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            dir, prot = self.queue.get()
            try:
                download_link(dir, prot)
            finally:
                self.queue.task_done()

def run_workers(dir):
    proteins = get_proteins()
    #print(len(proteins))
    #print(proteins)
    queue = Queue()
    for n in range(30):
        worker = DownloadWorker(queue)
        # Don't wait until this thread exits, stop it when main thread exits
        worker.daemon = True
        worker.start()
    for p in proteins:
        queue.put((dir, p))
    queue.join()

#####

#### Using Multiprocessing ####

def run_multi_thread(dir):
    proteins = get_proteins()
    #print(len(proteins))
    #print(proteins)
    download = partial(download_link, dir)
    with Pool(4) as p:
        p.map(download, proteins)

if __name__ == '__main__':
    dir = setup_download_dir()
    #time_it(run_single_thread, dir)
    #time_it(run_workers, dir)
    time_it(run_multi_thread, dir)
