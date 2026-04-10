from functools import wraps
import json
import time
import tracemalloc

def main():
    
    shout_number(9)
    
    n = 7   
    for i in range(n):
        shout_number(i + 1)
    
    print(f"Call count: {shout_number.call_count}")


def log_perf(func):
    
    call_count = 0
    
    @wraps(func) # Adjusts metadata of wrapper func to represent original func
    def wrapper(*args, **kwargs):
        
        nonlocal call_count # I need this because I'm not only reading, but also reassigning 
        

        # Loading in existing information
        try:
            with open("log.json", "r") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {} # Default to strating from scratch

        
        # Start measuring
        tracemalloc.start()
        start = time.time() # Time module shouldn't allocate much memory to skew result
        
        # Execute function
        result = func(*args, **kwargs)
        
        # Stop measuring
        end = time.time()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        # Write data
        data["execution_time_ms"] = round((end - start) * 1000, 6)  # Milliseconds
        data["mem_peak"] = peak
        
        call_count += 1
        wrapper.call_count = call_count # Making the count accessible from outside, for debugging etc
        
        data["call_count"] = call_count
        
        # Writing out resulting values:
        try:
            with open("log.json", "w") as f:
                json.dump(data, f)
        except OSError as e: # Catches things like full disk, permissions, wrong path etc.
            raise RuntimeError("Failed to write log file") from e
        
        return result
        
    
    return wrapper


@log_perf
def shout_number(n):
    print(f"NOW IT'S {n}")
    
    
if __name__ == "__main__":
    main()