import pandas
from pyecharts import Bar3D
import numpy


if __name__ == '__main__':
    data = pandas.DataFrame(pandas.read_excel('outputD_xun_2k.xlsx'))
    print(data.shape)
    data = data.replace(0,numpy.nan)
    #print(datamin)
    #print(data.min())
    #print(data.ix[3,2])
    data_out = list()     #建立空的list，用来保存元素
    data_min = data.min(axis=1)
    data_max = data.max(axis=1)
    #print(data_min)
    #print(data_min.min())
    data_max = data.max(axis=1)
    data = data.replace(numpy.nan,0 )
    for i in range(36):
        for j in range(36):
            if data.iloc[i,j]>0 :
                data_out.append([i,j,(1-(data.iloc[i,j]-data_min.min())/(data_max.max()-data_min.min()))])    #(1-(data.iloc[i,j]-data_min.min())/(data_max.max()-data_min.min()))
            # print(i,j,(1-(data.iloc[i,j]-data_min.min())/(data_max.max()-data_min.min())))
    #[d[1], d[0], d[2]] for d in data:

    #print(data[i].min())

    print(data_out)
    x_axis = list()
    y_axis = list()
    for i in range(36):
        x_axis.append(i)
        y_axis.append(i)

    bar3d = Bar3D("3D 柱状图示例", width=1200, height=600)
    '''
    x_axis = [
        "12a", "1a", "2a", "3a", "4a", "5a", "6a", "7a", "8a", "9a", "10a", "11a",
        "12p", "1p", "2p", "3p", "4p", "5p", "6p", "7p", "8p", "9p", "10p", "11p"
    ]
    y_axis = [
        "Saturday", "Friday", "Thursday", "Wednesday", "Tuesday", "Monday", "Sunday"
    ]
    
    data1 = [
        [0, 0, 5], [0, 1, 1], [0, 2, 0], [0, 3, 0], [0, 4, 0], [0, 5, 0],
        [0, 6, 0], [0, 7, 0], [0, 8, 0], [0, 9, 0], [0, 10, 0], [0, 11, 2],
        [0, 12, 4], [0, 13, 1], [0, 14, 1], [0, 15, 3], [0, 16, 4], [0, 17, 6],
        [0, 18, 4], [0, 19, 4], [0, 20, 3], [0, 21, 3], [0, 22, 2], [0, 23, 5],
        [1, 0, 7], [1, 1, 0], [1, 2, 0], [1, 3, 0], [1, 4, 0], [1, 5, 0],
        [1, 6, 0], [1, 7, 0], [1, 8, 0], [1, 9, 0], [1, 10, 5], [1, 11, 2],
        [1, 12, 2], [1, 13, 6], [1, 14, 9], [1, 15, 11], [1, 16, 6], [1, 17, 7],
        [1, 18, 8], [1, 19, 12], [1, 20, 5], [1, 21, 5], [1, 22, 7], [1, 23, 2],
        [2, 0, 1], [2, 1, 1], [2, 2, 0], [2, 3, 0], [2, 4, 0], [2, 5, 0],
        [2, 6, 0], [2, 7, 0], [2, 8, 0], [2, 9, 0], [2, 10, 3], [2, 11, 2],
        [2, 12, 1], [2, 13, 9], [2, 14, 8], [2, 15, 10], [2, 16, 6], [2, 17, 5],
        
        [2, 18, 5], [2, 19, 5], [2, 20, 7], [2, 21, 4], [2, 22, 2], [2, 23, 4],
        [3, 0, 7], [3, 1, 3], [3, 2, 0], [3, 3, 0], [3, 4, 0], [3, 5, 0],
        [3, 6, 0], [3, 7, 0], [3, 8, 1], [3, 9, 0], [3, 10, 5], [3, 11, 4],
        [3, 12, 7], [3, 13, 14], [3, 14, 13], [3, 15, 12], [3, 16, 9], [3, 17, 5],
        [3, 18, 5], [3, 19, 10], [3, 20, 6], [3, 21, 4], [3, 22, 4], [3, 23, 1],
        [4, 0, 1], [4, 1, 3], [4, 2, 0], [4, 3, 0], [4, 4, 0], [4, 5, 1],
        [4, 6, 0], [4, 7, 0], [4, 8, 0], [4, 9, 2], [4, 10, 4], [4, 11, 4],
        [4, 12, 2], [4, 13, 4], [4, 14, 4], [4, 15, 14], [4, 16, 12], [4, 17, 1],
        [4, 18, 8], [4, 19, 5], [4, 20, 3], [4, 21, 7], [4, 22, 3], [4, 23, 0],
        [5, 0, 2], [5, 1, 1], [5, 2, 0], [5, 3, 3], [5, 4, 0], [5, 5, 0],
        [5, 6, 0], [5, 7, 0], [5, 8, 2], [5, 9, 0], [5, 10, 4], [5, 11, 1],
        [5, 12, 5], [5, 13, 10], [5, 14, 5], [5, 15, 7], [5, 16, 11], [5, 17, 6],
        [5, 18, 0], [5, 19, 5], [5, 20, 3], [5, 21, 4], [5, 22, 2], [5, 23, 0],
        [6, 0, 1], [6, 1, 0], [6, 2, 0], [6, 3, 0], [6, 4, 0], [6, 5, 0],
        [6, 6, 0], [6, 7, 0], [6, 8, 0], [6, 9, 0], [6, 10, 1], [6, 11, 0],
        [6, 12, 2], [6, 13, 1], [6, 14, 3], [6, 15, 4], [6, 16, 0], [6, 17, 0],
        [6, 18, 0], [6, 19, 0], [6, 20, 1], [6, 21, 2], [6, 22, 2], [6, 23, 6]
    ]
    '''
    range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
                   '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']

    bar3d.add(
        "",
        x_axis,
        y_axis,
        [[d[1], d[0], d[2]] for d in data_out],
        is_visualmap=True,
        visual_range=[0, 1],  # visual_range -> list    默认 -> [0, 100]    指定组件的允许的最小值与最大值。
        visual_range_color=range_color,
        grid3d_width=200,  # grid3d_width -> int   默认 -> 100 三维笛卡尔坐标系组件在三维场景中的宽度
        grid3d_depth=200,
    )
    bar3d.render()

    xun2k = Bar3D("3D 柱状图示例", width=1200, height=600)
    xun2k.add(
        "",
        x_axis,
        y_axis,
        [[d[1], d[0], d[2]] for d in data_out],
        is_visualmap=True,
        visual_range=[0, 1],
        visual_range_color=range_color,
        grid3d_width=200,
        grid3d_depth=200,
        is_grid3d_rotate=True,
    )
    xun2k.render()