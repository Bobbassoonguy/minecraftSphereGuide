def rainbow():
  r, g, b = 255, 0, 0
  for g in range(256):
    yield r, g, b
  for r in range(255, -1, -1):
    yield r, g, b
  for b in range(256):
    yield r, g, b
  for g in range(255, -1, -1):
    yield r, g, b
  for r in range(256):
    yield r, g, b
  for b in range(255, -1, -1):
    yield r, g, b

print(rainbow())