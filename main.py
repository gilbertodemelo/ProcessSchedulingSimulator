from scheduler import Scheduler


def main():

    process_scheduler = Scheduler("data/process_list.csv")

    print(f"Number of processes in line: {process_scheduler.size} ")




if __name__ == '__main__':
    main()


