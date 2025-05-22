def detect_type(value):
    value = value.strip()

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

# گرفتن ورودی از کاربر
user_input = input("Insert a value:")
result = detect_type(user_input)
print(f"type value: {result}")
