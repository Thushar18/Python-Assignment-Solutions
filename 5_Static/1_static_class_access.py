class Cricketer:
    team_name = "Royal Challengers Bengaluru"

    def __init__(self,name,jersey_no,role):
        self.name = name
        self.jersey_no = jersey_no
        self.role = role

    def display(self):
        print("Name:",self.name)
        print("Jersey No:",self.jersey_no)
        print("Role:",self.role)
        print("Team:",Cricketer.team_name)

c1 = Cricketer("Virat Kohli",18,"Right-handed Batsman")
c2 = Cricketer("Bhuvaneshwar Kumar",15,"Right-arm Medium-Fast Bowler")
c3 = Cricketer("Rajat Patidar",97,"Right-handed Batsman")

c1.display()
c2.display()
c3.display()

print("Accessing Static Variables directly through class:")
print("Team Name:",Cricketer.team_name)