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
    'cflags':[ '<!@(pkg-config cairo --cflags)' ],
    'libraries': [ '<!@(pkg-config cairo --libs)', ],
    'conditions': [
        ['OS=="mac"', {
            'libraries': [ '<!@(pkg-config poppler-qt5 --libs)' ],
            'xcode_settings':{
                'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
                'OTHER_CFLAGS': [
                    '<!@(pkg-config poppler-qt5 --cflags)',
                    '-mmacosx-version-min=10.9',
                    '-stdlib=libc++',
                    '-std=c++11',
                ]
            }
        }],
        ['OS=="linux"', {
            'cflags': [
                '-I<(PRODUCT_DIR)/../../opt/include',
                '-I<(PRODUCT_DIR)/../../opt/include/poppler/qt5',
                '-I<(PRODUCT_DIR)/../../opt/include/poppler',
                '-lQt5Core',
                '-lQt5Gui',
            ],
            'libraries': [
                '-lpoppler-qt5',
                '-L<(PRODUCT_DIR)/../../opt/lib'
            ]
        }]
  ]
}
]}
