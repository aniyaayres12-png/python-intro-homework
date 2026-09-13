list1 = ["Python", "Java", "JavaScript", "C++"]
list2 = ["Python", "Java", "Go", "Ruby"]

set1 = set(list1)
set2 = set(list2)
print(f"Union:   {set1 | set2}")
print(f"Intersection: {set1 & set2}")
print(f"Difference:  {set1 - set2}")
