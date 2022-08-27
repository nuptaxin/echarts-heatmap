from pyecharts import Geo
import pandas as pd

df = pd.read_excel('各省市经纬度.xlsx')
df.head()

geo = Geo("2016年全国各地级市GDP(万亿)",  # 设置地图标题
          title_color="#fff",  # 设置标题颜色为白色
          title_pos="center",  # 标题位置在中间
          width=1200,  # 图片宽度
          height=600,  # 图片长度
          background_color='#fff',  # 设置图片背景颜色

          )

attr = list(df['市'])
value = list(df['GDP(万亿)'])
print(value)
# geo_cities_coords = {df.iloc[i]['市'] for i in range(len(df))}
geo.add("",  # 标题，构建坐标系的时候已经写好，不需要设置，设为空
        attr,  # 城市名
        value,  # 各城市的GDP
        visual_range=[0, 120000000],  # 可视化深浅的范围
        visual_text_color="#fff",  # 标签的颜色
        #is_piecewise=True,  #设置颜色分段显示
        visual_split_number=10,  # 设置10个不同的组
        symbol_size=7.5,  # 设置散点大小为7.5
        is_visualmap=True,  # 设置颜色与value一一对应，value越高，颜色越深
        #is_label_show=True,
        #visual_type="size",
        #type="effectScatter", #发散圈圈
        # type="effectScatter",
        #border_color='#fff',
        visual_range_color=['#CCCCCC', '#000'],
        color='#fff',
        area_color='#fff',
        geo_normal_color='#fff',
        #geo_effect_color='#fff',
        #is_piecewise=False,
        #pieces= [{'min':0, 'max':1000 , 'color': 'grey', 'symbol_size':2},{'min':1000,'max':1000000000000000 ,'color': 'red','visual_text_color':"#fff",'is_visualmap':True,'visual_type':"size",'border_color':'#fff',}]
        #{{min:900, max:1500}, {value: 123, 'label': '123（自定义特殊颜色）', 'color': 'grey'}}
        # geo_cities_coords=geo_cities_coords#设置散点所在的经纬度
        )

geo.render("geo1.html")
