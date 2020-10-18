import yaml
import os

def read(yaml_name=None):

    # 获取当前脚本所在文件夹路径
    curPath = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    # print(curPath)

    # 获取yaml文件路径
    yamlPath = os.path.join(curPath, "config/"+yaml_name)
    # print(yamlPath)

    # open方法打开直接读出来
    f = open(yamlPath, 'r', encoding='utf-8')
    cfg = f.read()
    d = yaml.safe_load(cfg)  # 用load方法转字典
    return d

