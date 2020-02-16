import csv

filename = 'attendance.csv' # filename of reading csv file-name
filewrite = 'attendance_percentage.csv' # writing to file
data = []

# Read CSV file
def file_read_write():
    with open(filename,'r') as readfile:
        reader = csv.reader(readfile)
        fields = reader.__next__() 
        for row in reader:
            data.append(row)
    readfile.close()

    fields = ["Email.Address","Attendance"]
    with open(filewrite, 'w') as csvfile: 
        csvwriter = csv.writer(csvfile) 
        csvwriter.writerow(fields) 

        for record in data:
            total = 0
            present = 0
            for col in record :
                if col == "Done" or col == "Not done":
                    total = total+1
                if col == "Done":
                    present = present+1
            attendance = present/total*100
            csvwriter.writerow([record[1], round(attendance,2)])


# Main function
def main() :
    file_read_write()
    print('Percentage calculated successfully!')


# Run main
main()


