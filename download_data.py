
from YourLesson import downloads

downloads.clear_data()

# 下载文件
print("正在下载课程id到data文件夹")
downloads.save_to_file(type="方案内课程",methods=downloads.in_course)
downloads.save_to_file(type="方案外课程",methods=downloads.out_course)
downloads.save_to_file(type="本班课程",methods=downloads.recommended_course)
downloads.save_to_file(type="校公选课",methods=downloads.public_course)
print("文件下载完成")
