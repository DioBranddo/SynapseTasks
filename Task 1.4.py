customers = [[1, 3], [2, 2], [2, 1], [7, 1], [8, 3], [9, 2]]


def waiting():
    orders = []
    sum = customers[0][0]
    waitingTime = 0

    for customer in customers:
        sum += customer[1]
        if sum > customer[0]:
            orders.append([customer[0], sum])
        else:
            sum = customer[0]+customer[1]
            orders.append([customer[0], sum])

    for order in orders:
        waitingTime += (order[1]-order[0])

    return(waitingTime/len(orders))


def main():
    print(f"\nAverage waiting time for a customer is {waiting():.2f} minutes\n")


if __name__ == '__main__':
    main()