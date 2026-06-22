[app]

title = StockPro
package.name = stockpro
package.domain = org.stockpro

source.dir = .
source.include_exts = py,png,jpg,kv,txt,json,html,css,js

version = 1.0.0

requirements = python3,kivy,flask,requests

orientation = portrait

android.api = 31
android.minapi = 21
android.build_tools_version = 30.0.3
android.skip_update = False

android.permissions = INTERNET,ACCESS_NETWORK_STATE

log_level = 2
warn_on_root = 1
