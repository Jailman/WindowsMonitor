CREATE TABLE `diskio_stat` (
  `id` integer PRIMARY KEY AUTOINCREMENT NOT NULL,
  `host` varchar(256) DEFAULT NULL,
  `read_speed_count` int(11) DEFAULT NULL,
  `write_speed_count` int(11) DEFAULT NULL,
  `read_speed_kb` int(11) DEFAULT NULL,
  `write_speed_kb` int(11) DEFAULT NULL,
  `read_time` int(20) DEFAULT NULL,
  `write_time` int(20) DEFAULT NULL,
  `time` bigint(11) DEFAULT NULL
);
