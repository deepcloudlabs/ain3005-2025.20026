import gc

gc.set_debug(gc.DEBUG_LEAK)
while True:
    a = [1] * 10_000_000
    del a
