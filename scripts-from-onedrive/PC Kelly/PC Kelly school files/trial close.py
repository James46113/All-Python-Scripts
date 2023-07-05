from tkinter.commondialog import Dialog

class Message(Dialog):
    command  = "tk_messageBox"


def _show(title=None, message=None, _icon=None, _type=None, **options):
    if _icon and "icon" not in options:    options["icon"] = _icon
    if _type and "type" not in options:    options["type"] = _type
    if title:   options["title"] = title
    if message: options["message"] = message
    res = Message(**options).show()
    return str(res)


def close_window(icon: str, buttons: str, **options):
    if icon != "error" and icon != "info" and icon != "question" and icon != "warning":
        s = _show("Close?", "Do you want to close?", "warning", "yesno", **options)
    elif buttons != "abortretryignore" and buttons != "ok" and buttons != "okcancel" and buttons != "retrycancel" and buttons != "yesno" and buttons != "yesnocancel":
        s = _show("Close?", "Do you want to close?", icon, "yesno", **options)
    else:
        s = _show("Close?", "Do you want to close?", icon, buttons, **options)


close_window("error", "ok")
