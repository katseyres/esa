def tuto_set():
  my_set = {1, 2, 3}
  my_set2 = set((3, 4, 5))
  my_set3 = set([5, 6, 7])
  
  print(my_set)
  print(my_set2)
  print(my_set3)

  # Intersection.
  print(my_set & my_set2)
  # Union.
  print(my_set | my_set2)
  # Equality. 
  print(my_set == my_set2)
  # Symmetric difference.
  print(my_set ^ my_set2)

  my_set.add(0)
  print(my_set)
  my_set.add(3)