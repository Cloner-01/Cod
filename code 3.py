def detect_type(value):
    value = value.strip()

    # تشخیص بولین
    if value.lower() == "true" or value.lower() == "false":
        return "bool"

    # تشخیص عدد صحیح
    try:
        int_val = int(value)
        if '.' not in value:
            return "int"
    except ValueError:
        pass

    # تشخیص عدد اعشاری
    try:
        float_val = float(value)
        return "float"
    except ValueError:
        pass

    # تشخیص کاراکتر (یک حرف)
    if len(value) == 1:
        return "char"

    # در غیر این صورت، رشته است
    return "string"

# گرفتن چند ورودی از کاربر
print("type the word exit: exit")
while True:
    user_input = input("Insert a value: ")
    if user_input.lower() in ["exit", "خروج"]:
        print("end program")
        break
    result = detect_type(user_input)
    print(f"type value: {result}")
