"""
    Desinging a simple Scheduler. 
    the Scheduler class maintains tasks with their execution timestamp
    as their key.
    method `run()`, runs them in order of their execution timestamp.
"""
import heapq
import time

class Scheduler:
    def __init__(self):
        self.heap = []

    def schedule_event(self, timestamp, event_name):
        """ schedule at event at a certain timestamp"""
        heapq.heappush(self.heap, (timestamp, event_name))

    def run(self):
        """ run execute the events at the order of their timestamp"""
        while self.heap:
            timestamp, event_name = heapq.heappop(self.heap)
            current_time = time.time()

            if timestamp > current_time:
                time.sleep(timestamp - current_time)

            # Execute the event here
            print(f'execting {event_name} at {time.strftime('%H:%M:%S', time.localtime(timestamp))}')


# Usage
scheduler = Scheduler()
curr = time.time()

scheduler.schedule_event(curr + 4, "Task A")
scheduler.schedule_event(curr + 6, "Task B")
scheduler.schedule_event(curr + 2, "Task C")
scheduler.run()