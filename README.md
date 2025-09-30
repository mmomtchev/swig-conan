# Up-to-date SWIG & SWIG JSE conan recipes

These are the `conan` recipes used for https://swig.momtchev.com/artifactory/api/conan/swig-jse

They are based on the official `conan` packages by [@valgur](https://github.com/conan-io/conan-center-index/pull/19058) but include the latest versions

* SWIG 4.3.0
* SWIG JSE 5.0.7

## Usage

```
conan remote add swig-jse https://swig.momtchev.com/artifactory/api/conan/swig-jse
```

### From a `conan` recipe

```ini
[tool_requires]
swig-jse/[>=5.0.7]
```

or

```ini
[tool_requires]
swig/[>=4.3.0]
```

### Use without conan

Download and install the package:
```
conan install -r swig-jse -r conancenter --requires swig-jse/5.0.7
```

Check the package ID:
```bash
conan list 'swig-jse/5.0.7:*'
```

Find its directory (the hex number is the package ID):
```bash
conan cache path swig-jse/5.0.7:dcf68e932572755309a5f69f3cee1bede410e907
export SWIG_DIR=`conan cache path swig-jse/5.0.7:dcf68e932572755309a5f69f3cee1bede410e907`
```

Try running:
```bash
SWIG_LIB=${SWIG_DIR}/swiglib ${SWIG_DIR}/swig-jse
```

At the moment this is somewhat ugly because SWIG does not support specifying a `SWIG_LIB` directory relative to its executable in order to create a relocatable package.

# Support platforms

Both packages have been tested on:
  - `Linux-gcc-x64`
  - `macOS-clang-x64`
  - `macOS-clang-arm64`
  - `Windows-MSVC-MSYS2-x64`
