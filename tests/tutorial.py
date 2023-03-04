# -*- coding:utf-8 -*-
##############################################################
# Created Date: Friday, January 13th 2023
# Contact Info: luoxiangyong01@gmail.com
# Author/Copyright: Mr. Xiangyong Luo
##############################################################


import path4gmns as pg
import os

path = "../data/ASU"

os.chdir(path)

# Generate network object
network = pg.read_network()

# 3.1 Get the shortest path between two nodes
print('\nshortest path (node id) from node 1 to node 2, '
      +network.find_shortest_path(1, 2))
print('\nshortest path (link id) from node 1 to node 2, '
      +network.find_shortest_path(1, 2, seq_type='link'))

