# 读写INI文件
```python

import configparser

### 创建config
config = configparser.ConfigParser()
config['DEFAULT'] = {'name': 'mdb'}
config["memory"] = {'total': 13190108, 'available': 11745396}
config['ipaddress'] = {'IP': "192.168.168.138"}
config['CPUnum'] = {'CPU': 4}

with open('config.ini', 'w') as conf_fh:
    config.write(conf_fh)

### 读取 ini 文件
conf = configparser.ConfigParser()
conf.read("config.ini")
print(dict(conf))

```

# TOML文件

```python
import toml
def load_toml(file):
    config = toml.load(file)
    return config
```

# YAML文件

