#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
# based on LCG random


class GenerateRandomList:

    def __init__(self):
        self.seedNum = [437, 211, 1]
        self.scale = [1366, 768, 3]  # x-posi,y-posi,rgb?
        self.dataLength = [1000]
        self.dataList = list()
        self.scaleComputeRefer = [(1 << 31) - 1]
        self.a = 29
        self.b = 23

    def get_time_str(self, compute_time):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(compute_time))

    def set_seed(self, new_seed_list):
        self.seedNum[0] = new_seed_list[0]
        self.seedNum[1] = new_seed_list[1]
        self.seedNum[2] = new_seed_list[2]

    def set_scale(self, new_scale_list):
        self. scale[0] = new_scale_list[0]
        self.scale[1] = new_scale_list[1]
        self.scale[2] = new_scale_list[2]

    def next_seed(self, *show):
        self.seedNum[0] = (self.a * self.seedNum[0] + self.b) % self.scaleComputeRefer[0]
        self.seedNum[1] = (self.a * self.seedNum[1] + self.b) % self.scaleComputeRefer[0]
        self.seedNum[2] = (self.a * self.seedNum[2] + self.b) % self.scaleComputeRefer[0]
        if len(show) > 0:
            self.get_seed()

    def get_seed(self):
        print 'current seed:', str(self.seedNum[0]%self.scale[0]), '_',  str(self.seedNum[1]%self.scale[1]), '_', str(self.seedNum[2]%self.scale[2])

    def reset_data(self):
        self.dataList = list()

    def set_data_length(self, new_length):
        self.dataLength[0] = new_length

    def load_data(self, *show):
        start_time = time.time()
        print 'start generating data at:', self.get_time_str(start_time)
        print 'data scale:', self.scale, ',seed:', self.seedNum, 'lenght:', self.dataLength[0]
        for i in range(0, 100000):
            self.next_seed()
            key = str(self.seedNum[0] % self.scale[0]) + '_' + str(self.seedNum[1] % self.scale[1]) + '_' + str(self.seedNum[2] % self.scale[2])
            if key not in self.dataList:
                self.dataList.append(key)
            if len(self.dataList) >= self.dataLength[0]:
                break
        if len(show) > 0:
            print 'dataList:', self.dataList
        end_time = time.time()
        time_dif = end_time-start_time
        print 'end generating data at:', self.get_time_str(end_time), ',with costing:', str(time_dif), 'secs'
        return self.dataList






