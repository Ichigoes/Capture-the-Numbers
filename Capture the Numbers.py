import re

expression = r"\d+"

while True:

    text = input()

    if not text:
        break

    result = re.finditer(expression, text, re.MULTILINE)

    for matchNum, match in enumerate(result, start=1):
        print(match[0], end=" ")

