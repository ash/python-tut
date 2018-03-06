text = ' Word '
print('[' + text.rstrip() + ']') # [ Word]
print('[' + text.lstrip() + ']') # [Word ]
print('[' + text.strip() + ']') # [Word]


print('[' + text + ']') # [ Word ]

text = text.strip()
print('[' + text + ']') # [Word]