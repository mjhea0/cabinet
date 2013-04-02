from flask.ext.assets import Bundle
from app import assets

css = Bundle('less/main.less',
	filters='less, yui_css', output='css/main.css')

js = Bundle('js/main.js',
	filters='yui_js', output='js/main-min.js')

assets.register('js', js)
assets.register('css', css)