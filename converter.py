import os
import sys
import shutil
import commands
from PIL import Image


def print_commands():
    """
    Print all commands to console
    """
    for command_option in commands.main_commands:
        print(command_option)


def get_work_dir():
    """
    Get working directory
    """
    return os.getcwd()


def create_outputdir():
    """
    Creates and returns path to output directory or None if directory exists and is not removed.
    """
    workdir = get_work_dir()
    outdir = os.path.join(workdir, r"00_img_out")
    if os.path.exists(outdir):
        print("'00_img_out' directory already exists! Do you wanna remove it and all of it's content? Y/n")
        remove = input()
        if remove == "Y" or remove == "y":
            shutil.rmtree(outdir)
            os.makedirs(outdir)
            return outdir
        else:
            print("Could not convert folder '00_img_out' already exists. Please remove or move folder and try again.")
            return None
    else:
        os.makedirs(outdir)
        return outdir


def get_image_file_paths(workdir):
    """
    find jpeg, jpg, and png images inside workdir.
    Returns list of file paths.
    """
    files = []
    for candidate in os.listdir(workdir):
        if candidate.lower().endswith(".png") or candidate.lower().endswith(".jpg") or candidate.lower().endswith(".jpeg"):
            files.append(candidate)
    return files


def convert_list_to_webp(files, outputdir):
    """
    Convert individual files to webp.
    Returns dictionary of lists about success and errored images 
    """
    converted_images = []
    error_images = []

    print("Input quality percentage. [0-100] where 0 is bad 100 good.")
    try:
        compression = int(input())
    except ValueError:
        print("--------------\n\nQuality percentage must be integer value. Zero pictures converted, try again!\n\n--------------")
        return None
    
    print("Starting conversion. Please wait!")
    for file in files:
        try:
            with Image.open(file) as im:
                print("*")
                output_file = os.path.splitext(file)[0] + ".webp"
                im.save(os.path.join(outputdir, output_file), 'webp', optimize=True, quality=compression)
                converted_images.append(file)
        except OSError:
            print("cannot convert", file)
            error_images.append(file)
    return {"success": converted_images, "error": error_images}


def convert_images():
    """
    Top level function to convert images
    """
    outputdir = create_outputdir()
    if outputdir is not None:
        workdir = get_work_dir()
        image_paths = get_image_file_paths(workdir)
        if len(image_paths) == 0:
            print(f"--------------\n\nNo image files detected! \n1.Make sure images are in .png, .jpg, or .png format. \n2.Files must be placed inside work dir: {get_work_dir()}\n\n--------------")
        else:
            convert_status = convert_list_to_webp(image_paths, outputdir)
            if convert_status is not None:
                print("--------------\n\nSuccesfully converted: ")
                for okstatus in convert_status["success"]:
                    print(f"{okstatus}")
                print("--------------\n\nFailed to convert: ")
                for error in convert_status["error"]:
                    print(f"{error}\n")
                print(f"\n\n--------------")
    else:
        pass


def count_images_in_converted_folder():
    """
    Return image count in converted folder.
    """
    outdir = os.path.join(get_work_dir(), r"00_img_out")
    count = 0
    if os.path.exists(outdir):
        for candidate in os.listdir(outdir):
            if candidate.endswith(".webp"):
                count = count + 1
    return count
    


def evaluate_command(command):
    """
    Evaluates given command and calls action
    """
    match command:
        case "help":
            print_commands()
        case "convert":
            convert_images()
        case "list":
            print("--------------\n\nFiles in working directory:\n")
            for file in get_image_file_paths(get_work_dir()):
                print(file)
            print("\n--------------\n\n")
        case "count": 
            print(f"--------------\n\nTotal image files in working directory: {len(get_image_file_paths(get_work_dir()))}\n\n--------------\n\n")
        case "countout":
            count = count_images_in_converted_folder()
            if count != 0:
                print(f"--------------\n\nTotal image files in converted directory: {count}\n\n--------------\n\n")
            else:
                print("--------------\n\nConverted directory is empty.\n\n--------------")
        case "license":
            print(commands.license_mit)
        case "exit":
            print("--------------\n\nGoodbye!\n\n--------------")
            sys.exit(1)
        case _:
            print("--------------\n\nInvalid command, check spelling!\n\n--------------")


def run_commandline_ui_loop():
    """
    Function runs main command-line ui loop.
    """
    while True:
        command = input()
        evaluate_command(command)

        
if __name__ == "__main__":
    # Print splash screen
    print(commands.splash_screen)
    print_commands()
    run_commandline_ui_loop()