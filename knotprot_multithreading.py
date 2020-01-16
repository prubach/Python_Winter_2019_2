from pathlib import Path

from knotprot_download import get_proteins, setup_download_dir, download_link, time_it, create_thumbnail
from threading import Thread
from queue import Queue
from multiprocessing.pool import Pool
from functools import partial
from concurrent.futures import ProcessPoolExecutor

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

##### Create thumbnails ###
def create_thumbnails_single_thread(dir):
    for f in Path(dir).iterdir():
        create_thumbnail((160, 160), f)

##### Create thumbnails in parallel ###
def create_thumbnails_process_pool(dir):
    run_thumbnail = partial(create_thumbnail, (160, 160))
    with ProcessPoolExecutor() as executor:
        executor.map(run_thumbnail, Path(dir).iterdir())


if __name__ == '__main__':
    dir = setup_download_dir()
    print('Run in single thread')
    time_it(run_single_thread, dir)
    print('Now creating thumbnails')
    time_it(create_thumbnails_single_thread, dir)
    dir = setup_download_dir()
    print('MULTIPLE THREADS')
    #time_it(run_workers, dir)
    time_it(run_multi_thread, dir)
    print('Now creating thumbnails')
    time_it(create_thumbnails_process_pool, dir)
