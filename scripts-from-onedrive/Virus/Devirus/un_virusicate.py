import glob
#~E~#
py_scripts = glob.glob("*.py") + glob.glob("*.pyw")
for script in py_scripts:
    print(script)
    code = []
    with open(script, "r") as f:
        script_code = f.readlines()

    add = True
    for line in script_code:
        if line == "#~S~#\n":
            add = False
        if add:
            code.append(line)
        if line == "#~E~#\n":
            add = True

    with open(script, "w") as f:
        f.writelines(code)
        print(code)