class Container:
    @classmethod
    def show_details(cls):
        print(f'Running from the {cls.__name__} class.')

container = Container()
container.show_details()