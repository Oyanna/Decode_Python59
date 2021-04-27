users = {
    "Anna": {
        "phone": "+989776",
        "email": "ann@gmail.com"
    },
    "Bob": {
        "telephone": "+989776",
        "email": "dshjus@gmail.com",
        "skype": "bob123",
        1: 1213

    }
}

ann_phone = users["Anna"]["phone"]
print(ann_phone)
key = "skype"
if key in users["Anna"]:
    print(users["Anna"]["skype"])
else:
    print("no skype")