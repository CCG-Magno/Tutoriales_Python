from timeit import default_timer as timer

def time_taken(fn):
    '''
    Measures the time taken by the function @param fn
    Returns a tuple with result of fn and end-start time

    Parameters:
                    fn (function): A function object to execute and measure time elapsed
                    

            Returns:
                    end - start (int): Integer of the difference of end and start time for the function.
    '''
    start = timer()
    res = fn()
    end = timer()

    return res, end-start
