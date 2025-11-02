# Up-to-date SWIG & SWIG JSE conan recipes

These are the `conan` recipes used for https://swig.momtchev.com/artifactory/api/conan/swig-jse

They are based on the official `conan` packages by [@valgur](https://github.com/conan-io/conan-center-index/pull/19058) but include the latest versions

* SWIG 4.4.0
* SWIG JSE 5.0.10

## Usage

Add the SWIG JSE repository:

```bash
conan remote add swig-jse https://swig.momtchev.com/artifactory/api/conan/swig-jse
```

### From a `conan` recipe

```ini
[tool_requires]
swig-jse/[>=5.0.10]
```

or

```ini
[tool_requires]
swig/[>=4.4.0]
```

### Use without conan

Add the SWIG JSE repository:

```bash
conan remote add swig-jse https://swig.momtchev.com/artifactory/api/conan/swig-jse
```

Download and install the package:
```bash
conan install -of /tmp --requires swig-jse/5.0.10 --deployer-folder=${TARGET_FOLDER} --deployer-package='*' --deployer=runtime_deploy
```

SWIG JSE will be available in `${TARGET_FOLDER}` with the shell scripts required to activate the environment in `/tmp`. You do not need any activation starting from SWIG JSE 5.0.8, SWIG main or SWIG JSE <5.0.8 need the `SWIG_LIB` environment variable.

# Support platforms

Both packages have been tested on:
  - `Linux-gcc-x64`
  - `macOS-clang-x64`
  - `macOS-clang-arm64`
  - `Windows-MSVC-MSYS2-x64`
