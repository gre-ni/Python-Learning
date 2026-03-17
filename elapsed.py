class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        import time
        print("Elapsed:", time.time() - self.start)

with Timer():
    sum(range(100000000))