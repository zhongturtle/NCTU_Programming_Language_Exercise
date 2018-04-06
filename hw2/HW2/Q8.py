department = "Biological Science and Technology"

sci_pos = department.find("Sci")
sci_count = department.count("Sci")

tech_pos = department.find("Tech")
tech_count = department.count("Tech")

olo_pos = department.find("olo")
olo_count = department.count("olo")

bio_pos = department.find("bio")
bio_count = department.count("bio")

lol_pos = department.find("lol")
lol_count = department.count("lol")

print( "The string \"Sci \" first occurs at position " + str(sci_pos ) + ", and it occurs " + str(sci_count) + " time(s)")
print( "The string \"Tech\" first occurs at position " + str(tech_pos ) + ", and it occurs " + str(tech_count) + " time(s)")
print( "The string \"olo \" first occurs at position " + str(olo_pos ) + ", and it occurs " + str(olo_count) + " time(s)")
print( "The string \"bio \" first occurs at position " + str(bio_pos ) + ", and it occurs " + str(bio_count) + " time(s)")
print( "The string \"lol \" first occurs at position " + str(lol_pos ) + ", and it occurs " + str(lol_count) + " time(s)")