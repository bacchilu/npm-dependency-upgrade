# npm-dependency-upgrade

If you want to update all your npm dependecies, this Python script is a usefull alternative to _npm update_ since it ignores the versioning tag in "package.json" updating it with the new version.

Since "node_packages/" "and package-lock.json" (actually this is moved to "/tmp/") are removed and recreated, not only top-level packages are upgraded.

Usage (run from the save directory of "package.json"):

    python3 BUILD.py
