from  models import Feature_Services


def add_feature_service(id,name,schema,bound,attribution,tileurl,description):
    '''
    :param id: 矢量服务的名称
    :param name: 矢量服务的名称
    :param schema: 矢量服务存储的系统
    :param bound: 矢量服务的四至
    :param attribution: 矢量服务的属性字段
    :param tileurl: 矢量服务的访问地址
    :param description: 矢量服务的描述
    :return:
    '''
    feature_service = Feature_Services(id,name,schema,bound,attribution,tileurl,description)

    feature_service.save()
