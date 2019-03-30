import pycaptcha.solve_it.cut_img
import pycaptcha.solve_it.de_line
import pycaptcha.solve_it.de_point

from PIL import Image
import pycaptcha.make_captcha.noise
import pycaptcha.make_captcha.make_capt

# 图像转化为01 np数组 Threshold为阀值
def get_mode(img,Threshold=100):
    mode = pycaptcha.make_captcha.make_capt.get_modes(img,Threshold)
    return mode


# 将01 np数组转化为黑白图片
def mode_to_img(mode):
    img = pycaptcha.make_captcha.noise.mode_to_draw(mode)
    return img


# 将np数组噪点处理，mode 数组，N是加噪率（边缘存在1个以上的黑点那么这个点有一点概率变黑） Z 加噪次数 返回数组
def show_noise_mode(mode, N, Z):
    new_mode = pycaptcha.make_captcha.noise.more_noise(mode, N, Z)
    return new_mode


# 将np数组噪点处理，mode 数组，N是加噪率（边缘存在1个以上的黑点那么这个点有一点概率变黑） Z 加噪次数 返回图片
def show_noise_img(mode, N, Z):
    new_img = pycaptcha.make_captcha.noise.more_noise(mode, N, Z, to_img='toimg')
    return new_img


# 偏移 传入np数组，横向偏移(默认右移)，纵向偏移，传出新的mode
def mode_pan(mode,width_x,height_y):
    new_mode = pycaptcha.make_captcha.make_capt.img_pan(mode,width_x,height_y)
    return new_mode


# 生成验证码 长宽 字符串个数 背景颜色 一般要上线用的话看源码改一改就好了
def make_capt_img(width,height,num_of_str,gray_value=255):
    image = pycaptcha.make_captcha.make_capt.get_captcha(width,height,num_of_str,gray_value=255)
    return image


# 生成简单的大写字母训练集图片
def get_train_img():
    file_name,image = pycaptcha.make_captcha.make_capt.train_img()
    return file_name,image

# 自定义生成训练图片
# def my_train_img():


def mode_img(mode,background=None):
    img = pycaptcha.solve_it.cut_img.mode_to_img(mode,background=None)
    return img

def mode_white_img(mode):
    img = pycaptcha.solve_it.cut_img.mode_to_img(mode,background=255)
    return img

def dele_noise(image, N, Z):
    img = pycaptcha.solve_it.de_point.clear_noise(image, N, Z)
    return img

def dele_line(image, N, pans=None):
    img = pycaptcha.solve_it.de_line.clear_line(image, N, pans=None)
    return img

def clear_train_img(image):
    img = pycaptcha.solve_it.de_line.clear_my_train_img(image)
    return img

def clear_lib_line(image):
    img = pycaptcha.solve_it.de_line.clear_my_line(image)
    return img

def cut_img_to_mode_list(image,max_width):
    img_mode_list = pycaptcha.solve_it.cut_img.cut_img(image,max_width)
    return img_mode_list

def cut_img_to_img_list(image,max_width,background=None):
    if background:
        mode_list = pycaptcha.solve_it.cut_img.cut_img(image,max_width)
        img_list = map(mode_white_img,mode_list)
        return img_list
    else:
        img_mode_list = pycaptcha.solve_it.cut_img.cut_img(image,max_width)
        return map(mode_img,img_mode_list)

# img = Image.open('1.png')
# print(get_mode(img))