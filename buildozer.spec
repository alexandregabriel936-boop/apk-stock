[app]

title = StockPro

package.name = stockpro
package.domain = com.stockpro.mobile

source.dir = .
source.include_exts = py,png,jpg,kv

version = 1.0

requirements = python3,kivy,kivymd

orientation = portrait

fullscreen = 0

android.api = 33
android.minapi = 21
android.ndk = 25b
android.build_tools = 33.0.2

android.archs = arm64-v8a

[buildozer]

log_level = 2
warn_on_root = 1
