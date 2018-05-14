disk_num = int(input("How many disks on the table? "))


def movetower(height, frompole, topole , withpole):
    if height >= 1:
        movetower(height - 1, frompole, withpole, topole)
        movedisk(frompole, topole)
        movetower(height - 1, withpole, topole, frompole)

def movedisk(frompole, topole):
    print("moving disk from ", frompole, " to ", topole)

movetower(disk_num, "A", "B", "C")