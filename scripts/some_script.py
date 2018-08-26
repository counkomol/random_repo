import random_repo as rr
import pdb
import matplotlib.pyplot as plt


plt.switch_backend('TkAgg')
plt.style.use('seaborn')


def main():
    print('I am a random script!')

    vals = list()
    for idx in range(1024):
        vals.append(rr.get_float())
    fig, ax = plt.subplots()
    ax.hist(vals)
    plt.show()


if __name__ == '__main__':
    main()
