def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    remaining = amount
    for coin in coins:
        count = remaining // coin
        if count > 0:
            result[coin] = count
            remaining -= coin * count
    return result

def find_min_coins(amount):
    coins = [1, 2, 5, 10, 25, 50]
    max_amount = amount + 1
    dp = [max_amount] * (amount + 1)
    dp[0] = 0
    coin_used = [0] * (amount + 1)
    for a in range(1, amount + 1):
        for coin in coins:
            if coin <= a:
                if dp[a - coin] + 1 < dp[a]:
                    dp[a] = dp[a - coin] + 1
                    coin_used[a] = coin
    if dp[amount] == max_amount:
        return {}
    result = {}
    a = amount
    while a > 0:
        coin = coin_used[a]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        a -= coin
    return result

if __name__ == "__main__":
    amount = 113
    print("Жадібний алгоритм:")
    greedy_result = find_coins_greedy(amount)
    print(greedy_result)

    print("\nДинамічне програмування:")
    dp_result = find_min_coins(amount)
    print(dp_result)
    
    amount = 12345
    print("\nЖадібний алгоритм:")
    greedy_result = find_coins_greedy(amount)
    print(greedy_result)

    print("\nДинамічне програмування:")
    dp_result = find_min_coins(amount)
    print(dp_result)