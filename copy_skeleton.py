import sys
import os
import shutil
from optparse import OptionParser

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-t', '--to', dest='to', default=None, help='create project.')

    (opt, args) = parser.parse_args()
    if not opt.to:
        parser.print_help()
        sys.exit(1)

    to_dir = os.path.abspath(opt.to)
    from_dir = os.path.dirname(os.path.abspath(__file__))

    print from_dir, ' to ', to_dir
    shutil.copytree(from_dir, to_dir, symlinks=True)
    os.remove(os.path.join(to_dir, 'copy_skeleton.py'))
    try:
        os.remove(os.path.join(to_dir, 'copy_skeleton.pyc'))
    except:
        pass
    os.remove(os.path.join(to_dir, 'readme.md'))
    os.chdir(to_dir)
    os.system('git remote rm origin')
