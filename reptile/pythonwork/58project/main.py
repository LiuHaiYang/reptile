from multiprocessing import  Pool
from channel_extract import channel_list
from page_parsing import get_links_from
from page_parsing import  get_item_info


def get_alt_links_from(channel):
    for run in range(1,5):
        get_links_from(channel,run)


if __name__ =='__main__':
    pool = Pool()
    #pool.map(get_all_links_from,channel_list.split())
    for i in get_item_info(pool.map(get_alt_links_from,channel_list.split())):
        print(i)



