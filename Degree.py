#!/usr/bin/env python
# coding=utf-8

import networkx as nx
import matplotlib.pyplot as plt
#import graphviz
from Queue import PriorityQueue
import random
import Evaluation


class Degree_Heuristic():
    def __init__(self, graph_path):
        self.graph, self.num_node, self.num_edge = self.load_graph(graph_path)

    def load_graph(self, graph_path):
        G = nx.Graph()
        with open(graph_path,'r') as f:
            for i, line in enumerate(f):
                if i == 0:
                    num_node, num_edge = line.strip().split('\t')
                    continue
                node1,node2=line.strip().split('\t')
                G.add_edge(int(node1),int(node2))
        return G, int(num_node), int(num_edge)


    def seed_selection(self,k):
        print "Finding top",k,"nodes"
        print "No.\tNode_id\tDegree\tTimes(s)"
        pairs=dict()
        seed_set=[]
        for node in self.graph.nodes():
            degree = self.graph.degree(node)
            pairs[node]=degree
            if len(pairs)>k:
                pairs=dict(sorted(pairs.items(),key=lambda item:item[1],reverse=False)[1:])

        for i in xrange(0,k):
            best_pair = sorted(pairs.items(),key=lambda item:item[1],reverse=True)[0]
            pairs=dict(sorted(pairs.items(),key=lambda item:item[1],reverse=True)[1:])
            seed_set.append(best_pair[0])
            print i+1,"\t",best_pair[0],"\t",best_pair[1],"\t",0
        return seed_set


    def draw_graph(self):
        nx.draw(self.graph)
        plt.show()

if __name__ == '__main__':
    DH = Degree_Heuristic('NetHEHT.txt')
    seeds=DH.seed_selection(50)
    # inf=Evaluation.monte_carlo(DH,list(seeds),50,10)
    # print "Total influence:",inf
    a=[1,5,10,15,20,25,30,35,40,45,50]
    for num in a:
        inf=Evaluation.monte_carlo(DH,seeds,num,10000)
        print "seed number:",num,"Total influence:",inf