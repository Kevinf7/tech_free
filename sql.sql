INSERT INTO role (name)
VALUES ('admin'),('user');

from app.admin_dashboard.models import User
from app import db
from datetime import datetime
now = datetime.now()
u = User(email="kevin_foong@yahoo.com", firstname="Kevin", lastname="Foong", password_hash="123", role_id=1, last_seen=now, create_date=now)
u.set_password('abc')
db.session.add(u)
db.session.commit()

==

Message

INSERT INTO message(name,email,message,user_read,create_date)
VALUES("John Smith", "john.smith@abc.com", "Hello how are you?", false, now());

INSERT INTO message(name,email,message,user_read,create_date)
VALUES("Amy Burr", "amy.burr@abc.com", "What a great website. Well done!", false, now());

INSERT INTO message(name,email,message,user_read,create_date)
VALUES("Troy Trojan", "troy@aabb.com", "Please help", false, now());

==

Page

insert into page (name, user_id, last_publish_date, create_date)
values ('home', 2, now(), now());

insert into page (name, user_id, last_publish_date, create_date)
values ('contact', 2, now(), now());

insert into page_status (name, create_date)
values ('draft', now());

insert into page_status (name, create_date)
values ('published', now());

insert into page_status (name, create_date)
values ('archived', now());

INSERT into page_contact (status_id, content, page_id, user_id, update_date, create_date)
VALUES (1, "Drop me a line! Either fill in the form below or send me an email. I will get back to you shortly.", 8, 2, now(), now());

INSERT into page_contact (status_id, content, page_id, user_id, update_date, create_date)
VALUES (2, "Drop me a line! Either fill in the form below or send me an <a href='abc'>email</a>. I will get back to you shortly. Thanks!", 8, 2, now(), now());


POST

INSERT into post (slug, active, create_date, post, title, update_date, user_id)
VALUES ('test-slug', 1, now(), 'This is a test post', 'Some title', now(), 2);

INSERT into post (slug, active, create_date, post, title, update_date, user_id)
VALUES ('another-slug', 1, now(), 'Another test post', 'Yep 123', now(), 2);


INSERT INTO image_type(name)
values('blog');
INSERT INTO image_type(name)
values('page');

INSERT INTO comment(comment, name,email,post_id,create_date)
values('Nice post by the way','Joe','joe@abc.com',1,now());
INSERT INTO comment(comment, name,email,post_id,create_date)
values('I have a question','Mary','mary@jjj.com',1,now());
