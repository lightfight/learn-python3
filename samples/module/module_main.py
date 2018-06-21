
"""

## 关于__name__

A module’s __name__ is set equal to '__main__'
when read from standard input, a script, or from an interactive prompt.

1. module作为程序启动入口时取值"__main__"

2. 被其它module引用时取值"$module路径"，比如"samples.module.module_main"

3. "if __name__ == '__main__':"用于判断入口是不是module本身

"""


def main():
    print("we are in %s" % __name__)


if __name__ == '__main__':
    main()


