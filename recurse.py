import sys
def recurse(level):
  print('recurse({})'.format(level))
  if level:
    recurse(level - 1)

  def not_called():
    print('This function is never called.')



def main():
  print('This is the main program.')
  recurse(2)
if __name__ == '__main__' :
  main()
  print(sys.argv)