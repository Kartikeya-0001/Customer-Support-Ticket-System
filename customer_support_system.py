class Ticket:
    def __init__(self, tid, name, issue, priority):
        self.tid = tid
        self.name = name
        self.issue = issue
        self.priority = priority
        self.next = None

class TicketLinkedList:
    def __init__(self):
        self.head = None

    def insertTicket(self, tid, name, issue, priority):
        new_ticket = Ticket(tid, name, issue, priority)
        new_ticket.next = self.head
        self.head = new_ticket
        print(f"Ticket {tid} added for {name}.")

    def deleteTicket(self, tid):
        temp = self.head
        prev = None
        while temp:
            if temp.tid == tid:
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                print(f"Ticket {tid} deleted.")
                return
            prev = temp
            temp = temp.next
        print("Ticket not found!")

    def retrieveTicket(self, tid):
        temp = self.head
        while temp:
            if temp.tid == tid:
                print(f"Ticket Found: ID={temp.tid}, Name={temp.name}, Issue={temp.issue}, Priority={temp.priority}")
                return
            temp = temp.next
        print("Ticket not found!")

class UndoStack:
    def __init__(self):
        self.stack = []

    def push(self, action):
        self.stack.append(action)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return None

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, tid, priority):
        self.queue.append((priority, tid))
        self.queue.sort(reverse=True)
        print(f"Ticket {tid} added to priority queue.")

    def dequeue(self):
        if self.queue:
            p, tid = self.queue.pop(0)
            print(f"Processing urgent ticket {tid} (Priority {p}).")
        else:
            print("No urgent tickets!")

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = []
        self.front = 0
        self.rear = 0

    def enqueue(self, ticket):
        if len(self.queue) < self.size:
            self.queue.append(ticket)
            print(f"Ticket {ticket} added for round-robin processing.")
        else:
            print("Queue full!")

    def dequeue(self):
        if self.queue:
            ticket = self.queue.pop(0)
            self.queue.append(ticket)
            print(f"Ticket {ticket} processed and moved to end (round-robin).")
        else:
            print("No tickets to process!")

# Polynomial Linked List comparison (for billing)
def compareBillingHistory(p1, p2):
    if p1 == p2:
        print("Billing records match.")
    else:
        print("Billing records differ.")

tickets = TicketLinkedList()
undo = UndoStack()
priority = PriorityQueue()
round_robin = CircularQueue(3)

tickets.insertTicket(1, "Kartikeya", "Login Issue", 2)
tickets.insertTicket(2, "Nikita", "Payment Failed", 1)
undo.push(("insert", 2))
tickets.retrieveTicket(2)
tickets.deleteTicket(1)

priority.enqueue(2, 5)
priority.enqueue(3, 3)
priority.dequeue()

round_robin.enqueue("Ticket1")
round_robin.enqueue("Ticket2")
round_robin.dequeue()

compareBillingHistory([100, 200], [100, 200])
