import os

def read(file_name):
    try:
        with open(file_name, 'r') as file:
            print("---> Recalling the Memories from the diary  📖:", file.read())
    except FileNotFoundError:
        print(f"Oops!🫨 The Diary '{file_name}' does not exist. You might want to create it first by writing to it.")

def write(file_name):
    data_input = input("Enter the Memories into the diary 📝 : ")
    with open(file_name, 'w') as file:
        file.write(data_input)
        print("Memories updated Successfully 🥳")

def append(file_name):
    if not os.path.exists(file_name):
        print(f"Oops!🫨 The Diary '{file_name}' does not exist. You cannot append to it.")
        return
    
    data_input = input("Enter the Memories you want to add into the file ✍️: ")
    with open(file_name, 'a') as file:
        file.write(data_input)
        print("Memories appended Successfully 🥳")

def diary():
    while True:
        file_name_input = input('Enter the diary name 💌: ')
        if file_name_input.strip() == "":
            print("Diary name cannot be empty 🫡")
        else:
            file_name = file_name_input + '.txt'
            break

    while True:
        print("\nOptions:")
        print("1. Write Memories into the diary 📝")
        print("2. Recalling Memories from the diary 📖")
        print("3. Append Memories into the diary 📝✍️")
        print("4. Quit👋")

        try:
            choice = int(input("Enter your choice 😌 :"))
        except ValueError:
            print("Invalid input 🫤. Please enter a number.")
            continue

        if choice == 1:
            write(file_name)
        elif choice == 2:
            read(file_name)
        elif choice == 3:
            append(file_name)
        elif choice == 4:
            break
        else:
            print("Invalid choice🥹")

if __name__ == "__main__":
    diary()
