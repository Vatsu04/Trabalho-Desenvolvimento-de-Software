import json

xs = {'primeira':'L', 'segunda':'O', 'terceira':'L'}
# lol_string = ' '.join(map(str, xs))
# lol_string = str(xs)
lol_string = json.dumps(xs)
# dict(lol_string)
print(lol_string)