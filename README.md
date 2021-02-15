# SocialSOP

### Create Database
~~~
CREATE TABLE IF NOT EXISTS pages (
  id varchar(128) NOT NULL,
  page_token varchar(128) NOT NULL,
  about text DEFAULT NULL,
  engagement_count int(11) DEFAULT NULL,
  engagement_social_sentence varchar(128) DEFAULT NULL,
  fan_count int(11) DEFAULT NULL,
  picture text DEFAULT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE IF NOT EXISTS posts (
  id varchar(128) NOT NULL,
  picture text DEFAULT NULL,
  status_type varchar(128) DEFAULT NULL,
  full_picture text DEFAULT NULL,
  page_id varchar(128) NOT NULL,
  PRIMARY KEY (id),
  KEY page_id (page_id),
  CONSTRAINT posts_ibfk_1 FOREIGN KEY (page_id) REFERENCES pages (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
~~~