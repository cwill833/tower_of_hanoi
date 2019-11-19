from stack import Stack

print("Lets stack!")

# create the stacks for the game
stacks = []

left_stack = Stack('Left')
middle_stack = Stack('Middle')
right_stack = Stack('Right')

stacks.extend([left_stack, middle_stack, right_stack])

# grab input from user and makes sure it is >= 3 as this is the minimum amount of disks to have a fun game
num_disks = int(input("\nHow many disks do you want to play with?\n"))

while num_disks < 3:
   num_disks = int(input("Enter a number greater than or equal to 3\n"))

# created first stack with users input
for num in range(num_disks, 0, -1):
    left_stack.push(num)

num_optimal_moves = 2^num_disks - 1

print(f"\nThe fastest you can solve this game is in {num_optimal_moves} moves")

def get_input():
    choices = [node.get_name()[:1] for node in stacks]
    while True:
        for i in (range(len(stacks))):
            name = stacks[i].get_name()
            letter = choices[i]
            print(f"Enter {letter} for {name}")
        user_input = input("")
        if user_input in choices:
            for i in (range(len(stacks))):
                if user_input == choices[i]:
                    return stacks[i]

get_input()