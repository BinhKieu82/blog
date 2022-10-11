# import logging
# import os
# import time
# from threading import Thread

# from fbchat import Client
# from fbchat.models import Message, ThreadType
# import schedule

# class Bot(Client):
#   #receicer msg from other & reply a msg
#   def onMessage(self, message_object, author_id, thread_id, thread_type, **kwargs):
#     lst_msg = list('Chúc mừng năm mới')
#     if author_id != self.uid and message_object.text in lst_msg:
#       self.send(Message(text='Năm mới chúc .....'),
#         thread_id=author_id,
#         thread_type=ThreadType.USER)

#   #sending msg to the friend list
#   def do_something(self):
#     #Đổi tên function cho phù hợp
#     logging.basicConfig(level=logging.INFO)
#     user_ids = ['100005089816527'] # List chứa fb id của những người bạn muốn gửi
#     for user_id in user_ids:
#       self.send(Message(text="Chúc mừng năm mới"),
#         thread_id=user_id, thread_type=ThreadType.USER)
#       self.sendLocalImage('/home/dosontung007/Pictures/wallpaper.png', message=Message(text='Chúc mừng năm mới'),
#         thread_id=user_id, thread_type=ThreadType.USER)
#       logging.info('Sent success to %s' % "100005089816527")
  
#   # def job_that_executes_once():
#   #   Bot(os.environ['USERNAME_'], os.environ['PASSWORD']).do_something()
#   #   return schedule.CancelJob

  
#   def reply_msg():
#     Bot(os.environ['USERNAME_'], os.environ['PASSWORD']).listen()


#   # def send_msg():
#   #   schedule.every().day.at('00:00').do(job_that_executes_once)
#   #   while True:
#   #     schedule.run_pending()
#   #     time.sleep(1)

  
#   #send msg without timer
#   #remove job_that_executes_once & replace send_msg() function above by this
#   def send_msg():
#     Bot(os.environ['USERNAME_'],os.environ['PASSWORD']).do_something()
  

#   #run parallely reply_msg() & send_msg()
#   def main():
#     thread1 = Thread(target=send_msg)
#     thread2 = Thread(target=reply_msg)

#     thread1.start()
#     thread2.start()

#     thread1.join()
#     thread2.join()


#   if __name__ == '__main__':
#     main()