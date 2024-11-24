import os
from dotenv import load_dotenv
import smtplib
load_dotenv()
yandex_login=os.getenv("LOGIN")
yandex_loginto="nemleinikita@yandex.ru"
yandex_password=os.getenv("PASSWORD")
server =smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(yandex_login,yandex_password)
text_letter="""Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""
tex_invitation="https://dvmn.org/profession-ref-program/id830437957/5tunx/"
name_to="Алексей"
name_from="Никита"
text_letter=text_letter.replace("%website%",tex_invitation)
text_letter=text_letter.replace("%friend_name%",name_to)
text_letter=text_letter.replace("%my_name%",name_from)
letter='''\
From: {yandex_login}
To: {yandex_loginto}
Subject: Важно!
Content-Type: text/plain; charset='UTF-8';

{text_letter}'''.format(text_letter=text_letter,yandex_login=yandex_login,yandex_loginto=yandex_loginto)
letter=letter.encode('UTF-8')
server.sendmail(yandex_login,yandex_loginto,letter)
server.quit()
