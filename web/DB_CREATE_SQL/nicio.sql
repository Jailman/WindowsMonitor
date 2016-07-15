CREATE TABLE `nicio_stat` (
  `id` integer PRIMARY KEY AUTOINCREMENT NOT NULL,
  `host` varchar(256) DEFAULT NULL,
  `sent_speed_kb` int(11) DEFAULT NULL,
  `recv_speed_kb` int(11) DEFAULT NULL,
  `sent_speed_pkt` int(11) DEFAULT NULL,
  `recv_speed_pkt` int(11) DEFAULT NULL,
  `time` bigint(11) DEFAULT NULL
);
