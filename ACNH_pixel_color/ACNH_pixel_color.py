




def make_lookup():
  """
  Returns dictionary relating ID numbers to h/v/b values
  """
  d1, d2 = {}, {}

  with open(r"ACNH_pixel_color\res\ACNH_color_palette", "r") as f1:
    d1['column_headers'] = f1.readline().split(",")
    while s1 := f1.readline():
        vals = s1.split(",")
        if vals[3] not in d1:
          d1[vals[3]] = " ".join(vals[0:3])


  with open(r"ACNH_pixel_color\res\farben.txt", "r") as f2:
    while s2 := f2.readline():
      vals = s2[1:].split(",")
      d2[vals[1][:-1]] = vals[0]

  d3 = {}

  for k,v in d2.items():
    d3[k] = d1[v]

  return d3

  