import os
import time
import tracemalloc
from rich.console import Console
from rich.progress import Progress

# Create global object to manage terminal logs
console = Console()

# FILE_NAME_SOURCE = "/Users/u102105/Downloads/COREJB_ACTIVIDAD_08072022.csv"
FILE_NAME_SOURCE = "/Users/u102105/Downloads/COREJB_ACTIVIDAD_22062022.txt" # 14 GB
FILE_NAME_RESULT = "/Users/u102105/Downloads/final.txt"
TEXT_TO_SEARCH = "1073741888"
SIZE_LINE = 400  # Line size in characters


def process_by_line(fhandler_source, fhandler_result):
    """Process loading only every line
    """
    console.print("Counting lines...")
    count_total_lines = os.path.getsize(FILE_NAME_SOURCE) / SIZE_LINE
    console.print(f"Lines (aprox) to process: {count_total_lines:,.0f}")

    count_written_lines = 0

    with Progress() as progress:
        task = progress.add_task(
            f"Searching for text: [red][bold]'{TEXT_TO_SEARCH}'[/red][/bold]...", total=count_total_lines)

        for line in fhandler_source:
            progress.update(task, advance=1)
            if TEXT_TO_SEARCH in line:
                fhandler_result.write(line)
                count_written_lines += 1

    console.print("\nProcess 'Using by line' finished sucessfully", style="bold green")
    console.print(f"Lines processed: {count_total_lines:,.0f} lines", style="yellow")
    console.print(f"Lines written: {count_written_lines:,} lines", style="yellow")


def process_by_list(fhandler_source, fhandler_result):
    """Process loading all the lines in memory
    """
    console.print("Counting lines...")
    lines = fhandler_source.readlines()
    count_total_lines = len(lines)
    console.print(f"Lines to process: {count_total_lines:,}")

    count_written_lines = 0

    with Progress() as progress:
        task = progress.add_task(
            f"Searching for text: [red][bold]'{TEXT_TO_SEARCH}'[/red][/bold]...", total=count_total_lines)

        for line in lines:
            progress.update(task, advance=1)
            if TEXT_TO_SEARCH in line:
                fhandler_result.write(line)
                count_written_lines += 1

    console.print("\nProcess 'Using a List' finished sucessfully", style="bold green")
    console.print(f"Lines processed: {count_total_lines:,} lines", style="yellow")
    console.print(f"Lines written: {count_written_lines:,} lines", style="yellow")


def main():
    # Start to measure memory use
    tracemalloc.start()
    console.print("\n***** review_file started *****\n", style="bold green")

    time_init = time.time()

    file_size = os.path.getsize(FILE_NAME_SOURCE) / 1024 / 1024 / 1024
    console.print(f"File size: {file_size:,.2f} Gb")

    fhandler_source = open(FILE_NAME_SOURCE, "r")
    fhandler_result = open(FILE_NAME_RESULT, "w")

    process_by_line(fhandler_source, fhandler_result)
    # process_by_list(fhandler_source, fhandler_result)  # Use a lot of memory

    fhandler_source.close()
    fhandler_result.close()

    console.print(
        f"Process time: {time.time() - time_init:,.2f} sg", style="yellow")
    file_size = os.path.getsize(FILE_NAME_RESULT) / 1024 / 1024 / 1024
    console.print(f"File result size: {file_size:,.2f} Gb", style="yellow")

    # displaying the memory used
    current, peak = tracemalloc.get_traced_memory()
    console.print(f"Memory current size: {current:,}", style="yellow")
    console.print(f"Memory peak size: {peak:,}", style="yellow")

    # Stop memory use measure
    tracemalloc.stop()
    console.print(
        "\n[bold green]***** review_file finished :smile: *****[/bold green]\n")


if __name__ == "__main__":
    main()
