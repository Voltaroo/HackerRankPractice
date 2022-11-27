# Problem: https://www.hackerrank.com/challenges/birthday-cake-candles/problem
# Points: 10.00


def birthdayCakeCandles(candles):
    tallest_candle = max(candles)
    count_tallest = sum([1 if candles[i] == tallest_candle else 0 for i in range(len(candles))])
    return count_tallest