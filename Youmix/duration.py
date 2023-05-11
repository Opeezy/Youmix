import math

def format_length(length: str) -> str:
    if length / 3600 >= 1:
        hour = math.floor(length / 3600)
        remaining = length % 3600
        if remaining % 60 >= 0:
            minute = math.floor(remaining / 60)
            second = remaining % 60
        hour = f"0{hour}" if len(str(hour)) == 1 else hour
        minute = f"0{minute}" if len(str(minute)) == 1 else minute
        second = f"0{second}" if len(str(second)) == 1 else second
        return f"{hour}:{minute}:{remaining}"
    else:
        if length / 60 >= 1:
            minute = minute = math.floor(length / 60)
            second = length % 60
            minute = f"0{minute}" if len(str(minute)) == 1 else minute
            second = f"0{second}" if len(str(second)) == 1 else second
            return f"00:{minute}:{second}"
        else:
            print(len(str(length)))
            second = f"0{length}" if len(str(length)) == 1 else length
            return f"00:00:{second}"

if __name__ == "__main__":
    new_length = format_length(2599)
    print(new_length)