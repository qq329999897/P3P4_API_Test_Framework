create DATABASE interface_test_db;

use interface_test_db;

create table requests_info(
	requests_id VARCHAR(10),
	requests_name VARCHAR(100) not null,
	requests_type VARCHAR(10) not null,
	requests_header VARCHAR(1000),
	requests_url VARCHAR(200) not null,
	requests_url_params VARCHAR(1000),
	requests_post_data VARCHAR(1000),
	PRIMARY key(requests_id)
)DEFAULT CHARSET = 'utf8';

create table case_info(
	case_id VARCHAR(10),
	case_name VARCHAR(1000) not null,
	is_run VARCHAR(4) not null DEFAULT '是',
	PRIMARY Key(case_id)
)DEFAULT CHARSET = 'utf8';

create table case_step_info(
	case_id VARCHAR(10) not null,
	case_step_id VARCHAR(10),
	requests_id VARCHAR(10),
	get_value_type VARCHAR(10),
	get_value_code VARCHAR(1000),
	get_value_variable VARCHAR(10),
	excepted_result_type VARCHAR(100),
	excepted_result VARCHAR(1000),
	CONSTRAINT fk_case FOREIGN KEY(case_id) REFERENCES case_info(case_id)
)DEFAULT CHARSET = 'utf8';


INSERT into case_info values('api_case_1','获取access_token接口测试','是');
INSERT into case_info values('api_case_2','创建标签接口测试','是');
INSERT into case_info values('api_case_3','删除标签接口测试','是');

INSERT into requests_info values('api_0001','获取access_token接口','get','','/cgi-bin/token','{"grant_type":"client_credential","appid":"wx55614004f367f8ca","secret":"65515b46dd758dfdb09420bb7db2c67f"}','');
INSERT into requests_info values('api_0002','创建标签接口','post','','/cgi-bin/tags/create','{"access_token":${token}}','{"tag":{"name":"邵阳"}}');
INSERT into requests_info values('api_0003','删除标签接口','post','','/cgi-bin/tags/delete','{"access_token":${token}}','{"tag":{"id":${tag_id}}}');

insert into case_step_info values('api_case_1','step_01','api_0001','无','','','body_regexp','"access_token":"(.+?)"');

insert into case_step_info values('api_case_2','step_01','api_0001','正则取值','"access_token":"(.+?)"','token','json_key_value','{"expires_in":7200}');
insert into case_step_info values('api_case_2','step_02','api_0002','无','','','json_key','tag');

insert into case_step_info values('api_case_3','step_01','api_0001','jsonpath取值','$.access_token','token','json_key','access_token');
insert into case_step_info values('api_case_3','step_02','api_0002','正则取值','"id":(.+?),','tag_id','json_key','');
insert into case_step_info values('api_case_3','step_03','api_0003','无','','','json_key_value','{"errcode":0}');

select * from case_info,case_step_info,requests_info 
where case_info.case_id = case_step_info.case_id and case_step_info.requests_id = requests_info.requests_id and case_info.is_run = '是'
order by case_info.case_id,case_step_info.case_step_id;

