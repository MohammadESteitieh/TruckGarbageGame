import random
def choose_object(time,prev_time) :
    if(time_spacing(seconds(time),seconds(prev_time))):
        x = seconds(time)
        bug_prob = (0.4*x)/(x+5) +0.1
        poo_prob = 1-bug_prob
        return random.choices(['images/poo.png', 'images/bug.png'],[poo_prob,bug_prob])
    else:
        return False

def seconds(time) :
    return time/1000.0
        
def time_spacing(time,prev_time):
    
    if((time-prev_time) < max(5-(time/1.25), 0.5)):
        return False
    else:
        return True

def track_objects(id_arr,time, prev_time):
    new_item = choose_object(time,prev_time)
    if(new_item):
        id_arr.append([new_item,random.randint(15, 345),0])
    return id_arr
    
    
    
