CREATE TABLE `cpu_stat` (
  `id` integer PRIMARY KEY AUTOINCREMENT NOT NULL,
  `host` varchar(256) DEFAULT NULL,
  `cpu_percent` int(11) DEFAULT NULL,
  `cpu_user` int(11) DEFAULT NULL,
  `cpu_system` int(11) DEFAULT NULL,
  `cpu_idle` int(11) DEFAULT NULL,
  -- `load_avg` varchar(128) DEFAULT NULL,
  `time` bigint(11) DEFAULT NULL
);
