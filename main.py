import time

def find_coins_greedy(amount, coins):
    result = {}

    for coin in coins:
        if amount // coin > 0:
            result[coin] = amount // coin
            amount %= coin

    return result

def find_min_coins(amount, coins):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [-1] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    result = {}
    remaining = amount
    while remaining > 0:
        coin = coin_used[remaining]
        result[coin] = result.get(coin, 0) + 1
        remaining -= coin

    return result

# Приклад використання функцій
coins_set = [50, 25, 10, 5, 2, 1]

amount_to_return = 113

greedy_result = find_coins_greedy(amount_to_return, coins_set)
min_coins_result = find_min_coins(amount_to_return, coins_set)

print("Greedy Algorithm result:", greedy_result)
print("Dynamic Programming result:", min_coins_result)

# Порівняння ефективності
amounts_to_test = [200, 580, 1043, 5020, 11321, 50678, 105680]

for amount in amounts_to_test:
    start_time = time.time()
    find_coins_greedy(amount, coins_set)
    greedy_time = time.time() - start_time

    start_time = time.time()
    find_min_coins(amount, coins_set)
    dp_time = time.time() - start_time

    print(f"Amount: {amount}, Greedy Time: {greedy_time:.6f}s, DP Time: {dp_time:.6f}s")