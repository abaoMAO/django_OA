echo "===========进入git项目django-OA目录============="
cd /product/django_OA/


echo "==========切换到release(发布分支）==============="
git checkout release

echo "==================git fetch======================"
git fetch

echo "==================git pull======================"
git pull

echo "===============切换到虚拟环境OAenv================"
workon OAenv


echo "===通过pip 更新requirements.txt中的依赖项=========="
pip install -r requirements.txt 


echo "============makemigrations==================="
python manage.py makemigrations


echo "=================migrate=========================="
python manage.py migrate

echo "============收集静态文件============="
python manage.py collectstatic

echo "====================关闭uWSGI====================="
uwsgi --stop uwsgi.pid  # 关闭uwsgi


echo "================sleep 10s========================="
for i in {1..10}
do
	echo $i"s"
	sleep 1s
done


echo "====================启动uWSGI====================="
uwsgi --ini uwsgi.ini   # 启动uwsgi配置




