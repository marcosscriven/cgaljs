import os
import tarfile
import urllib2

def download(url, path):
    filename = url.split('/')[-1]
    file_path = os.path.join(path, filename)
    print 'Downloading:%s to:%s' % tuple([url, file_path])

    if os.path.isfile(file_path):
        print 'Already downloaded'
        return file_path

    if not os.path.exists(path):
        os.makedirs(path)

    u = urllib2.urlopen(url)
    localFile = open(file_path, 'w')
    localFile.write(u.read())
    localFile.close()
    print 'Download completed'
    return file_path

def untar(tar_file, dest_path):
    # Check it actually needs to be unarchived
    if not is_archive_file(tar_file):
        return

    if os.path.exists(dest_path):
        print "Already unarchived. Clean if you want to get a fresh copy"
        return

    print "Unarchiving"
    tar_file = tarfile.open(tar_file)
    tar_file.extractall(dest_path)
    print "Finished unarchiving"

def is_archive_file(archive_path):
    return archive_path.split('.')[-1] == 'bz2'




