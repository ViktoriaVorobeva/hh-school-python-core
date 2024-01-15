import time

def time_decorator(func):
    def wrapper(*args, **kwargs):
        print (f'Start for {func.__name__}')
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'Lead time: {(end_time - start_time)* 1000} mcs')
        print('---------------------------')
        
        return result
    
    return wrapper