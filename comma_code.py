#!/usr/bin/env python3
def and_add(your_list):
  body = ", ".join(map(str, your_list[:-1]))
  return f"{body} and {your_list[-1]}"
 

spam = ['apples', 'bananas', 'tofu','here','here',123213, 'cats']
print(and_add(spam))


