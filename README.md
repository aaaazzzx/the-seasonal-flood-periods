# the-seasonal-flood-periods
分期洪水方法多样，本次研究分为预处理部分及划分部分
预处理部分是对水文时间序列进行处理，以适用于不同的分期方法

  1.目标
  
    a.构造序列矩阵，n×m，本次研究以旬（候）为一个时段，则一年有36个时段，n=36；
    b.m为时段参数，常用指标：（时段内）多年平均降雨量、多年平均最大3d雨量、大雨天数（>25mm）、多年平均Cv值、多年最大1d降雨量；
    
    
    
  2.方法
  
    matlab用于前处理，求出参数指标
    python用于分期方法
    
  3.进展
  
    前处理完成
    fisher最优分割法ing：以月为单位，前后相连方式下最优2分为4-7，前后不连最优单分为6.效果不理想
    以旬为单位，已完成第一次划分，目前已完成划分主程序主要部分，正在检测可靠性
