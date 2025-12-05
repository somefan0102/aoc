import sys

B = len(sys.argv) > 1 and sys.argv[1] == "b"
count = 12 if B else 2
result = 0

for bank in sys.stdin.readlines():
    bank = bank.strip()
    joltage = ""

    for _ in range(count):
        safe = max(bank[:len(bank)-count+len(joltage)+1])
        joltage += safe
        bank = bank[bank.index(safe)+1:]

    result += int(joltage)

print(result)