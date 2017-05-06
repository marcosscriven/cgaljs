import os
import shutil
from subprocess import call
from utils import download, untar

DOWNLOAD_DIR = "downloads"
SOURCE_DIR = "source"
BUILD_DIR = "build"


def build_component(name, includes_dir, libs_dir, working_dir=None):

    # Step 0 - Prepare
    print "Building component:%s" % name
    component =  __import__("components.%s.config" % name, fromlist="components")
    working_dir = prepare_directory(name, working_dir)
    source_dir = os.path.join(get_source_dir(working_dir), component.SOURCE_DIR)
    component_dir = os.path.join("components", name)

    # Step 1 - Download
    download_tarballs(component.DOWNLOADS, working_dir)

    # Step 2 - Patch source
    try:
        patch_files(component.SOURCE_PATCHES, source_dir, name)
    except:
        pass

    # Step 3 - Configure
    try:
        command = component.CONFIGURE_CMD.format(includes=os.path.abspath(includes_dir), libs=os.path.abspath(libs_dir),
                                                 component_dir=os.path.abspath(component_dir))
        call(command, cwd=source_dir, shell=True)
    except:
        pass

    # Step 4 - Patch any generated config or headers (IE Anything that's not in the original tarball)
    try:
        patch_files(component.CONFIG_PATCHES, source_dir, name)
    except:
        pass

    # Step 5 - Build
    try:
        call(component.MAKE_CMD, cwd=source_dir, shell=True)
    except:
        pass

    # Step 6 - Copy artifacts to given destination
    copy_artifacts(component.ARTIFACTS, working_dir, includes_dir, libs_dir)

    print "Completed building component:%s" % name
    print "********************************************************************************************************"


def get_default_working_dir(name):
    return os.path.join(os.getcwd(), BUILD_DIR, name)


def get_source_dir(path):
    return os.path.join(path, SOURCE_DIR)


def get_download_dir(path):
    return os.path.join(path, DOWNLOAD_DIR)


def get_component(name):
    try:
        return __import__("components.%s.config" % name, fromlist="components")
    except:
        print "No such component:%s" % name
        return


def prepare_directory(name, working_dir=None):
    if not working_dir:
        working_dir = get_default_working_dir(name)

    # Cleanup old source
    try:
        shutil.rmtree(get_source_dir(working_dir))
    except:
        pass

    return working_dir


def download_tarballs(downloads, working_dir):
    for download_url in downloads:
        download_file_path = download(download_url, get_download_dir(working_dir))
        untar(download_file_path, get_source_dir(working_dir))


def copy_artifacts(artifacts, working_dir, includes_dir, libs_dir):
    try:
        for include in artifacts['includes']:
            source = os.path.join(get_source_dir(working_dir), include['source'])
            destination = os.path.join(includes_dir, include['name'])
            print "Copying include directory from:%s to:%s" % tuple([source, destination])

            try:
                shutil.rmtree(destination)
            except:
                pass
            shutil.copytree(source, destination)
    except:
        print "Component did not produce any includes"

    try:
        for lib in artifacts['libs']:
            source = os.path.join(get_source_dir(working_dir), lib['source'])
            destination = os.path.join(libs_dir, lib['name'])
            print "Copying lib from:%s to:%s" % tuple([source, destination])
            shutil.copy(source, destination)
    except:
        print "Component did not produce any libs"


def patch_files(patches, source_dir, name):
    for patch in patches:
        original_file = os.path.join(source_dir, patch['file'])
        patch_file = os.path.join('components', name, 'patches', patch['patch'])
        call(['patch', original_file, patch_file])