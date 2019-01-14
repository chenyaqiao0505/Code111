# def mydecoretor(function):
#     def wrapped(*args,**kwargs):
#         #在调用函数前，做点什么
#         result = function(*args,**kwargs)
#         #函数调用之后，做点什么
#         #并返回结果
#         return result
#     return function

# class DecoratorAsClass:
#     def __init__(self, function):
#         self.function = function
#
#     def __call__(self, *args, **kwargs):
#         #在调用原始函数前，做点什么
#         result = self.function(*args, **kwargs)
#         #在调用原始函数后，做点什么
#         #并返回结果
#         return result

def repeat(number = 3):
    '''多次执行装饰函数。

    返回最后一次原始函数调用的值作为结果
    :param number:重复次数，默认为3
    '''
    def actual_decorator(function):
        def wrapped(*args,**kwargs):
            result = None
            for _ in range(number):
                result = function(*args,**kwargs)
            return result
        return wrapped
    return actual_decorator

@repeat(2)
def bbb():
    print(11)
bbb()
