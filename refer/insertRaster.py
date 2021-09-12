import subprocess
import os

path_PostgreSQL = 'C:\\software\\PostgreSQL\\bin'
path_data = 'E:\\code\\PythonProject\\rasterAnal\\data\\image\\PMS_after.tiff'
cmd = f"""
set path={path_PostgreSQL}
call raster2pgsql -s 4326 -I -C -M {path_data} -F -t auto public.PMS | psql -d postgres -U postgres -p 5432
pause
admin
"""
passwd = 'admin'
child = subprocess.Popen(cmd)
child.stdin.write(passwd)  # 你的密码


