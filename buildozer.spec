name: Build APK

on:
  push:
    branches: [ main ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Setup Python
      uses: actions/setup-python@v5
      with:
        python-version: "3.10"

    - name: Install system dependencies
      run: |
        sudo apt update
        sudo apt install -y git zip unzip openjdk-17-jdk \
        autoconf libtool pkg-config \
        zlib1g-dev libncurses5-dev libncursesw5-dev \
        libtinfo6 cmake libffi-dev libssl-dev

    - name: Install Buildozer + dependencies
      run: |
        python -m pip install --upgrade pip
        pip install --upgrade buildozer cython setuptools wheel

    # 🔥 FIX PRINCIPAL: força reinstalação limpa TOTAL
    - name: Clean EVERYTHING
      run: |
        rm -rf .buildozer
        rm -rf ~/.buildozer

    # 🔥 FORÇA download correto do python-for-android
    - name: Build APK (force fresh install)
      run: |
        buildozer android clean
        buildozer android update
        buildozer -v android debug
