from functools import partial
from multiprocessing import get_context, cpu_count


def run_in_parallel(function, object_list, kwargs={}, cpus=-1, ordered=False):
    '''
    Function to parallelize the application of processes on a list of objects

    Example:

        def my_function(var, param=1):

            a = var ** (2 * param)

            return a

        my_object = [4, 4, 4, 4, 8, 8, 8, 8]
        kwargs={'param': 1000}
        cpus=4

        results = run_in_parallel(my_function, my_object, kwargs=kwargs, cpus=cpus)
        list_results = [i for i in results]
    '''

    if cpus==-1:
        cpus = cpu_count()
    fun_partial = partial(function, **kwargs)
    
    with get_context("spawn").Pool(processes=cpus) as pool:
        if ordered == True:
            result = pool.imap(fun_partial, object_list)
        else:
            result = pool.imap_unordered(fun_partial, object_list)
        pool.close()
        pool.join()

    return result
