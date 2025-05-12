def max_profit(prices):
    max_pro=0
    n = len(prices)
    for i in range(1,n):
        if prices[i] > prices[i-1]:
            max_pro+= prices[i] - prices[i-1]

    return max_pro


if __name__ == '__main__':
    stock_prices = [7, 1, 5, 3, 6, 4]
    profit = max_profit(stock_prices)
    print(f"Maximum Profit: {profit}")  # should be 7

    # Additional test cases
    prices1 = [1, 2, 3, 4, 5]
    print(f"Maximum Profit: {max_profit(prices1)}")  # should be 4

    prices2 = [7, 6, 4, 3, 1]
    print(f"Maximum Profit: {max_profit(prices2)}")  # should be 0