import os
import time
import random
import threading
import mysql.connector
import psutil

def cpu_stress_test(duration=60):
    """
    Perform CPU Stress Test by utilizing CPU with infinite loops.
    """
    def cpu_load():
        while True:
            pass

    threads = []
    for _ in range(os.cpu_count()):
        t = threading.Thread(target=cpu_load)
        t.start()
        threads.append(t)

    time.sleep(duration)

    for thread in threads:
        thread.do_run = False
    print("CPU Stress Test completed.")


def memory_stress_test(duration=60):
    """
    Perform Memory Stress Test by allocating large blocks of memory.
    """
    memory_blocks = []
    try:
        for _ in range(duration):
            block = bytearray(100 * 1024 * 1024)  # Allocate 100MB
            memory_blocks.append(block)
            time.sleep(1)
    except MemoryError:
        print("Memory Stress Test completed with MemoryError.")
    finally:
        memory_blocks.clear()
        print("Memory Stress Test completed.")


def disk_stress_test(duration=60):
    """
    Perform Disk Stress Test by writing and deleting files continuously.
    """
    temp_dir = "./disk_stress_test"
    os.makedirs(temp_dir, exist_ok=True)

    end_time = time.time() + duration
    try:
        while time.time() < end_time:
            with open(os.path.join(temp_dir, f"temp_{random.randint(0, 10000)}.tmp"), 'w') as temp_file:
                temp_file.write(os.urandom(1024 * 1024))  # Write 1MB of random data
            time.sleep(0.1)
    finally:
        for temp_file in os.listdir(temp_dir):
            os.remove(os.path.join(temp_dir, temp_file))
        os.rmdir(temp_dir)
        print("Disk Stress Test completed.")


def sql_stress_test(host='localhost', user='ahmad', password='Iloveuae1', database='mysql', duration=60):
    """
    Perform SQL Stress Test by executing frequent SELECT queries.
    """
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    cursor = connection.cursor()
    end_time = time.time() + duration

    try:
        while time.time() < end_time:
            cursor.execute("SELECT * FROM your_table LIMIT 1000;")  # Replace 'your_table' with the actual table name
            connection.commit()
            time.sleep(0.1)  # Adjust the sleep time to control the QPS (queries per second)
    finally:
        cursor.close()
        connection.close()
                print("sql stress test completed")                                                                                                                                                81,1          61%



def main():
    print("Select a stress test to perform:")
    print("1 - Perform CPU Stress Test")
    print("2 - Perform Memory Stress Test")
    print("3 - Perform Disk Stress Test")
    print("4 - Perform SQL Stress Test")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        cpu_stress_test()
    elif choice == '2':
        memory_stress_test()
    elif choice == '3':
        disk_stress_test()
    elif choice == '4':
        sql_stress_test()
    else:
        print("Invalid choice. Exiting...")

if __name__ == "__main__":
    main()


