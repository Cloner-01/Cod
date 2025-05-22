def detect_type(value):
    value = value.strip()
    
    #تشخیص بولین 
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


inputs = ["5", "3.14", "a", "hello", "world!","True","False", "42.0"," ", "007"]

for inp in inputs:
    print(f"{inp!r} → {detect_type(inp)}")
