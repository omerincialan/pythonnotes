import statistics
import matplotlib.pyplot

def main() :
    show_stats('worldpop.txt')
    show_stats('presheights.txt')

def show_stats(filename) :
    data = []
    for line in open(filename) :
        fields = line.rsplit(" ", 1)
        data.append(int(fields[1]))
    mean = statistics.mean(data)
    median = statistics.median(data)
    stdev = statistics.stdev(data)
    print("Mean: %.0f\nMedian: %.0f\nStandard deviation: %.0f" 
       % (mean, median,stdev))

    matplotlib.pyplot.bar(range(len(data)), data)
    matplotlib.pyplot.show()

main()


