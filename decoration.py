
tab = '_'*10
space = ' '*2

def banner():
    print('\nok dude, this is meme banner :D')

def url_banner(url='pass',req_count=0):
    print()
    print(f'Url: {url}')
    print(f'Total requests: {req_count}')

    print(f'{tab*7}')
    print()

    print(f' STATUS{space*2} SIZE(b){space*3}REQUEST')

    print(f'{tab*7}')
    print()

class Timer:
    
    def __init__(self, time_perf_counter) -> None:
        self.start = time_perf_counter
    
    def show_time(self, time_perf_counter_end):
        print('(!) Execution time -> ',round(time_perf_counter_end-self.start,3))
