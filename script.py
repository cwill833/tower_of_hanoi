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

# show the minimum amount of moves to complete the game
num_optimal_moves = 2**num_disks - 1
print(f"\nThe fastest you can solve this game is in {num_optimal_moves} moves")

# checks the users input to make sure it was a correct stack choice
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

# setting up game / starts it
num_user_moves = 0

while right_stack.get_size() != num_disks:
    print("\n\n\n...Current Stack...")
    for stack in stacks:
        stack.print_items()
    while True:
        print("\nWhich stack do you want to move from?\n")
        from_stack = get_input()
        print("\nWhich stack do you want to move to?\n")
        to_stack = get_input()

        # checks to make sure move was valid before moving disks

        if from_stack.is_empty():
            print("\n\nInvalid Move. Try Again")
        elif to_stack.is_empty() or (int(from_stack.peek()) < int(to_stack.peek())):
            disk = from_stack.pop()
            to_stack.push(disk)
            num_user_moves += 1
            break
        else:
            print("\n\nInvalid Move. Try Again")

print(f"\n\nYou completed the game in {num_user_moves} moves, and the optimal number of moves is {num_optimal_moves}")