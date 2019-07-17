log_file = open("um-server-01.txt")
#opening the file

def sales_reports(log_file):
    for line in log_file:
    # iterate over the opened file

        line = line.rstrip()
        # strip off the white space after it

        day = line[0:3]
        # grab the day value by doing list slicing

        if day == "Mon":
            print(line)

        # print the data when day is Monday

sales_reports(log_file)
