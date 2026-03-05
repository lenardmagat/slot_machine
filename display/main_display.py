from datetime import datetime
def boxed_menu(credits, lines):
    date_str = datetime.now().strftime("%d/%m/%Y")
    header = f"{credits}     Date: {date_str}"
    content_width = max(len(header), *(len(line) for line in lines))
    box_width = content_width + 4 
    top = "┌" + "─" * box_width + "┐"
    mid = "├" + "─" * box_width + "┤"
    bottom = "└" + "─" * box_width + "┘"
    print(top)
    print(f"│ {header.ljust(box_width - 1)}│")
    print(mid)
    for line in lines:
        print(f"│ {line.ljust(box_width - 1)}│")
    print(bottom)

class main_window:
    def login_screen(self):
        lines = [
            "Enter [L] to login",
            "Enter [C] to create account"
        ]
        boxed_menu("WELCOME TO SLOT MACHINE", lines)
        return input("Enter: ").upper().strip()
    
    def main_screen(self, credits):
        lines = [
            "Enter [B] to bet",
            "Enter [I] to Cash in",
            "Enter [O] to cash out"
        ]
        boxed_menu(f"credits : {credits}", lines)
        return input("Enter: ").upper().strip()
