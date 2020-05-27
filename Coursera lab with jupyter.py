class Elevator:
    def __init__(self, bottom, top, current):
        self.bottom = bottom
        self.top = top
        self.current = current
        """Initializes the Elevator instance."""
        pass

    def up(self):

        if self.current >= self.top:
            self.current = self.top
        else:
            self.current += 1
        """Makes the elevator go up one floor."""
        pass
    def down(self):
        if self.current <= self.bottom:
            self.bottom = self.bottom
        else:
            self.current -=1
        """Makes the elevator go down one floor."""
        pass
    def go_to(self, floor):
        self.current = floor
        """Makes the elevator go to the specific floor."""
        pass
    def __str__(self):
        return "Current floor {}".format(self.current)

elevator = Elevator(-1, 10, 0)

elevator.up()
elevator.current #should output 1

elevator.down()
elevator.current #should output 0

elevator.go_to(10)
elevator.current #should output 10

# Go to the top floor. Try to go up, it should stay. Then go down.
elevator.go_to(10)
elevator.up()
elevator.down()
print(elevator.current) # should be 9
# Go to the bottom floor. Try to go down, it should stay. Then go up.
elevator.go_to(-1)
elevator.down()
elevator.down()
elevator.up()
elevator.up()
print(elevator.current) # should be 1

elevator.go_to(5)
print(elevator)
