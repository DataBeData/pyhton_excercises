def f(*args, **kwargs):  # args are POSITIONAL an kwargs are NAMED and come second???
    print("Named:", kwargs)
    print("Positional:", args)


f(100,50,25)
f(galleons=100, sickles=50, knuts=25)