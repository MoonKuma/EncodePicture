#!/usr/bin/env python
# -*- coding:utf-8 -*-


from PIL import Image
import GenerateRandomList
import sys
import base64


class PicEncode:
    # initial picEncode, also set default encoding into utf-8
    def __init__(self, *pic_use):
        self.picName = ''
        if len(pic_use) == 0:
            self.picName = 'C:/Users/7q/PycharmProjects/untitled/venv/2a2cfc18af94c5c1bc5c0516d193668c.jpg'
        else:
            self.picName = str(pic_use[0])
        default_encoding = 'utf-8'
        if sys.getdefaultencoding() != default_encoding:
            reload(sys)
            sys.setdefaultencoding(default_encoding)

    # translate message into digital value(private)
    def __digitizeMessageDo(self, trans_message):
        message_list = list()
        for cha in trans_message:
            message_list.append(ord(cha))
        return message_list

    # reload another picture
    def reload_pic(self, pic_use):
        self.picName = str(pic_use)

    # modify each point to encrypt message in(also private)
    def __encode_pic_with_message(self, im, location_list, message):
        trans_message = base64.b64encode(message)
        message_list = self.__digitizeMessageDo(trans_message)
        if len(message_list) + 2 > len(message_list) or len(message_list) > 25599:
            print 'Failed: message is too long'
            return 0
        else:
            # add length into the first two position of message list
            # this also limit the length to maxium 25599
            length = len(trans_message)
            print 'len(messageList):', length, ',adding into message:', [int(length/100),length-100*int(length/100)], 'at local:', location_list[0],location_list[1]
            message_list = [int(length/100),length-100*int(length/100)] + message_list
            # message
            for i in range(0,len(message_list)):
                tmp_pos = message_list[i].split('_')
                value = message_list[i]
                pix = list(im.getpixel((int(tmp_pos[0]), int(tmp_pos[1]))))
                pix[int(tmp_pos[2])] = value
                im.putpixel((int(tmp_pos[0]), int(tmp_pos[1])), tuple(pix))
            print 'Succeed in encrypting message'
            return 1

    # encode message into pics, a message(str) and a seed(int) num is required, seed num should not smaller than 1000
    def encode_pic(self, message, seed, *data_legth):
        seed = int(seed)
        im = Image.open(self.picName)
        img_size = im.size
        scale_triple = [img_size[0], img_size[1],3]
        seed_triple = [seed%scale_triple[0]+1, seed%scale_triple[1]+1, seed%scale_triple[2]+1]
        random_list = GenerateRandomList.GenerateRandomList()
        random_list.set_scale(scale_triple)
        random_list.set_seed(seed_triple)
        if len(data_legth) == 1 and data_legth[0] < 25599:
            random_list.set_data_length(data_legth[0])
        random_list.reset_data()
        location_list = random_list.load_data()
        if self.__encode_pic_with_message(im, location_list, message):
            save_name = self.picName.split('.')[0] + str(seed) + '_new2.png'
            im.save(save_name, "PNG")
            # caution only .png is safe here to main evey pixel change

    # test encoding
    def execute_test(self):
        message = 'magnet:?xt=urn:btih:WRBT4CJREXCOVFPM6FZ7NFGERKCWSEO6&dn=%e7%9e%92%e5%a4%a9%e8%bf%87%e6%b5%b7%ef%bc%9a%e7%be%8e%e4%ba%ba%e8%ae%a1%2e1080p%2eBD%e4%b8%ad%e8%8b%b1%e5%8f%8c%e5%ad%97%5b%e6%9c%80%e6%96%b0%e7%94%b5%e5%bd%b1www%2e66ys%2etv%5d%2emp4&tr=udp%3a%2f%2f9%2erarbg%2eto%3a2710%2fannounce&tr=udp%3a%2f%2f9%2erarbg%2eme%3a2710%2fannounce&tr=http%3a%2f%2ftr%2ecili001%2ecom%3a8070%2fannounce&tr=http%3a%2f%2ftracker%2etrackerfix%2ecom%3a80%2fannounce&tr=udp%3a%2f%2fopen%2edemonii%2ecom%3a1337&tr=udp%3a%2f%2ftracker%2eopentrackr%2eorg%3a1337%2fannounce&tr=udp%3a%2f%2fp4p%2earenabg%2ecom%3a1337'
        self.encode_pic(message,1447,10000)
        # reload(PicEncode)
        # test1 = PicEncode.PicEncode()
        # test1.executeTest()






