# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 14:50:42 2014

@author: aitor
"""

import csv
import networkx as nx

G = nx.DiGraph()

with open('./flights/citiesToCities.csv', 'rb') as csvfile:
    flightreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for i, row in enumerate(flightreader):
        if i==0:
            continue
        from_city = row[0]
        from_lon = float(row[1])
        from_lat= float(row[2]) * -1
        to_city = row[4]
        to_lon = float(row[5])
        to_lat= float(row[6]) * -1
        routes = float(row[8])
        
        if not G.has_node(from_city):
            G.add_node(from_city, lon = from_lon, lat = from_lat)       
        if not G.has_node(to_city):
            G.add_node(to_city, lon = to_lon, lat = to_lat)    
            
        G.add_edge(from_city, to_city, weight=routes)

        
nx.write_gexf(G, './data/city2city.gexf')
print 'done'
        
