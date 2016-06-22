# coding=utf-8

import os


def check_folder(folder):
    """ checa se a pasta existe caso contrario cria """
    if os.path.exists(folder) and os.path.isdir(folder):
        return folder
    else:
        os.makedir(folder)
        return folder
