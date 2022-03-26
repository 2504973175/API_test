#此文件用于存在测试数据、响应、其中响应可以用来断言
ADD_DATA = {
    "test_add_department_001": {
        "des":"JSON串数据传入所有字段并且格式正确",
        "req_data": {"data": [{"dep_id": "T01", "dep_name": "Test学院", "master_name": "Test-Master", "slogan": "Here is Slogan"}]},
        "res_key": "already_exist",
        "res_value": 0,
        "status_code":201},

    "test_add_department_002": {

        'des':"JSON串数据传入数据：1.dep_id为已存在的数据，其他为正常",
        "req_data": {"data": [{"dep_id": "T01", "dep_name": "Test学院", "master_name": "Test-Master", "slogan": "Here is Slogan"}]},
        "res_key": "already_exist",
        "res_value": 1,
        "status_code":200},

    "test_add_department_003": {
        "des":"JSON串数据传入数据：1.dep_id为空，其他为正常",
        "req_data": {"data": [{"dep_id":"", "dep_name": "dep_id为空学院", "master_name": "dep_id为空Master", "slogan": "Here is dep_id为空"}]},
        "res_key": "dep_id",
        "res_value": "该字段不能为空。",
        "status_code":400},

    "test_add_department_004": {
        "des":"JSON串数据传入数据：1.dep_name为空，其他为正常",
        "req_data": {"data": [{"dep_id": "T02", "dep_name":"", "master_name": "dep_name为空Master", "slogan": "Here is dep_name为空"}]},
        "res_key": "dep_name",
        "res_value": "该字段不能为空。",
        "status_code":400},

    "test_add_department_005": {
        "des":"JSON串数据传入数据：1.master_name为空，其他为正常",
        "req_data": {"data": [{"dep_id": "T02", "dep_name": "T02学院", "master_name": "", "slogan": "Here is master_name为空"}]},
        "res_key": "master_name",
        "res_value": "该字段不能为空。",
        "status_code":400},

    "test_add_department_006": {
        "des":"JSON串数据传入数据：1.slogan为空，其他为正常",
        "req_data": {"data": [{"dep_id": "AZo!T", "dep_name": "AZo!T", "master_name": "AZo!T", "slogan": ""}]},
        "res_key": "already_exist",
        "res_value": 0,
        "status_code":201},
    "test_add_department_007": {
        "des":"JSON串数据传入数据：1.dep_id为含特殊字符，其他为正常",
        "req_data": {"data": [{"dep_id": "t?vWL", "dep_name": "t?vWL1", "master_name": "AZo!T", "slogan": ""}]},
        "res_key": "already_exist",
        "res_value": 0,
        "status_code":200},
    "test_add_department_008": {
        "des":"JSON串数据传入数据：1.dep_name为含特殊字符，其他为正常",
        "req_data": {"data": [{"dep_id": "ae8Vh", "dep_name": "t?vWL", "master_name": "AZo!T", "slogan": ""}]},
        "res_key": "already_exist",
        "res_value": 0,
        "status_code":201},
    "test_add_department_009": {
        "des":"JSON串数据传入数据：1.master_name为含特殊字符，其他为正常",
        "req_data": {"data": [{"dep_id": "dJ3Qm", "dep_name": "dJ3Qm", "master_name": "AZo!T", "slogan": ""}]},
        "res_key": "already_exist",
        "res_value": 0,
        "status_code":201},
    "test_add_department_0010": {
        "des":"JSON串数据传入数据：1.slogan为含特殊字符，其他为正常",
        "req_data": {"data": [{"dep_id": "vP9WU", "dep_name": "vP9WU", "master_name": "vP9WU", "slogan": "AZo!T"}]},
        "res_key": "already_exist",
        "res_value": 0,
        "status_code":201},
    "test_add_department_0011": {
        "des":"JSON串数据传入数据：1.dep_id为超长，其他为正常",
        "req_data": {"data": [{"dep_id": "0lunhNOaB9Ro3iq5H7vTi", "dep_name": "o9b1d", "master_name": "AZo!T", "slogan": ""}]},
        "res_key": "dep_id",
        "res_value": "请确保这个字段不能超过 20 个字符。",
        "status_code":400},
    "test_add_department_0012": {
        "des":"JSON串数据传入数据：1.dep_name为超长，其他为正常",
        "req_data": {"data": [{"dep_id": "RxgaP", "dep_name": "Ovbnxx7nbNJRMC5sdE0ku", "master_name": "AZo!T", "slogan": ""}]},
        "res_key": "dep_name",
        "res_value": "请确保这个字段不能超过 20 个字符。",
        "status_code":400},
    "test_add_department_0013": {
        "des":"JSON串数据传入数据：1.master_name为超长，其他为正常",
        "req_data": {"data": [{"dep_id": "PI3g2", "dep_name": "PI3g2", "master_name": "2N0G8yEFBopAN5UfcHAOJ", "slogan": ""}]},
        "res_key": "master_name",
        "res_value":"请确保这个字段不能超过 20 个字符。",
        "status_code":400},
"test_add_department_0014": {
        "des":"JSON串数据传入数据：1.slogan为超长，其他为正常",
        "req_data": {"data": [{"dep_id": "dtwJ", "dep_name": "dtwJ", "master_name": "dtwJ", "slogan": "WDrN14826gz61iJi4RLMfUMiYFkrNX0z4aXuhDJDGLKov52dHj2xBIGjVkFhOx5puFu0EVZIQpsM00LTRQvEy9rv3HpaDZjWWJuv1"}]},
        "res_key": "slogan",
        "res_value": "请确保这个字段不能超过100个字符。",
        "status_code":400}
}