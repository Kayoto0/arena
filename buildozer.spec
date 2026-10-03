[app]
title = Arena Studio
package.name = arenastudiobuild
package.domain = org.arenastudio
source.dir = .
source.include_exts = atlas,bin,bmp,cfg,csv,gif,glb,gltf,ico,ini,jpeg,jpg,json,mp3,mtl,obj,ogg,otf,png,py,svg,ttf,txt,wav,webp
source.exclude_dirs = .buildozer,bin,.github,__pycache__
source.exclude_patterns = README_ANDROID.txt,buildozer.spec,build_apk.sh,.arena_android_manifest.json
version = 13.35.0
requirements = python3,sdl2,sdl2_image,sdl2_mixer,sdl2_ttf,pygame,numpy,pillow
orientation = landscape
fullscreen = 1
p4a.branch = v2023.09.16
android.api = 33
android.ndk = 25b
android.minapi = 24
android.archs = arm64-v8a
android.accept_sdk_license = True
android.logcat_filters = *:S python:D
icon.filename = %(source.dir)s/data/icon.png
presplash.filename = %(source.dir)s/data/presplash.png

[buildozer]
log_level = 2
warn_on_root = 0
