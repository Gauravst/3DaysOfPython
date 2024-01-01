import os

def main():
    while True:
        text = input("Enter what you want to speak: ")

        if text == "q":
            os.system("say 'bye bye'")
            break

        command = f"say '{text}'"  
        os.system(command)

if __name__ == '__main__':
    main()

