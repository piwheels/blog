build:
	BEEMO_POSTS_DIR=/home/ben/Projects/piwheels/blog/posts \
	BEEMO_STATIC_DIR=/home/ben/Projects/piwheels/blog/static \
	BEEMO_TEMPLATES_DIR=/home/ben/Projects/piwheels/blog/templates \
	BEEMO_OUTPUT_DIR=/home/ben/Projects/piwheels/blog/www \
	beemo

serve:
	python -m http.server -d www 8001 &