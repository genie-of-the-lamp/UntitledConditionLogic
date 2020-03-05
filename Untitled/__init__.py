# -*- coding : utf-8 -*-
# 2020.03.04 ~
# author : genie.jung
# language : python 3.7.3

from .option import *
from .logic import *


# This project is developed by borrowing the ideas used in Macevision's COBA 3.0 version.
# 주요 대상 고객층은 일본의 자동차 내부 전선망 개발 회사인 Yazaki Group 이지만,
# 그 외의 옵션이 있는 어떤 클라이언트라도 커버할 수 있게끔 개발하는 것을 목표로 한다.
# Yazaki의 옵션 구성의 복잡도는 최대 3개의 옵션이 엮이는 것으로 예상한다.
# (ex) 코바컨디션 형식으로 봤을 떄 "A and (B or C)"의 정도.)
