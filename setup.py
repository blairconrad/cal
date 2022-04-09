import setuptools

package_name = "cal"
url = "https://github.com/blairconrad/cal"

with open("src/cal/release_notes.md", "r") as notes:
    for line in notes:
        if line.startswith("## "):
            version = line[3:].strip()
            break

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=package_name,
    version=version,
    author="Blair Conrad",
    author_email="blair@blairconrad.com",
    description="Prints a calendar on the console",
    keywords="calendar console python",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=url,
    download_url="%(url)s/releases/%(version)s" % vars(),
    package_dir={"": "src"},
    packages=setuptools.find_packages("src"),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
    ],
    entry_points={"console_scripts": ["cal=cal.__main__:main"]},
)
