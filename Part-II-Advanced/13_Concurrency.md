# 13 Concurrency
## 13.1 Basics
- the art of making computers appearing to do multiple tasks at once
- in the past this meant to switch really fast between processes
- nowadays it can mean to use several processors to do several tasks at once
- often concurrency is used to further process data while waiting for i/o to happen
- e.g. a server that respond to a request while waiting for the next
- the rule is "I/O => threading", "CPU heavy processing => process"

## 13.2 Threads
### 13.2.1 Basics
- a thread is a "lightweight" process (a subprocess that shares some ressources(related to the process) with other subprocesses)
- in python threads are represented by the "Thread" object from the "threading" module(built-in)
- every program has at least one thread(belonging to the process) called "main thread"
- to construct a new thread the "Thread" object has to be inherited from and the "run" method has to be implemented
- in threads all state is shared by default
- the thread object is started by the "start()" method // not by the run method

### 13.2.2 Example
```python
    from threading import Thread

    class InputReader(Thread):
        def run(self):
            self.line_of_text = input("enter some text while i calculate: ")

    thread = InputReader()
    thread.start()

    count = result = 1
    while thread.is_alive():
        result = count * count
        count += 1

    print(f"calculated squares up to {count} result = {result}")
    print(f"while you typed {thread.line_of_text}")
```

### 13.2.3 Additional Info
- the access to all the programs memory can easy cause inconsistencies (one thread changes a modul var and the other threads are railed off)
- the turn order of threads is random, the one that goes first this round could be the last next round
- the solution is to "synchronize" access to any shared variable
- python provides the "queue.Queue" class to do so
- python forbids the execution of threads for the same process on different cores! // this is called global interpreter lock(GIL) NO PARALLEL PROCESSING WITH THREADS
- threads are cost intensive(compared to other methods of concurrency in python), manage all the threads will take ressources
- this can be adressed by the "ThreadPool" feature

## 13.3 Multiprocessing
### 13.3.1 Basics
- a process is a entity that requests ressources from the processor
- every process gets own memory and own computing time in the schedule => NO SHARED MEMORY
- the multiprocessing module(built-in) allows the creation of processes (it creates an entirely separate copy of the python interpreter running for each process)
- has similar interfaces as threading
- the copied python interpreter process imports the current module! // means if the processes are created on modul level AND NOT GATEKEEPED it will create processes recursively til the computer crashes

## 13.3.2 Example
```python
    from threading import Thread, get_ident
    from multiprocessing import Process, cpu_count
    import time
    import os

    class ProcessTest(Process):
        def run(self):
            print(os.getpid())
            for i in range(int(2e8)):
                pass

    class ThreadTest(Thread):
        def run(self):
            print(get_ident())
            for i in range(int(2e8)):
                pass

    def processes_going():
        print("process test")
        processes = [ProcessTest() for i in range(6)]
        start = time.time()
        for p in processes:
            p.start()
        for p in processes:
            p.join() # main process will wait til the next process is done before advancing further
        print(f"took {time.time() - start} seconds")

    def threads_going():
        print("thread test")
        threads = [ThreadTest() for i in range(6)]
        start = time.time()
        for t in threads:
            t.start()
        for t in threads:
            t.join() # main thread will wait til the next thread is done before advancing further
        print(f"took {time.time() - start} seconds")

    if __name__ == "__main__":
        threads_going()
        print()
        processes_going()
```

## 13.4 Multiprocessing Pools
### 13.4.1 Basics
- there is NO reason to have more proccesses as there are cpus on the system
    1. on one proccessor one process can run at each given time
    2. each process consumes ressources with a full copy of the interpreter
    3. communication between processes is expensive
- it is better(when in need of multiprocessing) to create as many processes as there are cpus at program start rather than create a process when a task comes up
- multiprocessing pools are the way to manage multiple processes
- the "multiprocessing.Pool" provides the functionality
- it restricts the places of interactions between processes to make it easyer to keep track
- the general work of interprocess communication in python is:
    - objects in one proccess are pickled
    - then passed in an os pipe
    - then another process can retreive the data from the pipe
    - then the data is unpickled
    - the request work is done
    - the data is pickled
    - the pickled data than passed in an os pipe
    - the requested process can then get the pickled data from the pipe
    - the data can be unpickled and accessed
- this is a ressource costing process (it is often more time consuming than to let the original process do the work alone, pickling is expensive) => hold the interprocess communication to a minimum 
> only adventageous when a lot of cpu processing has to be done

### 13.4.2 Example
```python
    import random
    from multiprocessing.pool import Pool

    def prime(value):
        factors = list()
        divisor = 2
        while value > 1:
            if value % divisor == 0:
                factors.append(divisor)
                value = value/divisor
                divisor -= 1
            divisor += 1 
        return factors

    if __name__ == "__main__":
        pool = Pool()

        to_factor = [random.randint(1e5, 5e7) for i in range(20)]
        results = pool.map(prime, to_factor)
        for value, factors in zip(to_factor, results):
            print(f"the factors of {value} are {factors}")
```
- what happens is:
    - by default Pool() will create a seperate process for each cpu
    - the map method accepts a function and an iterable
    - the pool then pickles each of the values within the iterable and passes it to an idling process
    - the process executes the function on it, pickles the result, and passes it back to the pool, and marks itself as idling to the pool
    - if the pool has more work it assigns the next item to the process
- after all items are processed, it returns the result to the original process, which waits til that moment

### 13.4.3 Additional Info
- "map_async(function, iterable)" -> map_object => same as map but the main-process wont be supended
- "map_object.ready() / map_object.wait()" => check if all items are processed
- "map_object.get_results()" => return the list with the currenty aviable processed items (will clear this)
- "closed()" => the current queue will be processed, afterwards the processes will be terminated
- "terminated()" => left processes running the current task, but then will be terminated

## 13.5 Queues
- a queue is a container where objects can be dumped for other processes to take them out
- python provides the "queue" modul(built-in)
- any pickable object can be send into a python queue
- the queue modul comes in handy for decentralized processing => distribute a task over more systems and merge the result at the end

## 13.6 Futures
### 13.6.1 Basics
- futures are wrapper around "multiprocessing pools" and or "thread pools"
- they provide a clean API
- the future wraps a function call and runs it in the background within an own thread/process

### 13.6.2 Example
```python
    from concurrent.futures import ThreadPoolExecutor
    from pathlib import Path
    from os.path import sep as pathsep
    from collections import deque

    def find_files(path, query_string):
        subdirs = list()
        for p in path.iterdir():
            full_path = str(p.absolute())
            if p.is_dir() and not p.is_symlink():
                subirs.append(p)
            if query_string in full_path:
                print(full_path)
        return subdirs

    query = ".py"
    futures = deque()
    basedir = Path(pathsep).absolute()

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures.append(executor.submit(find_files, query))
        while futures:
            future = futures.popleft()
            if future.exception():
                continue
            elif future.done():
                subdirs = future.result()
                for subdir in subdirs:
                    futures.append(executor.submit(find_files, subdir, query))
            else:
                futures.append(future)
```
> look for the asyncIO module if the project gets larger