# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import os
import sys

from typing import List

from alibabacloud_swas_open20200601.client import Client as SWAS_OPEN20200601Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_swas_open20200601 import models as swas__open20200601_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_console.client import Client as ConsoleClient
from alibabacloud_tea_util.client import Client as UtilClient


class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> SWAS_OPEN20200601Client:
        """
        使用AK&SK初始化账号Client
        @param access_key_id:
        @param access_key_secret:
        @return: Client
        @throws Exception
        """
        # 工程代码泄露可能会导致 AccessKey 泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考，建议使用更安全的 STS 方式，更多鉴权访问方式请参见：https://help.aliyun.com/document_detail/378659.html。
        config = open_api_models.Config(
            # 必填，请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_ID。,
            access_key_id='',
            # 必填，请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_SECRET。,
            access_key_secret=''
        )
        # Endpoint 请参考 https://api.aliyun.com/product/SWAS-OPEN
        config.endpoint = f'swas.cn-hongkong.aliyuncs.com'
        return SWAS_OPEN20200601Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_instances_request = swas__open20200601_models.CreateInstancesRequest(
            region_id='cn-hongkong',
            image_id='8b798eb927684a08b26bb95da94f5812',
            plan_id='swas.s2.c2m1s40b30t1.un',
            period=1,
            auto_renew=True
        )
        runtime = util_models.RuntimeOptions()
        try:
            resp = client.create_instances_with_options(create_instances_request, runtime)
            ConsoleClient.log(UtilClient.to_jsonstring(resp))
        except Exception as error:
            # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
            # 错误 message
            print(error.message)
            # 诊断地址
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_instances_request = swas__open20200601_models.CreateInstancesRequest(
            region_id='cn-hongkong',
            image_id='8b798eb927684a08b26bb95da94f5812',
            plan_id='swas.s2.c2m1s40b30t1.un',
            period=1,
            auto_renew=True
        )
        runtime = util_models.RuntimeOptions()
        try:
            resp = await client.create_instances_with_options_async(create_instances_request, runtime)
            ConsoleClient.log(UtilClient.to_jsonstring(resp))
        except Exception as error:
            # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
            # 错误 message
            print(error.message)
            # 诊断地址
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)


if __name__ == '__main__':
    Sample.main(sys.argv[1:])
