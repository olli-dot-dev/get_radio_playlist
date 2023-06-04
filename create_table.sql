CREATE TABLE `played_songs` (
  `station` varchar(30) NOT NULL,
  `time_played` datetime DEFAULT NULL,
  `artist` varchar(128) DEFAULT NULL,
  `song` varchar(128) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;