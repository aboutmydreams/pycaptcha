from PIL import Image
import pycaptcha.pycapt
import pycaptcha.solve_it
import pycaptcha

name = "pycaptcha"

# 图像转化为01 np数组 Threshold为阀值
def get_mode(img,Threshold=100):
    return pycaptcha.pycapt.get_mode(img,Threshold)


# 将01 np数组转化为黑白图片
def mode_to_img(mode):
    return pycaptcha.pycapt.mode_to_img(mode)


# 将np数组噪点处理，mode 数组，N是加噪率（边缘存在1个以上的黑点那么这个点有一点概率变黑） Z 加噪次数 返回数组
def show_noise_mode(mode, N, Z):
    return pycaptcha.pycapt.show_noise_mode(mode, N, Z)


# 将np数组噪点处理，mode 数组，N是加噪率（边缘存在1个以上的黑点那么这个点有一点概率变黑） Z 加噪次数 返回图片
def show_noise_img(mode, N, Z):
    return pycaptcha.pycapt.show_noise_img(mode, N, Z)


# 偏移 传入np数组，横向偏移(默认右移)，纵向偏移，传出新的mode
def mode_pan(mode,width_x,height_y):
    return pycaptcha.pycapt.mode_pan(mode,width_x,height_y)


# 生成验证码 长宽 字符串个数 背景颜色 一般要上线用的话看源码改一改就好了
def make_capt_img(width,height,num_of_str,gray_value=255):
    return pycaptcha.pycapt.make_capt_img(width,height,num_of_str,gray_value=255)


# 生成简单的大写字母训练集图片
def get_train_img():
    file_name,image = pycaptcha.pycapt.get_train_img()
    return file_name,image

# 自定义生成训练图片
# def my_train_img():


def mode_img(mode,background=None):
    return pycaptcha.pycapt.mode_img(mode,background=None)

def mode_white_img(mode):
    return pycaptcha.pycapt.mode_img(mode,background=255)

def dele_noise(image, N, Z):
    return pycaptcha.pycapt.dele_noise(image, N, Z)

def dele_line(image, N, pans=None):
    return pycaptcha.pycapt.dele_line(image, N, pans=None)

def clear_train_img(image):
    return pycaptcha.pycapt.clear_train_img(image)

def clear_lib_line(image):
    return pycaptcha.pycapt.clear_lib_line(image)

def cut_img_to_mode_list(image,max_width):
    return pycaptcha.pycapt.cut_img_to_mode_list(image,max_width)

def cut_img_to_img_list(image,max_width,background=None):
    if background:
        return pycaptcha.pycapt.cut_img_to_img_list(image,max_width,background=255)
    else:
        return pycaptcha.pycapt.cut_img_to_img_list(image,max_width,background=None)