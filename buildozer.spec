[app]

# Application title
title = AI Assistant

# Package name
package.name = aichat

# Package domain
package.domain = org.test

# Source directory
source.dir = .

# Main file
source.main = main.py

# Application version
version = 1.0.0

# Requirements
requirements = python3, kivy==2.2.1

# Orientation
orientation = portrait

# Android specific
android.api = 33
android.minapi = 21
android.sdk = 23
android.ndk = 23b
android.ndk_api = 21

# Architectures (use only one to speed up build)
android.archs = arm64-v8a

# Permissions
android.permissions = INTERNET

# Automatically accept SDK licenses
android.accept_sdk_license = True

# Build directory
build_dir = ./.buildozer
bin_dir = ./bin

[buildozer]
# Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2
