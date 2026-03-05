import msvcrt
class function_helper:
    def input_password(self, prompt="Password: "):
        print(prompt, end="", flush=True)
        password = ""
        while True:
            char = msvcrt.getch()

            if char in (b'\r', b'\n'):     
                print()
                break

            elif char == b'\x08':          
                if len(password) > 0:
                    password = password[:-1]
                    print("\b \b", end="", flush=True)

            elif char == b'\x03':          
                raise KeyboardInterrupt
            
            else:
                try:
                    decoded = char.decode()
                except:
                    continue
                password += decoded
                print("*", end="", flush=True)
        return password