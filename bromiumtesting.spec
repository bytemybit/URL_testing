# -*- mode: python -*-
a = Analysis(['bromiumtesting.py'],
             pathex=['C:\\Users\\mccoydo\\PycharmProjects\\URL testing'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='bromiumtesting.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
