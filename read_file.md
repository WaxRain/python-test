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

```python

import yaml
def load_yaml(file):
    with open(file, 'r') as fh:
        return yaml.load(fh, Loader=yaml.FullLoader)

config = load_yaml(yaml_file)
print(config)

```


# Perl读取INI文件 (二维哈希)
```perl
use Config::IniFiles;
my $config_file = "config.ini";
my %ini;
tie %ini, 'Config::IniFiles', ( -file => $config_file );
foreach my $c (keys %ini){
    foreach my $key (keys %{$ini{$c}}) {
        print $c."\t".$key."\t".$ini{$c}{$key}."\n";
    }
}

```

# perl读取INI文件（没有找到方法遍历）
```perl
use Config::IniFiles;
my $config_file = "config.ini";
my $cfg = new Config::IniFiles( -file => $config_file );
print $cfg->val('DEFAULT', 'name');
```

