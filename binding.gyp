# ===
# This is the main GYP file, which builds better-sqlite3 with SQLite3 itself.
# ===

{
  'includes': ['deps/common.gypi'],
  'targets': [
    {
      'target_name': 'better_sqlite3',
      'sources': ['src/better_sqlite3.cpp'],
      'cflags': ['-std=c++14'],
      'xcode_settings': {
        'OTHER_CPLUSPLUSFLAGS': ['-std=c++14', '-stdlib=libc++'],
      },
      'conditions': [
        ['OS=="linux"', {
          'ldflags': [
            '-Wl,-Bsymbolic',
            '-Wl,--exclude-libs,ALL',
          ],
        }],
        ['sqlite3_systemlib == ""', {
          'dependencies': ['deps/sqlite3.gyp:sqlite3'],
        }],
        ['sqlite3_systemlib != ""', {
          'ldflags': [
            '<!@(pkg-config sqlite3 --libs)'
          ],
        }],
      ],
    },
    {
      'target_name': 'test_extension',
      'conditions': [
        ['sqlite3 == ""', { 'sources': ['deps/test_extension.c'] }],
        ['sqlite3_systemlib == ""', {
          'dependencies': ['deps/sqlite3.gyp:sqlite3'],
        }],
      ],
    },
  ],
}
