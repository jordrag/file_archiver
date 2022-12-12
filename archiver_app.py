from archiver_package.archiver_input import *
from archiver_package.archiver_manager import *
from archiver_package.archiver_output import *


# *************************************************************************

def run_archiver():
    input_data = UserInput.entry_choice()
    compression = input_data[0]
    action = input_data[1]
    source = input_data[2]

    manager = ArchiveManager(compression, action, source)
    result = manager.manage_compression()

    file = FileOperator(result, compression, action)
    file.commands()

# **************************************************************************

run_archiver()