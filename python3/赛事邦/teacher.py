# -*-coding:utf-8-*-
import random
teacher_list = ['赵湘纹', '黄金伟', '林国振', '张艺', '张立', '钟玉梅', '李芳群', '关博', '洪彩霞', '林丽芬', '朱萍', '魏丽芬', '林邵宇', '王伟生', '郭庆平']

phone_list = ['13950326299','13905000937','13905000832','13163898989','13163878888','13107925252','17055632525','17055635757','13306927633','13305917356','13328676272','15659136799','15659755163','13255055629','18965077157']

all = []
for i in range(15):
    result = {}
    result['name'] = teacher_list[i]
    result['phone'] = phone_list[i]
    all.append(result)

print all
# def get_teacher():
#     return random.choice(teacher_list)
