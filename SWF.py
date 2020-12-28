# -*- coding: utf-8 -*-

import random

class Bin:
    def __init__(self):
        self.height_index=0;
        self.shelf_list = [];
        self.color_dictionary=[];
        
class Shelf:
    def __init__(self, shelf_height):
        self.shelf_height=shelf_height;
        self.width_index=0;
        self.item_list = []


class Item:
    def __init__(self, size, color):
        self.size = size
        self.color = color
    def __str__(self):
        return "(Size: %d, Color: %d) " % (self.size,self.color)


bins = []
area_opt=0;
best_shelf=-1;
best_width_index=0;
best_bin=-1;


def addItemToBin(new_item):
    best_shelf=-1;
    best_width_index=0;
    if new_item.size > 10:
        print("Size should be less than 10.")
        return
    if len(bins) == 0:
        #print("No Shelf found")
        bins.append(Bin())
        bin_index=len(bins)-1;
        bin_used=bins[bin_index];
        shelf_used=Shelf(new_item.size);
        shelf_used.width_index=new_item.size;
        shelf_used.item_list.append(new_item);
        bin_used.shelf_list.append(shelf_used);
        bin_used.height_index=bin_used.height_index+shelf_used.shelf_height;
        bin_used.color_dictionary.append(new_item.color);
        return
    else:
        for bin_index, ebin in enumerate(bins, start=0):
            if ebin.color_dictionary.count(new_item.color) == 0:
                for index,eshelf in enumerate(ebin.shelf_list, start=0):
                    if(eshelf.shelf_height >= new_item.size):
                        if(10 - eshelf.width_index) >= new_item.size:
                            if(best_width_index > eshelf.width_index):
                                best_width_index = eshelf.width_index;
                                best_shelf=index;
                                best_bin=bin_index
                        else:
                            continue;
                        
                        
        if(best_shelf != -1):
            ebin=bins[best_bin]; 
            eshelf=ebin.shelf_list[best_shelf];
            eshelf.width_index = eshelf.width_index + new_item.size
            eshelf.item_list.append(new_item);
            ebin.color_dictionary.append(new_item.color)
            return;
            
        ebin=bins[len(bins)-1];    
        if(10 - ebin.height_index >= new_item.size):
            shelf_used=Shelf(new_item.size);
            shelf_used.width_index=new_item.size;
            shelf_used.item_list.append(new_item);
            ebin.shelf_list.append(shelf_used);
            ebin.height_index=ebin.height_index+shelf_used.shelf_height;
            ebin.color_dictionary.append(new_item.color);
            return
        #print("No Shelf found")
        
        bins.append(Bin())
        bin_index=len(bins)-1;
        bin_used=bins[bin_index];
        shelf_used=Shelf(new_item.size);
        shelf_used.width_index=new_item.size;
        shelf_used.item_list.append(new_item);
        bin_used.shelf_list.append(shelf_used);
        bin_used.height_index=bin_used.height_index+shelf_used.shelf_height;
        bin_used.color_dictionary.append(new_item.color);
        return


try:
    isValid = True
    for x in range(10000):
        item_size = random.randint(1, 10)
        item_color = random.randint(1, 9)
        try:
            addItemToBin(Item(int(item_size), int(item_color)))
            area_opt += (int(item_size)*int(item_size));
        except Exception as e:
            print(e)
            isValid = False
            print("An exception occurred: Incorrect item.")

    total_height=0;
    for  index,ab in enumerate(bins, start=1):
        print("Bin ",str(index))
        #print("Height Index: ",ab.height_index);
        total_height=total_height+ab.height_index;
        for index_shelf,shelves in enumerate(ab.shelf_list, start=1):
            print("Shelf ",str(index_shelf), " Height: ",shelves.shelf_height)
            for item in shelves.item_list:
                print(item);

    
    print("Area(ALG): ",str(total_height*10));
    print("Area(OPT): ",str(area_opt));
    print("CR: ", str((total_height*10)/area_opt))
except:
    print("An exception occurred")