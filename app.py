import time
import os
import shutil


def create_dir():
    print('\n\n Creating Folders for Sorting.\n')
    p = os.getcwd()
    path = ['Compress', 'Document', 'Audio', 'Other', 'Image', 'Video']
    for p_ in path:
        if os.path.isdir(os.path.join(p, p_)):
            pass
        else:
            os.mkdir(os.path.join(p, p_))


def filehandlers(file_header, filename, number):
    path = os.path.join(os.getcwd(), 'Information')
    if os.path.exists(path):
        q = 'a+'
    else:
        os.mkdir(path)
        q = 'w+'
    try:
        f = open(os.path.join(path, file_header), q)
        f.write(str(number) + '.\t' + str(filename) + '\n')
        f.close()
    except PermissionError:
        return
    except TextIOWrapper:
        return


def fast_scandir(dirname):
    subfolders = [f.path for f in os.scandir(dirname) if f.is_dir()]
    for dirname in list(subfolders):
        subfolders.extend(fast_scandir(dirname))
    return subfolders


def cur_direct(path, image_ext, audio_ext, video_ext, docs_ext, compress_ext):
    i = 1
    j = 1
    k = 1
    l = 1
    m = 1
    n = 1

    print(' Hold on. \n Let me clear the files before entering folders.\n')
    files = os.listdir(path)
    image_ = os.path.join(path, 'Image')
    audio_ = os.path.join(path, 'Audio')
    video_ = os.path.join(path, 'Video')
    comp_ = os.path.join(path, 'Compress')
    doc_ = os.path.join(path, 'Document')
    other_ = os.path.join(path, 'Other')

    for file in files:
        file_location = os.path.join(path, file)
        ext = (file.split(".")[-1]).lower()
        try:
            if os.path.isfile(file_location) and ext != 'ini':
                os.chmod(file_location, 755)

                if ext in image_ext:
                    filehandlers('Image.txt', file, i)
                    i = i + 1
                    shutil.move(file_location, os.path.join(image_, file))
                elif ext in audio_ext:
                    filehandlers('Audio.txt', file, j)
                    j = j + 1
                    shutil.move(file_location, os.path.join(audio_, file))
                elif ext in video_ext:
                    filehandlers('Video.txt', file, k)
                    k = k + 1
                    shutil.move(file_location, os.path.join(video_, file))
                elif ext in docs_ext:
                    filehandlers('Document.txt', file, l)
                    l = l + 1
                    shutil.move(file_location, os.path.join(doc_, file))
                elif ext in compress_ext:
                    filehandlers('Compress.txt', file, m)
                    m = m + 1
                    shutil.move(file_location, os.path.join(comp_, file))
                else:
                    filehandlers('Other.txt', file, n)
                    n = n + 1
                    shutil.move(file_location, os.path.join(other_, file))
            else:
                # print('\n Are you sure the file is there ?\n')
                pass
        except PermissionError:
            print('\n You sure you have the rights ?\n')
            pass


def main():
    print(' File Organizer 1.2 \n')
    print('+++++++++++++++++++++++++++++\n')

    image_ext = ["jpg", "png", "jpeg", "gif", "webp", "tif"]
    audio_ext = ["mp3", "wav", "m4a"]
    video_ext = ["mp4", "mkv", "avi", "webm", "mov"]
    docs_ext = ["docx", "doc", "txt", "pdf", "rtf", "xlsx", "xls"]
    compress_ext = ["rar", "zip"]

    print(' Working Director \n')
    print('+++++++++++++++++++++++++++++\n')
    Working_Directory = input(' Please Enter Your working Directory : ')
    print('\n Loading Folders\n')
    # changing Directory :
    try:
        # Change the current working Directory
        os.chdir(Working_Directory)
        print(" Directory changed : " + Working_Directory)
    except OSError:
        print("\n Can't change the Current Working Directory")
        return
    path = os.getcwd()

    lst = fast_scandir(Working_Directory)
    create_dir()

    image_ = os.path.join(path, 'Image')
    audio_ = os.path.join(path, 'Audio')
    video_ = os.path.join(path, 'Video')
    comp_ = os.path.join(path, 'Compress')
    doc_ = os.path.join(path, 'Document')
    other_ = os.path.join(path, 'Other')
    # print(image_)
    # print(audio_)
    # print(video_)
    i = 1
    j = 1
    k = 1
    l = 1
    m = 1
    n = 1
    counter = 1
    wait_ = 1

    # This function to clear up the current path before clearing the folders.
    cur_direct(path, image_ext, audio_ext, video_ext, docs_ext, compress_ext)
    print(' Please Wait', end="", flush=True)
    for dir in lst:

        files = os.listdir(dir)
        # Printing this so user dont wait not knowing what's happening
        if wait_ == 15:
            print('\n')
            wait_ = 1
        else:
            print('.', end="", flush=True)
            wait_ += 1
        if len(files) == 0:  #
            shutil.rmtree(dir)  # Delete..
        else:
            for file in files:
                file_location = os.path.join(dir, file)
                ext = (file.split(".")[-1]).lower()
                try:
                    if os.path.isfile(file_location) and ext != 'ini':
                        os.chmod(file_location, 755)

                        if ext in image_ext:
                            filehandlers('Image.txt', file, i)
                            i = i + 1
                            shutil.move(file_location, os.path.join(image_, file))
                        elif ext in audio_ext:
                            filehandlers('Audio.txt', file, j)
                            j = j + 1
                            shutil.move(file_location, os.path.join(audio_, file))
                        elif ext in video_ext:
                            filehandlers('Video.txt', file, k)
                            k = k + 1
                            shutil.move(file_location, os.path.join(video_, file))
                        elif ext in docs_ext:
                            filehandlers('Document.txt', file, l)
                            l = l + 1
                            shutil.move(file_location, os.path.join(doc_, file))
                        elif ext in compress_ext:
                            filehandlers('Compress.txt', file, m)
                            m = m + 1
                            shutil.move(file_location, os.path.join(comp_, file))
                        else:
                            filehandlers('Other.txt', file, n)
                            n = n + 1
                            shutil.move(file_location, os.path.join(other_, file))
                    else:
                        # print('\n Are you sure the file is there ?\n')
                        pass
                except PermissionError:
                    print('\n You sure you have the rights ?\n')
                    pass
            counter = counter + 1

    print('\n+++++++++++++++++++++++++++++\n')
    print(' Files Sorted : ' + str(counter) + '\n')
    print('+++++++++++++++++++++++++++++\n')
    print(' Images   : ' + str(i) + '\n')
    print(' Docs     : ' + str(l) + '\n')
    print(' Audio    : ' + str(j) + '\n')
    print(' Video    : ' + str(k) + '\n')
    print(' Compress : ' + str(m) + '\n')
    print(' Other    : ' + str(n) + '\n')
    print('-----------------------------\n')


main()
