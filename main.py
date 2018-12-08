import sys
sys.path.append('..')
from katamarkovchain.core.manager import Manager

if __name__ == "__main__":
    text = sys.argv[2]
    number = int(sys.argv[1])
    manager = Manager()
    print(manager.run(text, number))
