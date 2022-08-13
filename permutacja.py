import itertools
lista=[1,2,3,4,5,6,7,8,9,10]

#print(list(itertools.permutations(lista)))
def permutation(s):
 if len(s) == 1:
  return [s]

 perm_list = []
 for a in s:
  remaining_elements = [x for x in s if x != a]
  z = permutation(remaining_elements)

  for t in z:
   perm_list.append([a] + t)

 return perm_list


print(permutation(lista))

