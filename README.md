# Up-to-date SWIG & SWIG JSE conan recipes

These are the `conan` recipes used for https://swig.momtchev.com/artifactory/api/conan/swig-jse

They are based on the official `conan` packages by [@valgur](https://github.com/conan-io/conan-center-index/pull/19058) but include the latest versions

* SWIG 4.2.1
* SWIG JSE 5.0.3

## Usage

```
conan remote add swig-jse https://swig.momtchev.com/artifactory/api/conan/swig-jse
```

```ini
[tool_requires]
swig-jse/[>=5.0.3]
```

or

```ini
[tool_requires]
swig/[>=4.2.1]
```

Both packages have been tested on Linux-gcc-x64, macOS-clang-x64, macOS-clang-arm64 and Windows-MSVC-MSYS2-x64
