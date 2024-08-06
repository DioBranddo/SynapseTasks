customers = [[1, 3], [2, 2], [2, 1], [7, 3], [7, 1], [8, 3], [9, 2], [20, 21]]

def waiting():
    orders = []
    leavingTime = customers[0][0]
    waitingTime = 0

    for customer in customers:
        
        if leavingTime > customer[0]:
            leavingTime += customer[1]
            orders.append([customer[0], leavingTime])
        else:
            leavingTime = customer[0] + customer[1]
            orders.append([customer[0], leavingTime])

    for order in orders:
        waitingTime += (order[1] - order[0])
    print(orders)
    return waitingTime / len(orders)

def main():
    print(f"\nAverage waiting time for a customer is {waiting():.2f} minutes\n")

if __name__ == '__main__':
    main()
