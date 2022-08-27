from pyecharts import Geo
import pandas as pd

df = pd.read_excel('各省市经纬度.xlsx')
df.head()

geo = Geo("金融科技关键词2019",  # 设置地图标题
          title_color="#fff",  # 设置标题颜色为白色
          title_pos="center",  # 标题位置在中间
          width=1200,  # 图片宽度
          height=600,  # 图片长度
          background_color='#fff',  # 设置图片背景颜色
          )

attr = list(df['城市'])
value = list(df['time2019'])
actual = dict(zip(attr,value))
print(type(actual))
nonvals = []
vals = []
for key,value in actual.items():
    if value >= 10000000:
        nonvals.append(key)
        vals.append(value)
print(vals)
# geo_cities_coords = {df.iloc[i]['市'] for i in range(len(df))}
geo.add("",  # 标题，构建坐标系的时候已经写好，不需要设置，设为空
        nonvals,  # 城市名
        vals,  # 各城市的GDP
        visual_range=[0, 582601461],  # 可视化深浅的范围
        visual_text_color="#fff",  # 标签的颜色
        # is_piecewise=False,  #设置颜色分段显示
        # visual_split_number=10,  # 设置10个不同的组
        symbol_size=2,  # 设置散点大小为7.5
        is_visualmap=True,  # 设置颜色与value一一对应，value越高，颜色越深
        #visual_range=[{min:0,max:145834105,'color': '#CCCCCC'},{},{}],
        # is_label_show=True,
        visual_type="size",
        type="effectScatter", #发散圈圈
        # type="effectScatter",
        border_color='#000',
        geo_normal_color='#fff',
        #area_color='#CCCCCC',
        #is_piecewise=True,
        #geo_effect_color='#CCCCCC',
        visual_range_color=['#CCCCCC','#fff'],
        #pieces= [{'min':0, 'max':1000 , 'color': 'grey', 'symbol_size':2},{'min':1000,'max':1000000000000000 ,'color': 'red','visual_text_color':"#fff",'is_visualmap':True,'visual_type':"size",'border_color':'#fff',}]
        pieces= [{'color': 'grey','visual_type':"size"}]
        #{{min:900, max:1500}, {value: 123, 'label': '123（自定义特殊颜色）', 'color': 'grey'}}
        # geo_cities_coords=geo_cities_coords#设置散点所在的经纬度
        )

geo.render("geo2019-new.html")
