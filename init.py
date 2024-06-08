from datetime import datetime # Used for dates
import pytz # Used for timezone
import calendar # Used to get proper date strings (month, day, etc)
import sys # Used for commandline arguments

def handle_command_args(args:list[str]) -> tuple[int, bool]:
    '''
    Handles any commandline arguments.

    ### Parameters:
    - args (list[list]):
        The list of commandline arguments (given from sys.argv)
    
    ### Returns:
        A tuple[int, bool] with the month to base on,
        and whether to print next month's roamers.
    '''
    possible_lengths = [1, 3, 5]
    args_len = len(args)

    next_month_str = "--next-month"
    month_str = "-m"
    
    if args_len not in possible_lengths:
        print(''.join([f"ERROR: Wrong amount of commandline arguments.\n",
                       f"Usage:\n",
                       f"\n",
                       f"$ py pri.py [OPT] [VAL]\n",
                       f"\n",
                       f"[OPT]            [VAL]       Explanation\n",
                       f"{month_str}               1-12        The month to get the roamers from\n",
                       f"{next_month_str}     true/false  Whether to print the next month's roamers\n"]))

        sys.exit(1)
    
    # Args to return, init to None
    month_arg:int = None
    next_month_arg:bool = None

    # Ensure given argument values are valid
    if month_str in args:
        month_idx = args.index(month_str, 1)+1
        month_val = int(args[month_idx])

        month_arg = int(month_val) if month_val in range(1, 12) else 1 if month_val < 1 else 12

    if next_month_str in args:
        next_month_idx = args.index(next_month_str, 1)+1

        next_month_arg = True if args[next_month_idx].lower() == "true" else False
    

    return month_arg, next_month_arg


# Handle any given commandline arguments
command_args = sys.argv
current_month, use_next_month = handle_command_args(command_args)


# Save month names list in variable for easier reference
month_names = calendar.month_name

# PokeMMO is based on UTC
timezone = pytz.UTC

# Get the current time and month
current_time = datetime.now(timezone)

if current_month == None: # Default to current real life month and use next month
    current_month = current_time.month
    use_next_month = True

next_month = current_month+1 if current_month < 12 else 1
current_month_name = month_names[current_month]
next_month_name = month_names[next_month]
