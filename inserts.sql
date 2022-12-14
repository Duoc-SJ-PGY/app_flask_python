INSERT INTO `region` (`id_region`, `nom_region`) VALUES 

(1, 'Arica y Parinacota'),
(2, 'Tarapacá'),
(3, 'Antofagasta'),
(4, 'Atacama'),
(5, 'Coquimbo'),
(6, 'Valparaiso'),
(7, 'Metropolitana de Santiago'),
(8, 'Libertador General Bernardo OHiggins'),
(9, 'Maule'),
(10, 'Bio-Bío'),
(11, 'La Araucanía'),
(12, 'Los Ríos'),
(13, 'Los Lagos'),
(14, 'Aysén del General Carlos Ibáñez del Campo'),
(15, 'Magallanes y de la Antártica Chilena'),
(16, 'Ñuble');


INSERT INTO `provincia` (`id_provincia`, `nom_provincia`, `id_region`) VALUES
(1, 'Antártica Chilena', 15),
(2, 'Antofagasta', 3),
(3, 'Arauco', 10),
(4, 'Arica', 1),
(5, 'Aysén', 14),
(6, 'Bio-Bío', 10),
(7, 'Cachapoal', 8),
(8, 'Capitán Prat', 14),
(9, 'Cardenal Caro', 14),
(10, 'Cauquenes', 9),
(11, 'Cautín', 11),
(12, 'Chacabuco', 7),
(13, 'Chañaral', 4),
(14, 'Chiloé', 13),
(15, 'Choapa', 5),
(16, 'Colchagua', 8),
(17, 'Concepción', 10),
(18, 'Copiapó', 4),
(19, 'Cordillera', 7),
(20, 'Coyhaique', 14),
(21, 'Curicó', 9),
(22, 'Diguillín', 16),
(23, 'El Loa', 3),
(24, 'Elqui', 5),
(25, 'General Carrera', 14),
(26, 'Huasco', 4),
(27, 'Iquique', 2),
(28, 'Isla de Pascua', 6),
(29, 'Itata', 16),
(30, 'Limarí', 5),
(31, 'Linares', 9),
(32, 'Llanquihue', 13),
(33, 'Los Andes', 6),
(34, 'Magallanes', 15),
(35, 'Maipo', 7),
(36, 'Malleco', 11),
(37, 'Marga Marga', 6),
(38, 'Melipilla', 7),
(39, 'Osorno', 13),
(40, 'Palena', 13),
(41, 'Parinacota', 1),
(42, 'Petorca', 6),
(43, 'Punilla', 16),
(44, 'Quillota', 6),
(45, 'Ranco', 12),
(46, 'San Antonio', 6),
(47, 'San Felipe de Aconcagua', 6),
(48, 'Santiago', 7),
(49, 'Talagante', 7),
(50, 'Talca', 9),
(51, 'El Tamarugal', 2),
(52, 'Tierra del Fuego', 15),
(53, 'Tocopilla', 3),
(54, 'Valdivia', 12),
(55, 'Valparaiso', 6),
(56, 'Última Esperanza', 15);

INSERT INTO `comuna` (`id_comuna`, `nom_comuna`,`id_provincia`) VALUES
(1, 'Antártica', 1),
(2, 'Cabo de Hornos', 1),
(3, 'Antofagasta', 2),
(4, 'Mejillones', 2),
(5, 'Sierra Gorda', 2),
(6, 'Taltal', 2),
(7, 'Arauco', 3),
(8, 'Cañete', 3),
(9, 'Contulmo', 3),
(10, 'Curanilahue', 3),
(11, 'Lebu', 3),
(12, 'Los Alamos', 3),
(13, 'Tirúa', 3),
(14, 'Arica', 4),
(15, 'Camarones', 4),
(16, 'Aisen', 5),
(17, 'Cisnes', 5),
(18, 'Guaitecas', 5),
(19, 'Alto Biobío', 6),
(20, 'Antuco', 6),
(21, 'Cabrero', 6),
(22, 'Laja', 6),
(23, 'Los Ángeles', 6),
(24, 'Mulchén', 6),
(25, 'Nacimiento', 6),
(26, 'Negrete', 6),
(27, 'Quilaco', 6),
(28, 'Quilleco', 6),
(29, 'San Rosendo', 6),
(30, 'Santa Bárbara', 6),
(31, 'Tucapel', 6),
(32, 'Yumbel', 6),
(33, 'Codegua', 7),
(34, 'Coinco', 7),
(35, 'Coltauco', 7),
(36, 'Doñihue', 7),
(37, 'Graneros', 7),
(38, 'Las Cabras', 7),
(39, 'Machalí', 7),
(40, 'Malloa', 7),
(41, 'Mostazal', 7),
(42, 'Olivar', 7),
(43, 'Peumo', 7),
(44, 'Pichidegua', 7),
(45, 'Quinta de Tilcoco', 7),
(46, 'Rancagua', 7),
(47, 'Rengo', 7),
(48, 'Requínoa', 7),
(49, 'San Vicente', 7),
(50, 'Cochrane', 8),
(51, 'O Higgins', 8),
(52, 'Tortel', 8),
(53, 'La Estrella', 9),
(54, 'Litueche', 9),
(55, 'Marchihue', 9),
(56, 'Navidad', 9),
(57, 'Paredones', 9),
(58, 'Pichilemu', 9),
(59, 'Cauquenes', 10),
(60, 'Chanco', 10),
(61, 'Pelluhue', 10),
(62, 'Carahue', 11),
(63, 'Cholchol', 11),
(64, 'Cunco', 11),
(65, 'Curarrehue', 11),
(66, 'Freire', 11),
(67, 'Galvarino', 11),
(68, 'Gorbea', 11),
(69, 'Lautaro', 11),
(70, 'Loncoche', 11),
(71, 'Melipeuco', 11),
(72, 'Nueva Imperial', 11),
(73, 'Padre Las Casas', 11),
(74, 'Perquenco', 11),
(75, 'Pitrufquén', 11),
(76, 'Pucón', 11),
(77, 'Saavedra', 11),
(78, 'Temuco', 11),
(79, 'Teodoro Schmidt', 11),
(80, 'Toltén', 11),
(81, 'Vilcún', 11),
(82, 'Villarrica', 11),
(83, 'Colina', 12),
(84, 'Lampa', 12),
(85, 'TilTil', 12),
(86, 'Chañaral', 13),
(87, 'Diego de Almagro', 13),
(88, 'Ancud', 14),
(89, 'Castro', 14),
(90, 'Chonchi', 14),
(91, 'Curaco de Vélez', 14),
(92, 'Dalcahue', 14),
(93, 'Puqueldón', 14),
(94, 'Queilén', 14),
(95, 'Quellón', 14),
(96, 'Quemchi', 14),
(97, 'Quinchao', 14),
(98, 'Canela', 15),
(99, 'Illapel', 15),
(100, 'Los Vilos', 15),
(101, 'Salamanca', 15),
(102, 'Chimbarongo', 16),
(103, 'Chépica', 16),
(104, 'Lolol', 16),
(105, 'Nancagua', 16),
(106, 'Palmilla', 16),
(107, 'Peralillo', 16),
(108, 'Placilla', 16),
(109, 'Pumanque', 16),
(110, 'San Fernando', 16),
(111, 'Santa Cruz', 16),
(112, 'Chiguayante', 17),
(113, 'Concepción', 17),
(114, 'Coronel', 17),
(115, 'Florida', 17),
(116, 'Hualpén', 17),
(117, 'Hualqui', 17),
(118, 'Lota', 17),
(119, 'Penco', 17),
(120, 'San Pedro de la Paz', 17),
(121, 'Santa Juana', 17),
(122, 'Talcahuano', 17),
(123, 'Tomé', 17),
(124, 'Caldera', 18),
(125, 'Copiapó', 18),
(126, 'Tierra Amarilla', 18),
(127, 'Pirque', 19),
(128, 'Puente Alto', 19),
(129, 'San José de Maipo', 19),
(130, 'Coihaique', 20),
(131, 'Lago Verde', 20),
(132, 'Curicó', 21),
(133, 'Hualañé', 21),
(134, 'Licantén', 21),
(135, 'Molina', 21),
(136, 'Rauco', 21),
(137, 'Romeral', 21),
(138, 'Sagrada Familia', 21),
(139, 'Teno', 21),
(140, 'Vichuquén', 21),
(141, 'Bulnes', 22),
(142, 'Chillán', 22),
(143, 'Chillán Viejo', 22),
(144, 'El Carmen', 22),
(145, 'Pemuco', 22),
(146, 'Pinto', 22),
(147, 'Quillón', 22),
(148, 'San Ignacio', 22),
(149, 'Yungay', 22),
(150, 'Calama', 23),
(151, 'Ollagüe', 23),
(152, 'San Pedro de Atacama', 23),
(153, 'Andacollo', 24),
(154, 'Coquimbo', 24),
(155, 'La Higuera', 24),
(156, 'La Serena', 24),
(157, 'Paihuano', 24),
(158, 'Vicuña', 24),
(159, 'Chile Chico', 25),
(160, 'Río Ibáñez', 25),
(161, 'Alto del Carmen', 26),
(162, 'Freirina', 26),
(163, 'Huasco', 26),
(164, 'Vallenar', 26),
(165, 'Alto Hospicio', 27),
(166, 'Iquique', 27),
(167, 'Isla de Pascua', 28),
(168, 'Cobquecura', 29),
(169, 'Coelemu', 29),
(170, 'Ninhue', 29),
(171, 'Portezuelo', 29),
(172, 'Quirihue', 29),
(173, 'Ránquil', 29),
(174, 'Treguaco', 29),
(175, 'Combarbalá', 30),
(176, 'Monte Patria', 30),
(177, 'Ovalle', 30),
(178, 'Punitaqui', 30),
(179, 'Río Hurtado', 30),
(180, 'Colbún', 31),
(181, 'Linares', 31),
(182, 'Longaví', 31),
(183, 'Parral', 31),
(184, 'Retiro', 31),
(185, 'San Javier', 31),
(186, 'Villa Alegre', 31),
(187, 'Yerbas Buenas', 31),
(188, 'Calbuco', 32),
(189, 'Cochamó', 32),
(190, 'Fresia', 32),
(191, 'Frutillar', 32),
(192, 'Llanquihue', 32),
(193, 'Los Muermos', 32),
(194, 'Maullín', 32),
(195, 'Puerto Montt', 32),
(196, 'Puerto Varas', 32),
(197, 'Calle Larga', 33),
(198, 'Los Andes', 33),
(199, 'Rinconada', 33),
(200, 'San Esteban', 33),
(201, 'Laguna Blanca', 34),
(202, 'Punta Arenas', 34),
(203, 'Río Verde', 34),
(204, 'San Gregorio', 34),
(205, 'Buin', 35),
(206, 'Calera de Tango', 35),
(207, 'Paine', 35),
(208, 'San Bernardo', 35),
(209, 'Angol', 36),
(210, 'Collipulli', 36),
(211, 'Curacautín', 36),
(212, 'Ercilla', 36),
(213, 'Lonquimay', 36),
(214, 'Los Sauces', 36),
(215, 'Lumaco', 36),
(216, 'Purén', 36),
(217, 'Renaico', 36),
(218, 'Traiguén', 36),
(219, 'Victoria', 36),
(220, 'Limache', 37),
(221, 'Olmué', 37),
(222, 'Quilpué', 37),
(223, 'Villa Alemana', 37),
(224, 'Alhué', 38),
(225, 'Curacaví', 38),
(226, 'María Pinto', 38),
(227, 'Melipilla', 38),
(228, 'San Pedro', 38),
(229, 'Osorno', 39),
(230, 'Puerto Octay', 39),
(231, 'Purranque', 39),
(232, 'Puyehue', 39),
(233, 'Río Negro', 39),
(234, 'San Juan de la Costa', 39),
(235, 'San Pablo', 39),
(236, 'Chaitén', 40),
(237, 'Futaleufú', 40),
(238, 'Hualaihué', 40),
(239, 'Palena', 40),
(240, 'General Lagos', 41),
(241, 'Putre', 41),
(242, 'Cabildo', 42),
(243, 'La Ligua', 42),
(244, 'Papudo', 42),
(245, 'Petorca', 42),
(246, 'Zapallar', 42),
(247, 'Coihueco', 43),
(248, 'San Carlos', 43),
(249, 'San Fabián', 43),
(250, 'San Nicolás', 43),
(251, 'Ñiquén', 43),
(252, 'Calera', 44),
(253, 'Hijuelas', 44),
(254, 'La Cruz', 44),
(255, 'Nogales', 44),
(256, 'Quillota', 44),
(257, 'Futrono', 45),
(258, 'La Unión', 45),
(259, 'Lago Ranco', 45),
(260, 'Río Bueno', 45),
(261, 'Algarrobo', 46),
(262, 'Cartagena', 46),
(263, 'El Quisco', 46),
(264, 'El Tabo', 46),
(265, 'San Antonio', 46),
(266, 'Santo Domingo', 46),
(267, 'Catemu', 47),
(268, 'Llaillay', 47),
(269, 'Panquehue', 47),
(270, 'Putaendo', 47),
(271, 'San Felipe', 47),
(272, 'Santa María', 47),
(273, 'Cerrillos', 48),
(274, 'Cerro Navia', 48),
(275, 'Conchalí', 48),
(276, 'El Bosque', 48),
(277, 'Estación Central', 48),
(278, 'Huechuraba', 48),
(279, 'Independencia', 48),
(280, 'La Cisterna', 48),
(281, 'La Florida', 48),
(282, 'La Granja', 48),
(283, 'La Pintana', 48),
(284, 'La Reina', 48),
(285, 'Las Condes', 48),
(286, 'Lo Barnechea', 48),
(287, 'Lo Espejo', 48),
(288, 'Lo Prado', 48),
(289, 'Macul', 48),
(290, 'Maipú', 48),
(291, 'Pedro Aguirre Cerda', 48),
(292, 'Peñalolén', 48),
(293, 'Providencia', 48),
(294, 'Pudahuel', 48),
(295, 'Quilicura', 48),
(296, 'Quinta Normal', 48),
(297, 'Recoleta', 48),
(298, 'Renca', 48),
(299, 'San Joaquín', 48),
(300, 'San Miguel', 48),
(301, 'San Ramón', 48),
(302, 'Santiago', 48),
(303, 'Vitacura', 48),
(304, 'Ñuñoa', 48),
(305, 'El Monte', 49),
(306, 'Isla de Maipo', 49),
(307, 'Padre Hurtado', 49),
(308, 'Peñaflor', 49),
(309, 'Talagante', 49),
(310, 'Constitución', 50),
(311, 'Curepto', 50),
(312, 'Empedrado', 50),
(313, 'Maule', 50),
(314, 'Pelarco', 50),
(315, 'Pencahue', 50),
(316, 'Río Claro', 50),
(317, 'San Clemente', 50),
(318, 'San Rafael', 50),
(319, 'Talca', 50),
(320, 'Camiña', 51),
(321, 'Colchane', 51),
(322, 'Huara', 51),
(323, 'Pica', 51),
(324, 'Pozo Almonte', 51),
(325, 'Porvenir', 52),
(326, 'Primavera', 52),
(327, 'Timaukel', 52),
(328, 'María Elena', 53),
(329, 'Tocopilla', 53),
(330, 'Corral', 54),
(331, 'Lanco', 54),
(332, 'Los Lagos', 54),
(333, 'Mariquina', 54),
(334, 'Máfil', 54),
(335, 'Paillaco', 54),
(336, 'Panguipulli', 54),
(337, 'Valdivia', 54),
(338, 'Casablanca', 55),
(339, 'Concón', 55),
(340, 'Juan Fernández', 55),
(341, 'Puchuncaví', 55),
(342, 'Quintero', 55),
(343, 'Valparaíso', 55),
(344, 'Viña del Mar', 55),
(345, 'Natales', 56),
(346, 'Torres del Paine', 56);




INSERT INTO `producto` (`id_producto`, `sku`, `nombre_producto`,`marca`,`nom_proveedor`, `descripcion`,`precio`,`foto`,`cantidad`) VALUES
(1, '0001', 'Sets Zebra Sarasa Vintage', 'ZEBRA', 'ZEBRA','Toda la comodidad y suavidad de un Sarasa Clip, pero con bellos tonos vintage.' ,7490, 'https://cdnx.jumpseller.com/blanca-papeleria/image/14583469/resize/540/540?1656473515', 100),
(2, '0002', 'Set Pilot Juice Up Glossy Colors', 'PILOT', 'PILOT', 'Pilot nos trae estos nuevos colores de su linea Juice Up, en tonalidades vintage', 11990, 'https://cdnx.jumpseller.com/blanca-papeleria/image/26461123/resize/540/540?1660866194', 100),
(3, '0003', 'Set Zebra Sarasa Clip 0.5', 'ZEBRA', 'ZEBRA', 'Lo mejor de los lápices Zebra Sarasa clip juntos en un pack de 10 colores a un muy buen precio', 14490, 'https://cdnx.jumpseller.com/blanca-papeleria/image/15198378/resize/540/540?1656473456', 100),
(4, '0004', 'Sets Zebra Mildliner', 'ZEBRA', 'ZEBRA', 'Zebra Mildliner es conocido por tener una paleta de colores muy variables (25 tonos)', 7500, 'https://cdnx.jumpseller.com/blanca-papeleria/image/14583480/resize/540/540?1656473593', 100),
(5, '0005', 'Set Muji Tapa 0.5 mm', 'MUJI', 'MUJI', 'Definitivamente uno de los lápices gel que debes probar y enamorarte de su suavidad.', 8500, 'https://cdnx.jumpseller.com/blanca-papeleria/image/26461102/resize/540/540?1660866148', 100),
(6, '0006', 'Set 7 Colores Zebra Sarasa R', 'ZEBRA', 'ZEBRA', 'Sarasa R, un lápiz punta 0.4 mm, con sistema clip, tinta gel y su principal característica', 10990, 'https://cdnx.jumpseller.com/blanca-papeleria/image/16003909/resize/540/540?1657724069', 100),
(7, '0007', 'Set Sarasa Clip 0.5 Pastel', 'ZEBRA', 'ZEBRA', 'Lo mejor de los lápices Zebra Sarasa clip, juntos en un pack de 8 colores en tonos pastel', 11990, 'https://cdnx.jumpseller.com/blanca-papeleria/image/14583109/resize/540/540?1656473451', 100),
(8, '0008', 'Sets Zebra Sarasa Nano 0.3', 'ZEBRA', 'ZEBRA', ' lápiz de tinta gel y una punta extra fina de 0.3 mm que permite una escritura clara y hermosa, con una sensación de escritura suave incluso al ser un lápiz con una punta fina.', 11490, 'https://cdnx.jumpseller.com/blanca-papeleria/image/21450207/resize/540/540?1651341043', 100),
(9, '0009', 'Set Zebra Mildliner Minnie & Mickey', 'ZEBRA', 'Disney', 'Disney Store en conjunto con Zebra nos traen este hermoso set de Mildliners inspirado en Minnie y Mickey', 9592, 'https://cdnx.jumpseller.com/blanca-papeleria/image/26461016/resize/540/540?1660865929', 100),
(10, '0010', 'Set Zebra Deco Shine', 'ZEBRA', 'ZEBRA', 'El Set Zebra Deco Shine cuenta con 10 lápices, de tinta gel y en colores metalizados.', 14490, 'https://cdnx.jumpseller.com/blanca-papeleria/image/25480582/resize/540/540?1656703064', 100),
(11, '0011', 'Zebra Click Art Dark Tone', 'ZEBRA', 'ZEBRA', 'Rotuladores retráctiles ClickArt están hechos con una tinta innovadora que no se seca y evita las manchas molestas', 15490, 'https://cdnx.jumpseller.com/blanca-papeleria/image/15198437/resize/540/540?1656182416', 100)

;


DELETE FROM Productos WHERE id > 0;