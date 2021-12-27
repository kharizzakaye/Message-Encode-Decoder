from tkinter import *
import base64

root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title('Message Encoder and Decoder')

# saves the message to be encoded/decoded
Text = StringVar()
# stores the private key
private_key = StringVar()
# saves mode
mode = StringVar()
# saves result
Result = StringVar()

Label(root, text = 'Encode Decode', font='arial 20 bold').pack(side = TOP)
Label(root, text = 'Secure your message', font='arial 20 bold').pack(side = BOTTOM)


# Message Encoder
def Encode(key, message):
    # empty list to store encoded message
    enc = []

    # run a loop to encode every character in the message
    for i in range(len(message)):
        # a list to store the value of the key
        key_c = key[i%len(key)]

        # add message and key to empty list enc to encode it
        # ord = convert to integer, chr = convert to string
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode(''.join(enc).encode())


# Message Decoder
def Decode(key, message):
    dec = []
    message = base64.urlsafe_b64decode(message).decode()

    for i in range(len(message)):
        key_c = key[i%len(key)]
        dec.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))
    return ''.join(dec)


# mode function
def Mode():
    if (mode.get() == 'e'):
        Result.set(Encode(private_key.get(), Text.get()))
    elif (mode.get() == 'd'):
        Result.set(Decode(private_key.get(), Text.get()))
    else:
        Result.set('Invalid Mode')


def Exit():
    root.destroy()


def reset():
    Text.set('')
    private_key.set('')
    mode.set('')
    Result.set('')


Label(root, font='arial 12 bold', text='MESSAGE').place(x=60, y=60)
Entry(root, font='arial 10', textvariable=Text, bg='ghost white').place(x=290, y=60)

Label(root, font='arial 12 bold', text='KEY').place(x=60, y=90)
Entry(root, font='arial 10', textvariable=private_key, bg='ghost white').place(x=290, y=90)

Label(root, font='arial 12 bold', text='MODE').place(x=60, y=120)
Entry(root, font='arial 10', textvariable=mode, bg='ghost white').place(x=290, y=120)

Entry(root, font='arial 10', textvariable=Result, bg='ghost white').place(x=290, y=150)
Button(root, font='arial 10 bold', text='RESULT', bg='LightGray', command=Mode).place(x=60, y=150)

Button(root, font='arial 10 bold', text='RESET', bg='LimeGreen', command=reset).place(x=60, y=180)

Button(root, font='arial 10 bold', text='EXIT', bg='OrangeRed', command=Exit).place(x=60, y=220)

# to display
root.mainloop()