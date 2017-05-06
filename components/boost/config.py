NAME = 'boost'
VERSION = '1.49.0'
DOWNLOADS = ['http://downloads.sourceforge.net/project/boost/boost/%s/boost_%s.tar.bz2' %
            tuple([VERSION, VERSION.replace('.', '_')])]
SOURCE_DIR = 'boost-%s' % VERSION
ARTIFACTS =  {
        'includes': [{
            'source':'boost_%s/boost' % VERSION.replace('.', '_'),
            'name':'boost'
        }]
    }


