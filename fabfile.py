from fabric import colors
from fabric.api import task
from fabric.api import env
from fabric.api import run
from fabric.api import cd
from fabric.api import prefix


env.hosts = ['tarjimonlar.org']
env.user = 'ubuntu'
env.key_filename = '/home/sardor/digkey.pem'


GITHUB = 'git@github.com:muminoff/tarjimonlar.git'
ROOT = '/home/ubuntu/'
CODE_ROOT = '%s/tarjimonlar' % ROOT
LOCAL_SETTINGS = '%s/tarjimonlar/config/production.py' % CODE_ROOT
GUNICORN = '/usr/local/bin/gunicorn'


@task
def git_pull():
    with cd(CODE_ROOT):
        run('git pull origin develop')


@task
def install_requirements():
    print(colors.cyan('Installing requirements...', bold=True))
    with cd(CODE_ROOT):
        run('pip install -U -r requirements.txt')
        run('pip install -e .')


@task
def deploy():
    """Deploy code to production"""
    print(colors.cyan('Deploying...', bold=True))
    with cd(CODE_ROOT):
        run('git pull origin develop')
        clear_cache()
        run('find . -name "*.pyc" -delete')
        restart()


@task
def clear_cache():
    with cd(CODE_ROOT):
        run('redis-cli -n 1 flushdb')


@task
def get_stat():
    with cd(CODE_ROOT):
        run("redis-cli -n 0 zrevrange ")
        run("redis-cli -n 0 get $(redis-cli -n 0 keys *posts |awk '{print $1 }'|head -n 1)")


@task
def restart():
    with cd(CODE_ROOT):
        run('supervisorctl -c deploy/supervisord.conf restart all')
