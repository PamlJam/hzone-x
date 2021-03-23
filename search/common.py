from django.db.models import Q
# 引入对象
def commonSearch(query_target,query_field,query_words):
# 通用查询
    conditions = None
    # 筛选条件
    for word in query_words.split():
    # 分割关键字
        if conditions == None:
            conditions = Q(**{query_field + '__contains': word})
            # 动态查询
        else:
            conditions |= Q(**{query_field + '__contains': word})
            # 逻辑复合
    return query_target.objects.filter(conditions)
    # 结果列表