{'targets': [{
    'target_name' : 'pdf',
    'include_dirs': [
        '<!(node -e "require(\'nan\')")',
        'opt/include/poppler/qt5',
        'opt/include/poppler',
        'opt/include/QtCore',
        'opt/include',
    ],
    'sources': [
        'src/pdf.cc',
        'src/NodePopplerAsync.cc',
        'src/NodePoppler.cc'
    ],
    'cflags!': [ '-fno-exceptions' ],
    'cflags_cc!': [ '-fno-exceptions' ],
    'cflags':[ '<!@(pkg-config cairo --cflags)' ],
    'libraries': [
        '<!@(pkg-config cairo --libs)',
        '-lpoppler-qt5',
        '-lQt5Core',
        '-lQt5Gui',
    ],
    'conditions': [
        ['OS=="mac"', {
            'libraries': [ '-L<(PRODUCT_DIR)/../../opt/lib' ],
            'xcode_settings':{
                'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
                'OTHER_CFLAGS': [
                    '-std=c++11',
                    '-stdlib=libc++',
                    '-fexceptions',
                    '<!@(pkg-config poppler-qt5 --cflags)'
                ]
            }
        }],
        ['OS=="linux"', {
            'cflags': [
                '-I<(PRODUCT_DIR)/../../opt/include',
                '-I<(PRODUCT_DIR)/../../opt/include/poppler/qt5',
                '-I<(PRODUCT_DIR)/../../opt/include/poppler',
            ],
            'libraries': [
                '-L<(PRODUCT_DIR)/../../opt/lib'
            ]
        }]
  ]
}
]}
