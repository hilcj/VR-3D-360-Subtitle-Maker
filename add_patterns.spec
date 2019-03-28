# -*- mode: python -*-

block_cipher = None


a = Analysis(['add_patterns.py'],
             pathex=['/home/desmond/Desktop/angel/VR/backup'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='add_patterns',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True , resources=['alpha_blend.cpython-36m-x86_64-linux-gnu.so,dll,alpha_blend.cpython-36m-x86_64-linux-gnu.so', 'create_vr_mapping.cpython-36m-x86_64-linux-gnu.so,dll,create_vr_mapping.cpython-36m-x86_64-linux-gnu.so'])
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='add_patterns')
