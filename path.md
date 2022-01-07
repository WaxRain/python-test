# 遍历目录查询特定后缀文件
1. 仅遍历目录下文件，不含子目录
2. 可多个后缀
3. 可多种后缀文件
4. 文件名称中不可出现点（.），如test.a.txt 后缀理解为['.a', '.txt']

```python
from pathlib import Path
def get_special_type_files(directory, suffixes=[]):
    files = (str(p.resolve()) for p in Path(directory).glob("**/*") \
                    if p.suffixes in suffixes)
    yield from files

for f in get_special_type_files(dir, [['.fastq'], ['.fastq', '.gz'], ['.fq'], ['.fq', '.gz']])
```

# 判断文件是否存在
1. 路径不存在报错
2. 存在但不是文件报错

```python
from pathlib import Path
def if_file_exists(file):
    if not Path(file).is_file():
        raise FileNotFoundError('file not found at: {}'.format(file))
```

