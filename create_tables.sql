DROP TABLE IF EXISTS course_offerings;

CREATE TABLE course_offerings(
            uuid TEXT PRIMARY KEY
            ,course_uuid TEXT
            ,term_code INTEGER
            ,name TEXT);



DROP TABLE IF EXISTS courses;

CREATE TABLE courses(
            uuid TEXT PRIMARY KEY
            ,name TEXT
            ,number INTEGER);



DROP TABLE IF EXISTS grade_distributions;

CREATE TABLE grade_distributions(
            course_offering_uuid TEXT
            ,section_number INTEGER
            ,a_count INTEGER
            ,ab_count INTEGER
	    ,b_count INTEGER
	    ,bc_count INTEGER
	    ,c_count INTEGER
	    ,d_count INTEGER
            ,f_count INTEGER
	    ,s_count INTEGER
	    ,u_count INTEGER
	    ,cr_count INTEGER
	    ,n_count INTEGER
	    ,p_count INTEGER
	    ,i_coubt INTEGER
	    ,nw_count INTEGER
	    ,nr_count INTEGER
	    ,other_count INTEGER);



DROP TABLE IF EXISTS instructors;

CREATE TABLE instructors(
            id INTEGER PRIMARY KEY
            ,name TEXT);



DROP TABLE IF EXISTS rooms;

CREATE TABLE rooms(
            uuid TEXT PRIMARY KEY
            ,facility_code TEXT
            ,roow_code TEXT);


DROP TABLE IF EXISTS schedules;

CREATE TABLE schedules(
            uuid TEXT PRIMARY KEY
            ,start_time INTEGER
            ,end_time INTEGER
            ,mon BOOLEAN
	    ,tues BOOLEAN
	    ,wed BOOLEAN
	    ,thurs BOOLEAN
	    ,fri BOOLEAN
	    ,sat BOOLEAN
	    ,sun BOOLEAN);


DROP TABLE IF EXISTS sections;

CREATE TABLE sections(
            uuid TEXT PRIMARY KEY
            ,course_offering_uuid TEXT
            ,section_type TEXT
            ,number INTEGER
	    ,room_uuid TEXT
	    ,schedule_uuid TEXT);


DROP TABLE IF EXISTS subject_memberships;

CREATE TABLE subject_memberships(
            subject_code TEXT
            ,course_offering_uuid TEXT);



DROP TABLE IF EXISTS subjects;

CREATE TABLE subjects(
            code TEXT PRIMARY KEY
            ,name TEXT
            ,abbreviation TEXT);



DROP TABLE IF EXISTS teachings;

CREATE TABLE teachings(
            instructor_id INTEGER
            ,section_uuid TEXT);
