# world = []
#
#
# def add_obj(o):
#     world.append(o)
#
# def remove_obj(o):
#     world.remove(o)
#     del o

objs = [[], [], []]


def add_obj(o, depth): # 하나 추가
    objs[depth].append(o)

def add_objs(ol, depth): # 여러개 추가
    objs[depth] += ol

def remove_obj(o):
    for layer in objs:
        if o in layer:
            layer.remove(o)
            del o
            return
    raise ValueError('Trying destroy non existing obj')

def all_objs():
    for layer in objs:
        for o in layer:
            yield o # 일드가 들어가는 함수는 제너레이터 취급, 하나씩 던져줌


def clear():
    for o in all_objs():
        del o
    for layer in objs:
        layer.clear()