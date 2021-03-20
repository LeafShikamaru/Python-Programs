def computerpay(hours, rate):
    if fh > 40:
        reg = fr * fh
        otp = (fh - 40.0) * (fr * 0.5)
        xp = reg + otp
    else:
        xp = fh * fr

    return pay

sh = input("Enter Hours: ")
sr = input("Enter Rate: ")

fh = float(sh)
fr = float(sr)

xp = computepay(fh, fr)

print("Pay:",xp)
