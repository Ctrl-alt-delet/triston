setup(
 name="MyFirstTestBot",
 version="1.0.0",
 packages=find_packages(),
 install_requires=
 "requests",
 "flask",
,
 entry_points={
 "console_scripts": 
 "mftb = mftb:app",
 
 }
)
