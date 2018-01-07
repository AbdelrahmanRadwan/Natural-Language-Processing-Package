def remove_endlines(lines):
    for i in range(len(lines)):
        lines[i]= lines[i].rstrip()
    return lines