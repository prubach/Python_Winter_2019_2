from knotprot_download import get_proteins, setup_download_dir, download_link, time_it

def run_single_thread(dir):
    proteins = get_proteins()
    print(len(proteins))
    print(proteins)
    for p in proteins:
        download_link(dir, p)

dir = setup_download_dir()
time_it(run_single_thread, dir)
