# DONE ls. Вывести список файлов и директорий для текущей директории.
# DONE# pwd. Вывести полный путь для текущей директории.
# DONE  cd <путь>. Переход по относительному или абсолютному пути.
# DONE cp <имя файла> <имя файла>. Скопировать файл.
# DONE mv <имя файла> <имя файла>. Переместить файл.
# DONErm <имя файла>. Удалить файл.
# DONE# rmdir <имя директории>. Удалить директорию в случае, если она пуста.
# DONE# mkdir <имя директории>. Создать директорию, если ее не было.

import sys
import shlex
import os
from colorama import Fore
import shutil as sh
SHELL_RUN = 1
SHELL_STOP = 0
NOT_FORMAT = 2


def delete(name):
    try:
        if name[1]:
            os.remove(name[1])
    except OSError as error:
        print(error)
    return SHELL_RUN

def move(name):
    dir = os.getcwd()
    try:
        if name[1] and name[2]:
            os.replace(name[1], name[2])
    except OSError as error:
        print(error)
    return SHELL_RUN


def copy(name):
    dir = os.getcwd()
    try:
        if name[1] and name[2]:
            if (os.path.isfile(os.path.join(dir, name[2]))):
                sh.copyfile(name[1], name[2])
            elif (os.path.isdir(os.path.join(dir, name[2]))):
                sh.copy(name[1], name[2])
    except OSError as error:
        print(error)
    return SHELL_RUN


def def_ls():
    dir = os.getcwd()
    list = os.listdir(dir)
    for filename in list:
        if (os.path.isdir(os.path.join(dir, filename)) and filename[0] != "."):
            print(Fore.BLUE + filename, end="\t")
    for filename in list:
        if (os.path.isfile(os.path.join(dir, filename)) and filename[0] != "."):
            print(Fore.WHITE + filename, end="\t")

    print()


def def_cd(name):
    try:
        if name[1]:
            os.chdir(name[1])
    except OSError as error:
        print(error)
    return SHELL_RUN


def def_pwd():
    dir = os.getcwd()
    print(dir)
    return SHELL_RUN


def del_dir(name):
    dir = os.getcwd()
    os.chdir(dir)
    try:
        if name[1]:
            os.rmdir(name[1])
            print("Directory '%s' has been removed successfully" % name[1])
    except OSError as error:
        print(error)
        print("Directory '%s' can not be removed" % name[1])
    return SHELL_RUN


def make_folder(name):
    dir = os.getcwd()
    os.chdir(dir)
    try:
        if name[1]:
            os.mkdir(name[1])
        print("Dirrecrory '%s' successfully created" % name[1])
    except OSError as error:
        print(error)
        print("Directory '%s' can not be removed" % name[1])
    return SHELL_RUN


def execute(tokens):
    pid = os.fork()
    st = SHELL_RUN
    if pid == 0:

        if (tokens[0] == "mkdir"):
            st = make_folder(tokens)
        if (tokens[0] == "rmdir"):
            st = del_dir(tokens)
        if (tokens[0] == "pwd"):
            st = def_pwd()
        if (tokens[0] == "cd"):
            st = def_cd(tokens)
        if (tokens[0] == "ls"):
            st = def_ls()
        if (tokens[0] == "cp"):
            st = copy(tokens)
        if (tokens[0] == "mv"):
            st = move(tokens)
        if (tokens[0] == "rm"):
            st = delete(tokens)
        # os.execvp(tokens[0], tokens)
    elif pid > 0:
        while True:
            wait, status = os.waitpid(pid, 0)
            if os.WIFEXITED(status) or os.WIFSIGNALED(status):
                break
    return SHELL_RUN


def cmd_token(command):
    return shlex.split(command)


def shell():
    status = SHELL_RUN

    while status == SHELL_RUN:
        sys.stdout.write("> ")
        sys.stdout.flush()
        command = sys.stdin.readline()
        tokens = cmd_token(command)
        status = execute(tokens)


def main():
    shell()


if __name__ == "__main__":
    main()