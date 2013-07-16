# cubetools.py


def generateRows(n):
  rows = []
  n = int(n)
  for z in range(0, n):
    for y in range(0, n):
      for x in range(0, n):
        maxed = 0
        for c in (x,y,z):
          if c==(n-1) or c==0:
            maxed = maxed + 1
        if maxed > 0:
          if maxed == 1:
            type = 'face'
          elif maxed == 2:
            type = 'edge'
          elif maxed == 3:
            type = 'corner'
          rows.append([x, y, z, type])
  return rows

#def scale(val, src, dst):
#  """
#  Scale the given value from the scale of src to the scale of dst.
#  """
#  return ((val - src[0]) / (src[1]-src[0])) * (dst[1]-dst[0]) + dst[0]


def generateTable(tbl, n):
  tbl.clear(keepFirstRow=True)
  rows = generateRows(n)
  n = float(n)
  if n % 2 == 0:
    max = n/2.0 + .5
  else:
    max = (n-1.0)/2.0
  min = -max
  id = 0
  for row in rows:
     tbl.appendRow([id, row[0], row[1], row[2], row[3]])
     id = id + 1

if __name__ == 'main':
  print(repr( generateRows(3) ) )