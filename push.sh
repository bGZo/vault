# +--------------------------+
# Auto Push (changes) Sctipts
# +--------------------------+
# 1. git submodule so parent can use lastest version.
# we assume run this sctipt on root of projects.
cd clippers
git add -u
git commit -m "docs: update clippers by scripts"
git push origin main 
cd -

cd .obsidian
git add -u
git commit -m "docs: update config by scripts"
git push origin main
cd -

git add -u
git commit -m "docs: update vault by scripts"
git push origin main 
