import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pyvirtualdisplay import Display
# 设置 DISPLAY 环境变量指向 Xvfb 虚拟显示
# 启动Xvfb虚拟显示
display = Display(visible=0, size=(2044,1024))
display.start()

# 启动 Xvfb
#os.system("Xvfb :99 -screen 0 1920x1080x24 &")
os.environ['DISPLAY'] = ':98'
os.environ["LIBGL_ALWAYS_SOFTWARE"] = "0"
os.environ["LIBGL_ALWAYS_INDIRECT"] = "0"
# 配置 Chrome 选项
chrome_options = Options()

chrome_options.add_argument("--start-fullscreen")  # 启动全屏模式
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument('--disable-dev-shm-usage')  # 避免共享内存问题
chrome_options.add_argument('--remote-debugging-port=9222')  # 启用远程调试
chrome_options.add_argument('--enable-gpu')  # 启用 GPU 加速
chrome_options.add_argument('--ignore-gpu-blacklist')  # 忽略 GPU 黑名单
chrome_options.add_argument('--use-gl=desktop')  # 使用桌面 OpenGL
chrome_options.add_argument('--window-size=2044x1024')  # 设置窗口大小
chrome_options.add_argument('--enable-unsafe-webgpu')  # 设置窗口大chrome_options.add_argument('--enable-unsafe-webgpu')  # 设置窗口大小小
chrome_options.add_argument('--disable-vulkan')
chrome_options.add_argument("--enable-gpu-rasterization")
chrome_options.add_argument("--enable-webgl-draft-extensions")
chrome_options.add_argument("--enable-webgl2-compute-context")

#chrome_options.add_argument("--headless")  # 无头模式
#chrome_options.add_argument('--disable-dev-shm-usage')
#chrome_options.add_argument("--enable-gpu-rasterization")
chrome_options.add_argument("--enable-zero-copy")
# 设置 ChromeDriver 路径
chrome_driver_path = '/usr/local/bin/chromedriver-linux64/chromedriver'

# 启动 Selenium 控制的 Chrome 浏览器
#service = Service(ChromeDriverManager().install())
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
# 打开 WebGL 页面
#driver.get('https://codesandbox.io/p/sandbox/cvqhmm')
driver.get('chrome://gpu')
# 在页面上等待几秒钟，以确保 WebGL 内容加载
driver.implicitly_wait(10)
#time.sleep(20)

# 执行 JavaScript 进行页面滚动
$driver.execute_script("window.scrollBy(0, 300);")

# 录制屏幕
#os.system("ffmpeg -video_size 1920x1080 -framerate 25 -f x11grab -i :99 -c:v libx264 -preset ultrafast output2.mp4 &")


#time.sleep(240)

# 截图确认页面加载成功
driver.save_screenshot('webgl_test.png')

#driver.get('chrome://flags')
# 在页面上等待几秒钟，以确保 WebGL 内容加载
#driver.implicitly_wait(20)

#driver.execute_script("window.scrollBy(0, 1200);")
#driver.save_screenshot('webgl_test1.png')

# 停止录制
#os.system("killall ffmpeg")


# 关闭浏览器
driver.quit()
display.stop()
