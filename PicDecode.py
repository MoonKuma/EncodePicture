#!/usr/bin/env python
# -*- coding:utf-8 -*-


from PIL import Image
import GenerateRandomList
import sys
import base64


class PicDecode:
    # initial PicDecode, instantiate this class to decode message from pictures
    def __init__(self):
        self.pic_name = ''
        self.data_length = 1000
        default_encoding = 'utf-8'
        if sys.getdefaultencoding() != default_encoding:
            reload(sys)
            sys.setdefaultencoding(default_encoding)
    # recover message from digital value(this is private)

    def __digitize_message_recover(self,trans_message_list):
        trans_message = ''
        for num in trans_message_list:
            trans_message = trans_message + chr(num)
        return trans_message

    def __value_of_location(self,im,location_str):
        tmp_local = location_str.split('_')
        tmp_pix = list(im.getpixel((int(tmp_local[0]), int(tmp_local[1]))))
        value = tmp_pix[int(tmp_local[2])]
        return value

    # load/reset Pics name

    def load_pic(self,pic_use):
        self.pic_name = str(pic_use)

    def set_data_length(self,length):
        self.data_length = length

    # decode pics

    def __decode_pic_with_local(self, im, location_list, message_container):
        value100 = self.__value_of_location(im,location_list[0])
        value1 = self.__value_of_location(im,location_list[1])
        length = value100*100 + value1
        print 'value100:', value100, ',value1:', value1, ',at local:', location_list[0], location_list[1]
        if length + 2 > self.data_length:
            print 'Failed : data_length is too short. Need to reset data_length to at least:', str(length+2)
            return 0
        else:
            message_list = list()
            for i in range(0,length):
                value = self.__value_of_location(im,location_list[i+2])
                message_list.append(value)
            base64_message = self.__digitize_message_recover(message_list)
            message = base64.b64decode(base64_message)
            message_container[0] = message
            return 1

    def decode_pic(self,seed,pic_use):
        self.load_pic(pic_use)
        seed = int(seed)
        im = Image.open(self.pic_name)
        img_size = im.size
        scale_triple = [img_size[0], img_size[1], 3]
        seed_triple = [seed % scale_triple[0] + 1, seed % scale_triple[1] + 1, seed % scale_triple[2] + 1]
        random_list = GenerateRandomList.GenerateRandomList()
        random_list.set_scale(scale_triple)
        random_list.set_seed(seed_triple)
        random_list.set_data_length(self.data_length)
        random_list.reset_data()
        location_list = random_list.load_data()
        message_container = ['']
        if self.__decode_pic_with_local(im, location_list, message_container):
            print message_container[0]
            return message_container[0]

    def execute_test(self):
        pic_name = 'C:/Users/7q/PycharmProjects/untitled/venv/2a2cfc18af94c5c1bc5c0516d193668c1447_new2.png'
        self.set_data_length(10000)
        self.decode_pic(1447, pic_name)

    # import PicDecode
    # reload(PicDecode)
    # test2 = PicDecode.PicDecode()
    # test2.execute_test()


