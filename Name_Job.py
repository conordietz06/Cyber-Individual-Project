def get_names():
    num = int(input("Enter the number of names you want to input: "))
    list_names = []
    for i in range(num):
        name = input("Please enter a name: ")
        list_names.append(name)
    return list_names
def write_file(list_names):
    with open("Name.txt", "w") as input_file:
        for name in list_names:
            input_file.write(name+"\n")
        input_file.close()


def read_file():
    with open("Name.txt", "r") as read_file:
        list_jobs = []
        count_name = 1
        for line in read_file.readlines():
            print("Please enter the job for name number", count_name, end = "")
            jobs = input(": ")
            list_and_job = line.strip()+" " +jobs
            list_jobs.append(list_and_job)
            count_name+=1
        read_file.close()
        return list_jobs
def print_table(list_jobs):
    count = 1
    print("%-15s %-15s %-15s"  % ("RoleNum","Name","Job"))
    for name_job in list_jobs:
        split_name_job = name_job.split(" ")
        # print(split_name_job)
        print("%-15d %-15s %-15s" % (count, split_name_job[0], split_name_job[1]))
        count += 1
def main():
    try:
        list_names = get_names()
        write_file(list_names)
        list_jobs = read_file()
        print_table(list_jobs)
    except Exception as e:
        print(e)
    finally:
        print("My name is Conor")
main()