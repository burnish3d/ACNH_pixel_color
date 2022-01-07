




if __name__ == "__main__":
  
  d1, d2 = {}, {}
  hist = {}
  with open("keyval/res/ACNH_color_palette", "r") as f1:
    d1['column_headers'] = f1.readline().split(",")

    while s1 := f1.readline():
      vals = s1.split(",")
      d1[vals[3]] = vals[0:3]
      hist[vals[3]] = hist.get(vals[3], 0) + 1

  hist2 = {}
  for k in hist.values():
    hist2[k] = hist2.get(k, 0) + 1
  l = []
  for k,v in hist2.items():
    l.append([k,v])
  l.sort(key=lambda x: x[0])
  [print(elem) for elem in l]

  with open("keyval/res/farben.txt", "r") as f2:

    while s2 := f2.readline():
      vals = s2[1:].split(",")
      d2[vals[1][:-1]] = vals[0]
  
  while True:
    id = input()

    if not id.isnumeric(): break

    hex_code = d2.get(id, -1)

    hvb = d1.get(hex_code, "Value not found")

    print(hvb)

