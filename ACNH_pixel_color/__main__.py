




if __name__ == "__main__":
  

  
  while True:
    id = input()

    if not id.isnumeric(): break

    hex_code = d2.get(id, -1)

    hvb = d1.get(hex_code, "Value not found")

    print(hvb)

