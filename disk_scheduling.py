def fcfs(requests, initial_position):
    total_head_movements = 0
    current_position = initial_position
    for request in requests:
        total_head_movements += abs(request - current_position)
        current_position = request
    return total_head_movements


def scan(requests, initial_position, total_cylinders):
    total_head_movements = 0
    current_position = initial_position
    requests.sort()
    index = requests.index(initial_position)

    for direction in ['left', 'right']:
        if direction == 'left':
            for i in range(index, -1, -1):
                total_head_movements += abs(requests[i] - current_position)
                current_position = requests[i]
        else:
            for i in range(index + 1, len(requests)):
                total_head_movements += abs(requests[i] - current_position)
                current_position = requests[i]
    return total_head_movements


def c_scan(requests, initial_position, total_cylinders):
    total_head_movements = 0
    current_position = initial_position
    requests.sort()
    index = requests.index(initial_position)

    for direction in ['right', 'left']:
        if direction == 'right':
            for i in range(index, len(requests)):
                total_head_movements += abs(requests[i] - current_position)
                current_position = requests[i]
        else:
            for i in range(0, index):
                total_head_movements += abs(requests[i] - current_position)
                current_position = requests[i]
    return total_head_movements


def read_requests(file_name):
    with open(file_name, 'r') as file:
        requests = [int(line.strip()) for line in file]
    return requests


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python disk_scheduling.py initial_position requests_file.txt")
        sys.exit(1)

    initial_position = int(sys.argv[1])
    requests_file = sys.argv[2]
    requests = read_requests(requests_file)
    total_cylinders = 5000

    fcfs_movements = fcfs(requests, initial_position)
    scan_movements = scan(requests, initial_position, total_cylinders)
    c_scan_movements = c_scan(requests, initial_position, total_cylinders)

    print("FCFS total head movements:", fcfs_movements)
    print("SCAN total head movements:", scan_movements)
    print("C-SCAN total head movements:", c_scan_movements)


def fcfs(requests, initial_position):
    total_head_movements = 0
    current_position = initial_position
    for request in requests:
        total_head_movements += abs(request - current_position)
        current_position = request
    return total_head_movements


def scan(requests, initial_position, total_cylinders):
    total_head_movements = 0
    current_position = initial_position
    requests.sort()
    index = requests.index(initial_position)

    for direction in ['left', 'right']:
        if direction == 'left':
            for i in range(index, -1, -1):
                total_head_movements += abs(requests[i] - current_position)
                current_position = requests[i]
        else:
            for i in range(index + 1, len(requests)):
                total_head_movements += abs(requests[i] - current_position)
                current_position = requests[i]
    return total_head_movements


def c_scan(requests, initial_position, total_cylinders):
    total_head_movements = 0
    current_position = initial_position
    requests.sort()
    index = requests.index(initial_position)

    for direction in ['right', 'left']:
        if direction == 'right':
            for i in range(index, len(requests)):
                total_head_movements += abs(requests[i] - current_position)
                current_position = requests[i]
        else:
            for i in range(0, index):
                total_head_movements += abs(requests[i] - current_position)
                current_position = requests[i]
    return total_head_movements


def read_requests(file_name):
    with open(file_name, 'r') as file:
        requests = [int(line.strip()) for line in file]
    return requests


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python disk_scheduling.py initial_position requests_file.txt")
        sys.exit(1)

    initial_position = int(sys.argv[1])
    requests_file = sys.argv[2]
    requests = read_requests(requests_file)
    total_cylinders = 5000

    fcfs_movements = fcfs(requests, initial_position)

    # Sort requests for SCAN and C-SCAN algorithms
    sorted_requests_scan = sorted(requests)
    sorted_requests_c_scan = sorted(requests)

    scan_movements = scan(sorted_requests_scan, initial_position, total_cylinders)
    c_scan_movements = c_scan(sorted_requests_c_scan, initial_position, total_cylinders)

    print("FCFS total head movements:", fcfs_movements)
    print("SCAN total head movements:", scan_movements)
    print("C-SCAN total head movements:", c_scan_movements)
