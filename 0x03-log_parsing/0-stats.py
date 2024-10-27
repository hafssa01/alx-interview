#!/usr/bin/python3
import sys
import signal
import re

"""Initialize global variables for tracking file size and status code counts"""
total_file_size = 0
status_code_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}

def print_metrics():
    """
    Prints the total file size and counts of each HTTP status code.
    Metrics are printed in ascending order of status code.
    """
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")

def process_line(line):
    """
    Processes a single line of log data. Extracts status code and file size if the line format is valid.
    
    Parameters:
        line (str): A single line of log data.
        
    Returns:
        None
    """
    global total_file_size, status_code_counts

    # Regular expression pattern for the expected log format
    pattern = r'^\S+ - \[\S+ \S+\] "GET \/projects\/260 HTTP\/1\.1" (\d{3}) (\d+)$'
    match = re.match(pattern, line)
    
    if match:
        # Extract status code and file size from the matched line
        status_code = match.group(1)
        file_size = int(match.group(2))
        
        # Update the total file size
        total_file_size += file_size
        
        # Increment the count for the status code if it exists in the dictionary
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1

def main():
    """
    Main function that reads lines from standard input, processes each line, 
    and periodically prints metrics.
    """
    line_count = 0

    # Define a signal handler to catch keyboard interrupts (CTRL + C)
    def signal_handler(sig, frame):
        """
        Signal handler to print metrics before exiting when interrupted.
        
        Parameters:
            sig (int): Signal number.
            frame: Current stack frame.
        
        Returns:
            None
        """
        print_metrics()
        sys.exit(0)

    # Set up signal handling for graceful termination
    signal.signal(signal.SIGINT, signal_handler)

    try:
        # Read each line from standard input
        for line in sys.stdin:
            process_line(line.strip())
            line_count += 1

            # Print metrics every 10 lines
            if line_count % 10 == 0:
                print_metrics()

        # Final print of metrics after all lines are processed
        print_metrics()
    
    except Exception as e:
        """
        Catch any unexpected exceptions that might occur during processing.
        """
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
