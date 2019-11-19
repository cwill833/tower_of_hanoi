from stack import Stack

print("Lets stack!")

# create the stacks for the game
stack = []

left_stack = Stack('Left')
middle_stack = Stack('Middle')
right_stack = Stack('Right')

stack.extend([left_stack, middle_stack, right_stack])

num_disks = int(input("\nHow many disks do you want to play with?\n"))

while num_disks < 3:
   num_disks = int(input("Enter a number greater than or equal to 3\n"))