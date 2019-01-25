
import random

team_name = 'Blake Werlingers team' # Only 10 chars displayed.
strategy_name = 'RNG'
strategy_description = 'The computer picks a random number and selects either c or b because of it'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.'''
    a = random.int(1,2)
    if a == 1:
        return 'c'
    else:
        return 'b'
    
            