def max_profit(prices):
    min_num=prices[0]
    maximum_profit=0
    n = len(prices)
    for i in range (1,n):
        maximum_profit=max(prices[i]-min_num,maximum_profit)
        if prices[i] < min_num:
            min_num=prices[i]

    return maximum_profit


if __name__ == '__main__':
    stock_prices = [7, 1, 5, 3, 6, 4]
    profit = max_profit(stock_prices)
    print(f"Maximum Profit: {profit}")  # should be 5

    # Additional test cases
    prices1 = [7, 6, 4, 3, 1]
    print(f"Maximum Profit: {max_profit(prices1)}")  # should be 0 (no profit possible)

    prices2 = [1, 2, 3, 4, 5]
    print(f"Maximum Profit: {max_profit(prices2)}")  # should be 4 (buy at 1, sell at 5)