def speeding_ticket(speed, speedLimit):
    diff = speed - speedLimit
    if diff >= 20:
        return (500, True)
    elif diff >= 5:
        return (100, False)
    else:
        return (0, False)


print(speeding_ticket(50, 50)) #No fine. Prints: (0, False)
print(speeding_ticket(60, 50)) #100€ fine, doesn't lose license. Prints: (100, False)
print(speeding_ticket(100, 50)) #500€ fine, loses license. Prints: (500, True)