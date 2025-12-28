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

# 添加常用工具
git add ./weekly/
git add ./how-to/
git add ./labs/
git add ./newsletters/
git add ./reviews/
git add ./tools/
# 添加修改文件
git add -u
git commit -m "docs: update vault by scripts"
git push origin main 
