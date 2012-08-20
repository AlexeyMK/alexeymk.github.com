# idea:
# ensure git is ready.
# copy over everything that doesn't start with an underscore
# copy over _site
# push to published branch

from tempfile import mkdtemp
import os
import sys
SOURCE_BRANCH_NAME = "blog_source"
PUBLIC_BRANCH_NAME = "master"

commitname = " ".join(sys.argv[1:])
if not commitname:
    exit("what name should this commit/post be?")

if os.system('git checkout %s' % SOURCE_BRANCH_NAME) != 0:
    exit("your branch is weird!")
publish_dir = mkdtemp()
# assume you are in branch 'master'
for file_or_dir in os.listdir(os.getcwd()):
    if file_or_dir[0] not in '_.':
        cmd = "cp -r %s %s" % (file_or_dir, publish_dir)
        print cmd
        os.system(cmd)

os.system("jekyll")
for file_or_dir in os.listdir(os.path.join(os.getcwd(), "_site")):
    cmd = "cp -r %s %s" % (os.path.join(os.getcwd(), "_site", file_or_dir),
                           publish_dir)
    print cmd
    os.system(cmd)

if os.system('git checkout %s' % PUBLIC_BRANCH_NAME) != 0:
    exit("couldn't change branches, aborting")

# get rid of everything old
os.system("rm -r *")

for file_or_dir in os.listdir(publish_dir):
    cmd = "cp -r %s %s" % (os.path.join(publish_dir,file_or_dir), os.getcwd())
    print cmd
    os.system(cmd)

os.system("git add .")
os.system("git commit -am \"%s\"" % commitname)
os.system("git push public %s" % PUBLIC_BRANCH_NAME)
os.system("git checkout %s" % SOURCE_BRANCH_NAME)

# uncomment once everything works
#shutil.rmtree(publish_dir)
