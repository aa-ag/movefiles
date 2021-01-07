###--- IMPORTS ---###
import shutil
import os
import settings


###--- GLOBAL VARIABLES ---###
source = settings.SOURCE_PATH
destination = settings.DESTINATION_PATH


###--- FUNCTIONS ---###
# def shutil_move():
#     '''
#      Using `shutil`
#     '''
#     global source, destination

#     # move source file to destination directory
#     # shutil.move(source, destination)

#     all_files_in_given_directory = os.listdir(source)

#     for individual_file in all_files_in_given_directory:
#         shutil.move(os.path.join(source, individual_file), destination)


def rename_and_move():
    '''
     Using `rename`
    '''
    global source, destination

    for count, filename in enumerate(os.listdir(source)):
        dst = "file_" + str(count) + ".txt"

        # rename all the files
        os.rename(os.path.join(source, filename),
                  os.path.join(destination, dst))


###--- DRIVER CODE ---###
if __name__ == "__main__":
    # shutil_move()
    rename_and_move()
