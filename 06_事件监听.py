import pygame


pygame.init()

# 创建游戏窗口480*700
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))

# 绘制英雄的飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (150, 300))
# 可以在screen对象完成所有blit后再调用update方法
pygame.display.update()


# 定义rect对象记录英雄的初始位置
hero_rect = pygame.Rect(150, 300, 102, 126)

# 创建时钟对象
clock = pygame.time.Clock()

# 游戏循环，意味着游戏的正式开始
while True:

    # 1 可以指定游戏循环内部代码执行的频率
    clock.tick(60)

    # 监听事件
    for event in pygame.event.get():

        # 判断事件类型是否是退出事件

        if event.type == pygame.QUIT:

            print("游戏退出。。。")
            # quit卸载所有的模块
            pygame.quit()
            # exit直接终止正在执行的程序
            exit()
    # 2 修改飞机的位置
    hero_rect.y -= 1

    # 判断飞机的位置
    if hero_rect.y <= 0:
        hero_rect.y = 700


    # 3 调用blit方法绘制图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 4 调用update方法更新屏幕
    pygame.display.update()


pygame.quit()