seconds_input = int(input("3600"))
hours = seconds_input // 3600
remaining_seconds = seconds_input % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60
print(f"{seconds_input}, {hours} , {minutes} , {seconds} ")