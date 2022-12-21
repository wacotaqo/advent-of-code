# This program is an exercise/challenge from the 2022 advent of code competition
#
#
import os
import re
from collections import deque
from functools import reduce
from collections import defaultdict

filename = "day19_input.txt"
filename = "day19_input_test.txt"

DEBUG = 1
def debug(msg):
    if DEBUG:
        print(msg)

try:
    fh = open(os.path.join(os.getcwd(), filename), "r")
except FileNotFoundError:
    fh = open(os.path.join(os.getcwd(),"2022\\python\\day19" ,filename), "r")
data = fh.read().strip()
fh.close()
lines = data.splitlines()

blueprints = {}
RES_ORE = 1
RES_CLAY = 2
RES_OBSIDIAN = 3
RES_GEODE = 4
RESOURCES = {
    'ore': RES_ORE,
    'clay': RES_CLAY,
    'obsidian': RES_OBSIDIAN, 
    'geode': RES_GEODE
}

def get_cost(strAmt, strResource):
    amt = int(strAmt)
    res = RESOURCES[strResource]
    return (amt, res)

def get_robcosts(costs): # Redundent, remove later
    rc = []
    for (amt, res) in costs:
        rc.append((amt, res))
    return rc 
    
for line in lines:
    print(line)
    x = re.match('Blueprint (\d+): .+(ore) robot.* (\d+) (ore)\. .+ (clay) robot .* (\d+) (ore)\. .* (obsidian) robot .* (\d+) (ore) and (\d+) (clay)\. .*(geode) robot.* (\d+) (ore) and (\d+) (obsidian)', line)
    matches = x.groups()
    print(matches)
    blueprint = int(matches[0])
    resources = {
        RES_ORE: 0,
        RES_CLAY: 0,
        RES_OBSIDIAN: 0,
        RES_GEODE: 0,
    }
    robcosts = []
    robcosts.append((RESOURCES[matches[1]], get_robcosts([get_cost(matches[2], matches[3])])))
    robcosts.append((RESOURCES[matches[4]], get_robcosts([get_cost(matches[5], matches[6])])))
    robcosts.append((RESOURCES[matches[7]], get_robcosts([get_cost(matches[8], matches[9]), get_cost(matches[10], matches[11])])))
    robcosts.append((RESOURCES[matches[12]], get_robcosts([get_cost(matches[13], matches[14]), get_cost(matches[15], matches[16])])))

    blueprints[blueprint] = {
        'robcosts': robcosts,
        'resources': resources,
        'robots': defaultdict(int, {RES_ORE:1})
    }        
    
for b in blueprints:
    print("%s = %s" % (b, blueprints[b]))
#    (blueprint, ore_rob_ore_cost, clay_rob_ore_cost, obs_rob_ore_cost, obs_rob_clay_cost, geo_rob_ore_cost, geo_rob_obs_cost) = [int(m) for m in x.groups()]
#    print(blueprint, ore_rob_ore_cost, clay_rob_ore_cost, obs_rob_ore_cost, obs_rob_clay_cost, geo_rob_ore_cost, geo_rob_obs_cost)

t = 0

print("")
while t < 24:
    t += 1
    if 1:
        b = 1#for b in blueprints.keys():
        # start making robots if possible
        making_robots = []
        robcosts = blueprints[b]['robcosts']
        resources = blueprints[b]['resources']
        robots = blueprints[b]['robots']
        for robcost in robcosts:
            (robtype, resources_needed) = robcost
            if len(resources_needed) == len([res for (amt, res) in resources_needed if amt <= resources[res]]):
                making_robots.append(robtype)
                for (amt, res) in resources_needed:
                    resources[res] -= amt

        # collect resources
        for (res, cnt) in robots.items():
            resources[res] += cnt
        # complete making robots
        for robtype in making_robots:
            robots[robtype] += 1
        
        blueprints[b] = {
            'robcosts': robcosts,
            'resources': resources,
            'robots': robots
        }     
        
        print(t, b, blueprints[b])
    
    
    