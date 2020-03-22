# !/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @project : DjangoBlog
# @file    : jd_cps.py
# @time    : 2020/3/21 21:57
# @author  : GuangLin
# @version : 0.01
# @desc    :


import jd.api
import json


def get_share_link(link):
    jd.setDefaultAppInfo("82af29e9ffadfc0bfa495cfeeda80657", "dbccb28df7a148dcba1fdbc80bd4ea2c")

    a = jd.api.jdUnionOpenPromotionCommonGet()

    a.param_json = json.dumps({
        "promotionCodeReq": {
            "materialId": link,
            "siteId": "2031455107",
        }
    })

    f = a.getResponse()
    result = json.loads(f['jd_union_open_promotion_common_get_response']['result'])['data']
    print(result)
    return result.get("clickURL")


if __name__ == '__main__':
    print(get_share_link("https://item.jd.com/31332274597.html"))
