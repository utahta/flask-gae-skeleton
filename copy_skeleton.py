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
    from_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'app')

    print from_dir, ' to ', to_dir
    shutil.copytree(from_dir, to_dir)
    os.chdir(to_dir)
    os.system('git remote rm origin')
