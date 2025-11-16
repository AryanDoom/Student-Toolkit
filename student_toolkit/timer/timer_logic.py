import time
#simple stuff bro just read up on the timer library
def format_time(seconds):
    return time.strftime("%H:%M:%S", time.gmtime(seconds))

def start_timer_logic(running, current_subject, subjects, start_time):
    if not running and current_subject in subjects:
        running = True
        start_time = time.time() - subjects[current_subject]
    return running, start_time

def stop_timer_logic(running, current_subject, subjects, elapsed):
    if running and current_subject in subjects:
        running = False
        subjects[current_subject] = elapsed
    return running, subjects

def reset_timer_logic(running, elapsed, current_subject, subjects):
    running = False
    elapsed = 0
    if current_subject in subjects:
        subjects[current_subject] = 0
    return running, elapsed, subjects
