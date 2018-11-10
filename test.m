a = pwd ;
b = xlsread ('C:\Users\LHX\the-seasonal-flood-periods\data\source\毛俊日流量表1973-2003.xls','1973','B3:M33');
d = [a,'\data\source\毛俊日流量表1973-2003.xls'];
c = xlsread ([a,'\data\source\毛俊日流量表1973-2003.xls'],'1973','B3:M33');