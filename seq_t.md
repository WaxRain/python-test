
# 碱基序列反向互补
```python
def revcomp(seq):
    """ 碱基序列反向互补 """
    set_all = set('ATCGatcgRYMKrymkVBHDvbhd')
    set_seq = set(seq)
    if set_seq - set_all:
        print("\033[31m* 字符%s超出碱基范围\033[0m" % ",".join(set_seq -set_all))
        return
    seq = seq[::-1]
    return seq.translate( str.maketrans( "ACGTacgtRYMKrymkVBHDvbhd",
                                         "TGCAtgcaYRKMyrkmBVDHbvdh"))
```

# 计算序列中GC含量
```python

from collections import Counter
def gc_percence(seq):
    stat = dict(Counter(seq.upper()))

    gc_num = stat['G'] + stat['C']
    atcg_num = stat['G'] + stat['C'] + stat['A'] + stat['T']

    gc1 = gc_num / len(seq)   # 涵盖序列中 N
    gc2 = gc_num / atcg_num   # 除去N
    print(gc1, gc2)

```


# 读取fasta文件
```python
def readfasta(fname):
    import gzip
    open_func = gzip.open if fname.endswith('gz') else open
    with open_func(fname, 'rt') as fp:
        seqs = []
        for line in fp:
            if line[0] == '>':
                if seqs:
                    yield name, "".join(seqs)
                    seqs = []
                name = line[1:].partition(" ")[0]
            else:
                seqs.append(line[:-1])
        yield name, "".join(seqs)

if __name__ == "__main__":
    import sys
    for name, seq in readfasta(sys.argv[1]):
        print(name, len(seq))
```

# 读取fasta文件(效率基本相同)
```python
def readFasta(fname):
    """ 读取fasta文件，生成器 """
    import gzip
    open_func = gzip.open if fname.endswith('gz') else open
    fp = open_func(fname, 'rt')
    last = None # 正待处理的line
    while True:
        if not last: # 没有待处理line，则读取下一行
            for l in fp: #
                if l[0] in '>':
                    last = l[:-1]
                    break
        if not last: break
        name, seqs, last = last[1:].partition(" ")[0], [], None
        for l in fp:
            if l[0] in '>':
                last = l[:-1]
                break
            seqs.append(l[:-1])
        yield name, ''.join(seqs)

if __name__ == "__main__":
    import sys
    for name, seq in readFasta(sys.argv[1]):
        print(name, len(seq))
```


# N50
```python
def icumsum(arr):
    total = 0
    for i, x in enumerate(arr):
        total += x
        yield i, total

def N50(arr):
    """ 一组数的N50位置 """
    if not isinstance(arr, list):
        arr = list(arr)
    arr.sort()
    s = sum(arr)
    return int(arr[[i for i, c in icumsum(arr) if c >= s*0.5][0]])

print(N50(range(100)))
```