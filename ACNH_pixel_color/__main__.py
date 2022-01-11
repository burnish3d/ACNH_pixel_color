
import ACNH_pixel_color




if __name__ == "__main__":
  
  lookup = ACNH_pixel_color.ACNH_pixel_color.make_lookup()
  print("Enter the lookup number of a hex code, the next line will print the values of the hue, vividness, and brightness.")
  while True:
    id = input()

    if not id.isnumeric(): break

    print(lookup.get(id,f"Values not found for {id}"))
