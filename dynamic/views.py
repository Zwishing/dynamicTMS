import grequests
import requests
import json as json_
from sanic.log import logger
from sanic import Blueprint
from sanic.response import raw, json
from settings import PG_TILE_SERV
from models import Feature_Services
from utils import feature2postgis
from db import add_feature_service
import aiofiles

feature_bp = Blueprint('feature', url_prefix='feature')
function_bp = Blueprint('function', url_prefix='function')
publish_bp = Blueprint('publish', url_prefix='publish')

@publish_bp.post('/upload')
async def uplaod_file(request): #上传文件的接口
    f = request.files.get('file')
    async with aiofiles.open(f'../uploads/{f.name}','wb') as file:
        await file.write(f.body)
        return json({'':''})

@publish_bp.post('/publish')
async def publish_feature(request): #入库发布的接口
    # feature2postgis()
    # add_feature_service()
    pass

@feature_bp.get('/services')
async def get_feature_services(request): #获取矢量服务的接口
    urls = []
    results = []
    res=await _get_services()

    for k,v in res.items():
        if v['type']=='table':
            urls.append(v['detailurl'])
    res_list = await _get_services_detail(urls)

    for res in res_list:
        res = json_.loads(str(res.content, 'utf-8'))
        results.append(res)

    return json(results)


@function_bp.post('/services')
async def get_function_services(request): #获取函数服务的接口
    pass


@feature_bp.get('/<layer>/<z:int>/<x:int>/<y:(?P<y>\d+).pbf>',name ='get_tile_postgis')
async def get_tile_postgis(request, layer, x, y, z): #矢量服务加载的接口
    url = f'http://{PG_TILE_SERV["host"]}:{PG_TILE_SERV["port"]}/{layer}/{z}/{x}/{y}.pbf'
    res = await _get_tile(url)
    return res


async def _get_tile(url):
    req_list = [grequests.get(url)]
    res = grequests.map(req_list)[0]

    return raw(res.content,
               headers={"Content-Type": "application/x-protobuf"})

async def _get_services():
    url = f'http://{PG_TILE_SERV["host"]}:{PG_TILE_SERV["port"]}/index.json'
    res = grequests.map([grequests.get(url)])[0]
    res = json_.loads(str(res.content, 'utf-8'))
    return  res

async def _get_services_detail(urls):
   return grequests.map([grequests.get(url) for url in urls])
