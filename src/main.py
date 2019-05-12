import numpy as np
import sort_implementation as si


def main():
    print('Creating random vector from 0 to 9:')
    a = np.arange(10)
    np.random.shuffle(a)
    print(a)
    a = si.merge_sort(a)
    print('sorted vector:')
    print(a)

if __name__ == '__main__':
    main()
