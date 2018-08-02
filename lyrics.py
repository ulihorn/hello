def repeat_lyrics():
    print_lyrics()
    print_lyrics()

def print_lyrics():
  print("I'm a lumberjack, and I'm okay.")
  print("I sleep all night and I work all day.")

repeat_lyrics()

def print_twice(bruce):
    print(bruce)
    print(bruce)

def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)

line1 = "Bing tiddle "
line2 = "tiddle bang."
cat_twice(line1, line2)

result = print_twice('Bing')
print(type(result))