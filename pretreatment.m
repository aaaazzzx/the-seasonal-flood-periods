% 读取日流量数据
file = pwd ;
% num = zeros(31*3,12);
% shangxunpjun = zeros(1,12);
% zhongxunpjun = zeros(1,12);
% xiaxunpjun = zeros(1,12);

% for i = 1973:2003
%     
%     num((i-1972)*3-2,:)=xlsread('I:/毛俊水库水文工作/分期洪水/毛俊日流量表1973-2003.xls',num2str(i),'B36:M36'); 
%     num((i-1972)*3-1,:)=xlsread('I:/毛俊水库水文工作/分期洪水/毛俊日流量表1973-2003.xls',num2str(i),'B37:M37'); 
%     num((i-1972)*3,:)=xlsread('I:/毛俊水库水文工作/分期洪水/毛俊日流量表1973-2003.xls',num2str(i),'B38:M38'); 
%      shangxunpjun = num((i-1972)*3-2,:)+ shangxunpjun ;   %上旬平均
%      zhongxunpjun = num((i-1972)*3-1,:)+ zhongxunpjun ;   %上旬平均
%      xiaxunpjun = num((i-1972)*3,:)+ xiaxunpjun ;   %上旬平均
%     
%     % xlswrite('D:/Desktop/分期洪水/毛俊日流量表1973-2003.xls','sheet1','D')
% end


% % xlswrite('I:/毛俊水库水文工作/分期洪水/毛俊旬平均流量表1973-2003.xls',num,'sheet1','C2')
% % xlswrite('I:/毛俊水库水文工作/分期洪水/毛俊旬平均流量表1973-2003.xls',shangxunpjun/31,'sheet1','C95')
% % xlswrite('I:/毛俊水库水文工作/分期洪水/毛俊旬平均流量表1973-2003.xls',zhongxunpjun/31,'sheet1','C96')
% % xlswrite('I:/毛俊水库水文工作/分期洪水/毛俊旬平均流量表1973-2003.xls',xiaxunpjun/31,'sheet1','C97')

% 逐日平均流量
Q = zeros(31,31,12);     %年/日/月
for i = 1973:2003
    Q(i-1972,:,:)=xlsread([file,'\data\source\毛俊日流量表1973-2003.xls'],num2str(i),'B3:M33'); 
end

%逐年旬日平均最大值
Q1max_xun = zeros(31,12,3);
%逐年月日平均最大值
Q1max_Moon = zeros(31,12);

% for i = 1 :31        
%     for j = 1:12
%         Q1max_xun(i,j,1) = max( Q(i,1:10,j) );     %上旬
%         Q1max_xun(i,j,2) = max( Q(i,11:20,j) );
%         Q1max_xun(i,j,3) = max( Q(i,21:31,j) );
%         Q1max_Moon(i,j) = max( Q(i,1:31,j) );     
% 
%     end
% end


% Q1max_MoonEx = zeros(1,12);
% Q1max_xunEx = zeros(1,12*3);
% for i = 1 : 12
%     Q1max_MoonEx(i) = mean(Q1max_Moon(:,i));   %逐月最大值平均
%      for j = 1 : 3
%          Q1max_xunEx(i*3-3+j) = mean(Q1max_xun(:,i,j)) ;   %逐旬最大值平均
%      end
% end

% xlswrite('I:/毛俊水库水文工作/分期洪水/毛俊最大值平均流量表1973-2003.xls',Q1max_MoonEx,'sheet1','B2')
% xlswrite('I:/毛俊水库水文工作/分期洪水/毛俊最大值平均流量表1973-2003.xls',Q1max_xunEx,'sheet1','B3')


% %找出年最大流量所在月与旬
% Q1max_yearEx = zeros(31,2);
% 
% for i = 1:31
%     
%     [ x , y] = find ( Q(i,:,:) == max ( max ( Q(i,:,:) ) ) ) ;
%     if numel(x)>1
%         y = y(1);
%     end
%     a = ceil(y/31);
%     b = mod(y,31);
%     b = ceil(b/10);
%     Q1max_yearEx(i,:) = [a,b];
% end
% 
% xlswrite('I:/毛俊水库水文工作/分期洪水/毛俊最大值平均流量表1973-2003.xls',Q1max_yearEx,'sheet2','B2')

%逐月平均值

Month_Ex = zeros(1,12);



for i = 1 :12 
    Month_Ex(1,i) = nansum(nansum( Q(:,:,i) )) / (sum(sum(Q(:,:,i)~=0))-numel(find(isnan(Q(:,:,i)))));
    

    
 end


% xlswrite('I:/毛俊水库水文工作/分期洪水/毛俊月平均流量表1973-2003.xls',Month_Ex,'sheet1','B2')

%逐旬平均值
Xun_Ex = zeros(1,3*12);

for i = 1:12
     for j = 1 : 3
         if j == 1
             Xun_Ex(i*3-3+j) = nansum(nansum( Q(:,1:10,i) )) / (sum(sum(Q(:,1:10,i)~=0))-numel(find(isnan(Q(:,1:10,i))))) ;   %逐旬平均
         elseif j==2
             Xun_Ex(i*3-3+j) = nansum(nansum( Q(:,11:20,i) )) / (sum(sum(Q(:,11:20,i)~=0))-numel(find(isnan(Q(:,11:20,i))))) ;  ;   %逐旬平均    
         else 
             Xun_Ex(i*3-3+j) = nansum(nansum( Q(:,21:31,i) )) / (sum(sum(Q(:,21:31,i)~=0))-numel(find(isnan(Q(:,21:31,i))))) ;  ;   %逐旬平均    
         end
         
         
         
     end
         
end


xlswrite([file,'\data\source\毛俊日流量表1973-2003.xls'],Xun_Ex,'sheet2','B2')


