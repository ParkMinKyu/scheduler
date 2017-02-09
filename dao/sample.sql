/*database 이름은 각자 편하게*/
create database myintranet;

/*테이블 생성*/
CREATE TABLE `my_schedule` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `start` datetime NOT NULL,
  `end` datetime NOT NULL,
  `allDay` char(1) NOT NULL DEFAULT 'Y',
  PRIMARY KEY (`id`)
);

insert into my_schedule(title, start, end, allDay) values('my schedule', now(), now(), 'Y');

commit;
