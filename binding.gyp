{
  "targets": [
    {
      "target_name": "pdtools",
      "sources" : [
        "src/pdtools.cpp",
        "src/PdObject.cpp",
        "src/RtAudio.cpp",
        "src/externals/freeverb~.c"
      ],
      "type" : "executable",
      "defines" : [
        "PD",
        "LIBPD_USE_STD_MUTEX", 
        "HAVE_UNISTD_H", 
        "__MACOSX_CORE__",
        "USEAPI_DUMMY"
      ],
      "include_dirs" : [
        "../libpd/libpd_wrapper",
        "../libpd/pure-data/src",
        "../libpd/libpd_wrapper/util",
        "../libpd/cpp",
        "./src",
      ],
      "link-settings" : {
        "ldflags" : ["-mmacosx-version-min=10.15"],
        'libraries' : [
          '/usr/local/lib/libpd/libpd.dylib',
          'Foundation.framework',
          'CoreAudio.framework'
        ]
      },
      "ldflags" : ["-mmacosx-version-min=10.15"],
      "libraries" : [
        '/usr/local/lib/libpd/libpd.dylib',
        'Foundation.framework',
        'CoreAudio.framework'
      ],
      "cflags" : ["-std=c++11" "-03", "-mmacosx-version-min=10.15" ],
      "cflags_cc" : ["-std=c++11", "-03", "-mmacosx-version-min=10.15"],
      'cflags!': [ '-fno-exceptions', '-mmacosx-version-min' ],
      'cflags_cc!': [ '-fno-exceptions', '-mmacosx-version-min'],
      'conditions': [
        ['OS=="mac"', {
          'xcode_settings': {
            'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
            'MACOSX_DEPLOYMENT_TARGET' : '10.15'
          }
        }]
      ]
    }
  ]
}