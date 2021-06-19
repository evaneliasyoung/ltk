#!/usr/bin/env python3
"""
Author   : Evan Elias Young
Date     : 2020-01-06
Revision : 2020-05-19
"""

from typing import List, Tuple

COPYRIGHT: str = 'Copyright (c) Evan Elias Young 2020'
VER: str = '0.1.1'


def print_header() -> None:
    """Prints the headers.
    """
    print(r'  ____ ____   ___  _   _  ____ _____ _   _ ')
    print(r' / ___|  _ \ / _ \| \ | |/ ___| ____| \ | |')
    print(r'| |   | |_) | | | |  \| | |  _|  _| |  \| |')
    print(r'| |___|  _ <| |_| | |\  | |_| | |___| |\  |')
    print(r' \____|_| \_\\___/|_| \_|\____|_____|_| \_|')
    print()
    print(f'Version {VER}')
    print(COPYRIGHT)
    print()


def get_opt(opts: List[Tuple[str, str]]) -> str:
    """Gets an option, or exit.

    Arguments:
        opts {List[Tuple[str, str]]} -- The list of options.

    Returns:
        str -- The chosen option.
    """
    print('Choose from below, or [e]xit to quit.')
    for i in range(len(opts)):
        print(f'[{i + 1}] {opts[i][0]}')
    while True:
        sel = input()
        if sel == 'exit' or sel == 'e':
            exit()
        try:
            return opts[int(sel) - 1][1]
        except:
            pass


def get_minutes() -> str:
    """Gets the minutes pattern.

    Returns:
        str -- The minutes pattern.
    """
    opts: List[Tuple[str, str]] = [('Every Minute', '*'),
                                   ('Even Minutes', '*/2'),
                                   ('Odd Minutes', '1-59/2'),
                                   ('Every 5 Minutes', '*/5'),
                                   ('Every 15 Minutes', '*/15'),
                                   ('Every 30 Minutes', '*/30'),
                                   ('Custom Minutes', '?')]
    opt: str

    print('RUN MINUTES')
    opt = get_opt(opts)

    if opt == '?':
        opt = input()

    return opt


def get_hours() -> str:
    """Gets the hours pattern.

    Returns:
        str -- The hours pattern.
    """
    opts: List[Tuple[str, str]] = [('Every Hour', '*'), ('Even Hours', '*/2'),
                                   ('Odd Hours', '1-23/2'),
                                   ('Every 6 Hours', '*/6'),
                                   ('Every 12 Hours', '*/12'),
                                   ('Custom Hours', '?')]
    opt: str

    print('RUN HOURS')
    opt = get_opt(opts)

    if opt == '?':
        opt = input()

    return opt


def get_days() -> str:
    """Gets the days pattern.

    Returns:
        str -- The days pattern.
    """
    opts: List[Tuple[str, str]] = [('Every Day', '*'), ('Even Days', '*/2'),
                                   ('Odd Days', '1-31/2'),
                                   ('Every 5 Days', '*/5'),
                                   ('Every 10 Days', '*/10'),
                                   ('Every Half Month', '*/15'),
                                   ('Custom Days', '?')]
    opt: str

    print('RUN DAYS')
    opt = get_opt(opts)

    if opt == '?':
        opt = input()

    return opt


def get_months() -> str:
    """Gets the months pattern.

    Returns:
        str -- The months pattern.
    """
    opts: List[Tuple[str, str]] = [('Every Month', '*'),
                                   ('Even Months', '*/2'),
                                   ('Odd Months', '1-12/2'),
                                   ('Every 3 Months', '*/3'),
                                   ('Every 4 Months', '*/4'),
                                   ('Every 6 Months', '*/6'),
                                   ('Custom Months', '?')]
    opt: str

    print('RUN MONTHS')
    opt = get_opt(opts)

    if opt == '?':
        opt = input()

    return opt


def get_weekdays() -> str:
    """Gets the weekdays pattern.

    Returns:
        str -- The weekdays pattern.
    """
    opts: List[Tuple[str, str]] = [('Everyday', '*'), ('Weekdays', '1-5'),
                                   ('Weekends', '0,6'),
                                   ('Custom Weekdays', '?')]
    opt: str

    print('RUN WEEKDAYS')
    opt = get_opt(opts)

    if opt == '?':
        opt = input()

    return opt


def get_command() -> str:
    """Gets the command to run.

    Returns:
        str -- The command to run.
    """
    print('RUN COMMAND')
    return input()


def get_output() -> str:
    """Gets the output pattern.

    Returns:
        str -- The output pattern.
    """
    opts: List[Tuple[str, str]] = [('Mute', 'm'), ('File', 'f')]
    opt: str

    print('RUN OUTPUT')
    opt = get_opt(opts)

    return input() if opt == 'f' else '/dev/null 2>&1'


def get_cron_tag() -> str:
    """Gets the full cron tag.

    Returns:
        str -- The full cron tag.
    """
    run_minutes: str = get_minutes()
    print()
    run_hours: str = get_hours()
    print()
    run_days: str = get_days()
    print()
    run_months: str = get_months()
    print()
    run_weekdays: str = get_weekdays()
    print()
    command: str = get_command()
    print()
    output: str = get_output()
    print()

    return f'{run_minutes} {run_hours} {run_days} {run_months} {run_weekdays} {command} > {output}'


if __name__ == '__main__':
    print_header()
    print(get_cron_tag())
