###--- IMPORTS ---###
import shutil
import settings


###--- GLOBAL VARIABLES ---###
source = settings.SOURCE_PATH
destination = settings.DESTINATION_PATH


###--- FUNCTIONS ---###
def shutil_move():
    '''
    Using `shutil`
    '''
    global source, destination

    # move source to destination
    shutil.move(source, destination)


###--- DRIVER CODE ---###
if __name__ == "__main__":
    shutil_move()
