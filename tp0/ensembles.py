robots_exploration = {"R2", "R5", "R7"}
robots_transport = {"R5", "R9", "R7", "R3"}

def robots_double_mission():
    double_mission=set()
    double_mission= robots_exploration & robots_transport
    return double_mission


    
double_mission = robots_double_mission() 
    
assert double_mission == {"R5", "R7"}

def ajouter_robot_mission(robots, robot):
    
    nouvel_ensemble = robots.copy()
    nouvel_ensemble.add(robot)
    
    return nouvel_ensemble


def retirer_robot_mission(robots, robot):
    
    nouvel_ensemble = robots.copy()
    nouvel_ensemble.remove(robot)
    
    return nouvel_ensemble


ajout = ajouter_robot_mission(robots_exploration, "R8")
retrait = retirer_robot_mission(robots_transport, "R9")


assert ajout == {"R2", "R5", "R7", "R8"}

assert retrait == {"R3", "R5", "R7"}


assert robots_transport == {"R5", "R9", "R7", "R3"}

