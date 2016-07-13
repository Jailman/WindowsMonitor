CREATE TABLE `mem_stat` (
  `id` integer PRIMARY KEY AUTOINCREMENT NOT NULL,
  `host` varchar(256) DEFAULT NULL,
  `mem_free` int(11) DEFAULT NULL,
  `mem_usage` int(11) DEFAULT NULL,
  `mem_total` int(11) DEFAULT NULL,
  -- `load_avg` varchar(128) DEFAULT NULL,
  `time` bigint(11) DEFAULT NULL
);
