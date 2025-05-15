from package.constants import Constants


class Calculations:

    name = "circle"  # Shape name

    def area(radius):
        """
        This is the default area implementation meant for circle.
        """
        return Constants.pi * radius ** 2
    
    def volume():
        """
        This is the placeholder for the volume implementation.
        Since volume is not defined for circle, this method is not implemented.
        """
        raise NotImplementedError("This method should be overridden in subclasses")