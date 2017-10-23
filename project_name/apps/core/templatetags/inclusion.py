from django import template
from django.db.models import Count
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from project_name.apps.module.models import RoleModule, RoleModuleItem
from project_name.apps.user.models import User
from .. import constants as core_constants
from django.core.cache import cache, caches

register = template.Library()


@register.inclusion_tag('themes/partials/menu_brand/menu_1.html',
                        takes_context=True)
def tag_menu_siderbar_one(context):
    request = context['request']
    user = User.objects.get(email=request.user)
    user_key = "{0}_menu_siderbar_key".format(str(user.id))
    if not cache.get(user_key):
        module_team = RoleModule.current.filter(
            roleId=user.roleId, moduleId__bandType=core_constants.CODE_BAND_ONE,
            moduleId__isDeleted=False
        ).values('moduleId', 'moduleId__order', 'roleId').annotate(
            dcount=Count('moduleId')).order_by('moduleId__order')
        result = dict()
        for x in module_team.iterator():
            m_team = RoleModule.current.get(
                moduleId=x["moduleId"], roleId=x["roleId"])
            if m_team.moduleId.order not in result.keys():
                result[m_team.moduleId.order] = list()
            add_module_dict = dict(
                module=dict(
                    text=m_team.moduleId.name, match=m_team.moduleId.match,
                    submodule=dict(), icon=m_team.moduleId.icon,
                    urlname=m_team.moduleId.urlName
                )
            )
            result[m_team.moduleId.order].append(add_module_dict)
            m_item_team = RoleModuleItem.current.filter(
                roleModuleId=m_team)
            if m_item_team.exists():
                for y in m_item_team:
                    dict_sub_menu = result[m_team.moduleId.order][0]['module'][
                        'submodule']
                    if y.moduleitem.reference not in dict_sub_menu.keys():
                        dict_sub_menu[y.moduleitem.reference] = list()
                    add_module_dict = dict(text=y.moduleitemId.name,
                                           match=y.moduleItemId.match)
                    dict_sub_menu[y.moduleitemId.reference].append(
                        add_module_dict)
        cache.set(user_key, result, 60 * 30)
        return {'result': result, 'request': request}
    else:
        return {'result': cache.get(user_key), 'request': request}


@register.inclusion_tag('themes/partials/menu_brand/menu_2.html', takes_context=True)
def tag_menu_siderbar_two(context):
    """for order need change line 22, 29, 34"""
    request = context['request']
    user = User.objects.get(email=request.user)
    module_team = RoleModule.current.filter(
        roleId=user.roleId, moduleId__bandType=core_constants.CODE_BAND_TWO,
        moduleId__isDeleted=False
    ).values('moduleId', 'moduleId__order', 'roleId').annotate(
        dcount=Count('moduleId')).order_by('moduleId__order')
    result = dict()
    for x in module_team.iterator():
        m_team = RoleModule.current.get(
            moduleId=x["moduleId"], roleId=x["roleId"])
        if m_team.moduleId.order not in result.keys():
            result[m_team.moduleId.order] = list()
        add_module_dict = dict(
            module=dict(
                text=m_team.moduleId.name, match=m_team.moduleId.match,
                submodule=dict(), icon=m_team.moduleId.icon,
                urlname=m_team.moduleId.urlName
            )
        )
        result[m_team.moduleId.order].append(add_module_dict)
        m_item_team = RoleModuleItem.current.filter(
            roleModuleId=m_team)
        if m_item_team.exists():
            for y in m_item_team:
                dict_sub_menu = result[m_team.moduleId.order][0]['module'][
                    'submodule']
                if y.moduleitemId.reference not in dict_sub_menu.keys():
                    dict_sub_menu[y.moduleitemId.reference] = list()
                add_module_dict = dict(text=y.moduleitemId.name,
                                       match=y.moduleitemId.match)
                dict_sub_menu[y.moduleitemId.reference].append(add_module_dict)
    return {'result': result, 'request': request}


@register.inclusion_tag('themes/partials/page-breadcrumb.html',
                        takes_context=True)
def tag_menu_breadcrumb(context):
    request = context['request']
    current_language = request.LANGUAGE_CODE
    url_name = request.resolver_match.url_name
    parameter_kwargs = ""
    try:
        if request.resolver_match.kwargs:
            parameter_kwargs = request.resolver_match.kwargs
        namespace_name = request.resolver_match.namespaces[0]
        parser = "{0}:{1}".format(str(namespace_name), str(url_name))
    except IndexError:
        namespace_name = 'index'
        parser = "{0}".format(str(namespace_name))
    url_parse = reverse('{0}'.format(str(parser)), kwargs=parameter_kwargs)

    crumbs = url_parse.split('/')[1:-1]
    home = _('Home')

    link = u" <li>" \
           u"<i class='icon-home2 position-left'></i>" \
           u"<a href='/{0:s}/'>{1:s}</a>" \
           u"</li>".format(str(current_language), str(home))
    for index, name in enumerate(crumbs):
        link += u"<li class='active'>{0:s}</li>".format(str(name).lower())
    return {'result': mark_safe(link)}
