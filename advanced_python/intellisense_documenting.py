class Ticket:

    def __init__(self):
        self.id = int
        self.owner = str
        self.date_purchased = str
        self.__completed: bool = False

        return self

    def mark_completed(self):
        """Marks the ticket's completed field with True. Only use after yada yada
        >>> x = 5

        """
        self.__completed = True


ticket = Ticket()
ticket.mark_completed
