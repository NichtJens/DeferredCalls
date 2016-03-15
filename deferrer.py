#!/usr/bin/env python


class Deferrer(object):

    history = []

    def __getattr__(self, name):
        return lambda *args, **kwargs: self.remember(name, args, kwargs)

    def remember(self, name, args, kwargs):
        self.history.append((name, args, kwargs))

    def recall(self, target):
        for name, args, kwargs in self.history:
#            print self.debug(target, name, *args, **kwargs)
            f = getattr(target, name)
            f(*args, **kwargs)

    def debug(self, target, name, *args, **kwargs):
            l = [str(i) for i in args] + ["{}={}".format(k, v) for k, v in kwargs.iteritems()]
            s = "{}.{}({})".format(target.__name__, name, ", ".join(l))
            return s





if __name__ == '__main__':
    # Create a Deferrer object
    d = Deferrer()

    # Use it as if it was pyplot
    d.plot(range(10), linewidth=2, linestyle="dashed")
    d.plot(range(1, 9), range(1, 9))
    d.plot(range(2, 8))
    d.show()
    # Nothing plotted so far...

    # Actually import pyplot and recall the method calls
    import matplotlib.pyplot as plt
    d.recall(plt)



