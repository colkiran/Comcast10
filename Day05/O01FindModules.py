
import inspect, importlib as implib

if __name__ == '__main__':
    mod = implib.import_module("test")
    for i in inspect.getmembers(mod, inspect.ismodule):
        print(i[0])
