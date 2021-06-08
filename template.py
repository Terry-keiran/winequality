import os



dirs=[
    os.path.join("data","raw"),
    os.path.join("data","processed"),
    "notebook",
    "models",
    os.path.join("src","data"),
    os.path.join("src","features"),
    os.path.join("src","models"),
    os.path.join("src","visualization")

]

for dir in dirs:
    os.makedirs(dir,exist_ok=True)
    with open(os.path.join(dir,".gitkeep"),"w") as f:
        pass

files=[
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    os.path.join("src","__init__.py")
    ]

for file in files:
    with open(file,"w") as f:
        pass
    