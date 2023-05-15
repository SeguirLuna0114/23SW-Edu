from itertools import count

for page_idx in count():
    if page_idx >= 5:
        break
    print(page_idx)
    # 0
    # 1
    # 2
    # 3
    # 4
print('finished')
