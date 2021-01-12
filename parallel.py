'''

Function to parallelize the application of processes on a list of objects

Example:

def my_function(constant, optional=1):

    a = constant ** (2 * optional)

    return a

my_object = [4, 4, 4, 4, 8, 8, 8, 8]
kwargs={'optional': 100000000}
cpus=4

results = run_in_parallel(my_function, my_object, kwargs=kwargs, cpus=cpus)
list_results = [i for i in results]

'''

from functools import partial
from multiprocessing import get_context, cpu_count


def run_in_parallel(function, object_list, kwargs=None, cpus=-1, ordered=False):

    if cpus==-1:
        cpus = cpu_count()
    fun_partial = partial(function, **kwargs)

    if ordered == True:
        with get_context("spawn").Pool(processes=cpus) as pool:
            result = pool.imap(fun_partial, object_list)
            pool.close()
            pool.join()
    else:
        with get_context("spawn").Pool(processes=cpus) as pool:
            result = pool.imap_unordered(fun_partial, object_list)
            pool.close()
            pool.join()

    return result