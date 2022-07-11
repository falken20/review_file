from rich.console import Console
from rich.progress import Progress

# Create global object to manage terminal logs
console = Console()

FILE_NAME_SOURCE = "/Users/u102105/Downloads/COREJB_ACTIVIDAD_08072022.csv"
FILE_NAME_SOURCE = "/Users/u102105/Downloads/COREJB_ACTIVIDAD_22062022.txt" # 14 GB
FILE_NAME_RESULT = "/Users/u102105/Downloads/final.txt"
TEXT_TO_SEARCH = "1073741888"

def main():

    console.print("Process to review lines in a file")

    # FILE_NAME_SOURCE = input("File name to review: ")
    # FILE_NAME_RESULT = input("File name to write: ")

    fhandler_source = open(FILE_NAME_SOURCE, "r")
    fhandler_result = open(FILE_NAME_RESULT, "w")

    console.print("Counting lines...")
    lines = fhandler_source.readlines()
    count_total_lines = len(lines)
    console.print(f"Lines to process: {count_total_lines}")
    
    count_written_lines = 0

    with Progress() as progress:
        task = progress.add_task(f"Searching for text: [red][bold]'{TEXT_TO_SEARCH}'[/red][/bold]...", total=count_total_lines)
    
        for line in lines:
            progress.update(task, advance=1)
            if TEXT_TO_SEARCH in line:
                fhandler_result.write(line)
                count_written_lines += 1

    fhandler_source.close()
    fhandler_result.close()

    console.print("Process finished sucessfully")
    console.print(f"Lines processed: {count_total_lines}")
    console.print(f"Lines written: {count_written_lines}")
  

if __name__ == "__main__":
    console.print("\n***** review_file started *****\n", style="bold green")
    main()
    console.print("\n[bold green]***** review_file finished :smile: *****[/bold green]\n")
