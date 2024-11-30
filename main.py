def min_coins(coins, target_amount):
    # Initialize a DP array with "infinity" for all amounts
    dp = [float('inf')] * (target_amount + 1)
    
    # Base case: 0 coins are needed to make amount 0
    dp[0] = 0
    
    # Build the DP table
    for coin in coins:
        for amount in range(coin, target_amount + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    # If dp[target_amount] is infinity, it means the target amount cannot be formed
    return dp[target_amount] if dp[target_amount] != float('inf') else -1
