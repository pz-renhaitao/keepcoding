# 程序目的：演示抽象工场模式
# 程序实现思路：按照对抽象工厂模式的原有知识理解写得这段代码
# 收益：熟悉python3类的写法，熟练__main__入口写法
# 问题：抽象工厂模式的理解不到位、Python脚本写得不熟练、SVG不理解、程序基本没有设计
# 其他：2018.3.15 于东恒家中 by RENHAITAO


# coding=utf-8

class DiagramCreatorFactory(object):
    def __init__(self, cls_type):
        self.type = cls_type

    def generate_creator(self):
        if (self.type == 'text'):
            newCreator = TextDCreator()
        elif (self.type == 'SVG'):
            newCreator = SVGDCreator()

        return newCreator


class TextDCreator(object):
    def print_diagram(self):
        print("+--------------------------+\n")
        print("|  +--------------------+  |\n")
        print("|  |%%%%%%%%%%%%%%%%%%%%|  |\n")
        print("|  |%%Abstract Factory%%|  |\n")
        print("|  |%%%%%%%%%%%%%%%%%%%%|  |\n")
        print("|  +--------------------+  |\n")
        print("+--------------------------+\n")


class SVGDCreator(object):
    def print_diagram(self):
        print("this is a SVG")


def main():
    td = DiagramCreatorFactory('text').generate_creator()
    td.print_diagram()

    td = DiagramCreatorFactory('SVG').generate_creator()
    td.print_diagram()


if __name__ == '__main__':
    main()
    print("helloworld")



