
# Python installation on Ubuntu

## Prerequisites

- Ensure you have `sudo` privileges.
- A stable internet connection is required.
- Update your system's package list to ensure you have the latest versions using `sudo apt update` command.

## Instructions to install Python (`3.11.11`) on Ubuntu (`24.04-LTS`)

> The analogous steps should be followed for other versions of Python or Linux distributions, though the commands may vary.

### 1. **Download [gzipped source tarball](https://www.python.org/ftp/python/3.11.11/Python-3.11.11.tgz) file from python.org**

If you haven't already downloaded the file, you can use `wget` to download it directly to your unix machine.

```bash

wget  https://www.python.org/ftp/python/3.11.11/Python-3.11.11.tgz

```

### 2. **Extract the `.tgz` archive**

Once the file is downloaded, extract it using the `tar` command.

> This command will extract the contents to a `Python-3.11.11` directory.

```bash

tar  -xvzf  Python-3.11.11.tgz

```

### 3. **Install dependencies**

Before building Python, you need to install some development tools and libraries that Python depends on.

> Run the following commands to ensure the required packages are installed.

```bash

sudo  apt  update

sudo  apt  install  -y  build-essential  libssl-dev  zlib1g-dev  libbz2-dev  \

libreadline-dev  libsqlite3-dev  wget  curl  llvm  \

libncurses5-dev  libncursesw5-dev  libssl-dev  \

libgdbm-dev  libdb5.3-dev  liblzma-dev  tk-dev  \

libffi-dev  liblzma-dev  python3-openssl  git

```

### 4. **Configure and Build Python**

Navigate to the extracted Python directory, and configure the build process by running `./configure` process to set up the necessary files for building Python.

> The `--enable-optimizations` flag helps with optimizing the Python binary.

```bash

cd  Python-3.11.11

./configure  --enable-optimizations

```

Once the configuration is done, start the build process.

> Here, `$(nproc)` will automatically set the number of CPU cores to speed up the process.

```bash

make  -j$(nproc)

```

### 5. **Install Python**

Once the build process is complete, install Python 3.11.11 to your system:

> We use `altinstall` instead of `install` to avoid overwriting the default system Python (if any).

```bash

sudo  make  altinstall

```

### 6. **Verify the installation**

Finally, verify that Python 3.11.11 was installed correctly by checking the version:

> It should display something like `Python 3.11.11`

```bash

python3.11  --version

```

---
