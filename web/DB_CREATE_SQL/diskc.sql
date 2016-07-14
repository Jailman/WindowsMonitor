CREATE TABLE `diskc_stat` (
  `id` integer PRIMARY KEY AUTOINCREMENT NOT NULL,
  `host` varchar(256) DEFAULT NULL,
  `disk_total` int(11) DEFAULT NULL,
  `disk_used` int(11) DEFAULT NULL,
  `disk_free` int(11) DEFAULT NULL,
  `disk_percent` int(11) DEFAULT NULL,
  `time` bigint(11) DEFAULT NULL
);
