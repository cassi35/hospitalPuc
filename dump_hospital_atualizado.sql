-- MySQL dump 10.13  Distrib 8.0.36, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: HospitalSaoLucas
-- ------------------------------------------------------
-- Server version	5.5.5-10.11.13-MariaDB-0ubuntu0.24.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Consulta`
--

DROP TABLE IF EXISTS `Consulta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Consulta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `data_hora` date DEFAULT NULL,
  `paciente_id` int(11) DEFAULT NULL,
  `medico_id` int(11) DEFAULT NULL,
  `especialidade_id` int(11) DEFAULT NULL,
  `status` enum('ativo','nao ativo') DEFAULT NULL,
  `observacoes` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_paciente` (`paciente_id`),
  KEY `fk_medico` (`medico_id`),
  KEY `fk_especidade` (`especialidade_id`),
  CONSTRAINT `fk_especidade` FOREIGN KEY (`especialidade_id`) REFERENCES `especialidade` (`id`) ON DELETE SET NULL,
  CONSTRAINT `fk_medico` FOREIGN KEY (`medico_id`) REFERENCES `Medico` (`id`) ON DELETE SET NULL,
  CONSTRAINT `fk_paciente` FOREIGN KEY (`paciente_id`) REFERENCES `Paciente` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Endereco`
--

DROP TABLE IF EXISTS `Endereco`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Endereco` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rua` varchar(30) DEFAULT NULL,
  `bairro` varchar(30) DEFAULT NULL,
  `cidade` varchar(30) DEFAULT NULL,
  `estado` varchar(30) DEFAULT NULL,
  `cep` char(8) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Exame`
--

DROP TABLE IF EXISTS `Exame`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Exame` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_exame` tinytext DEFAULT NULL,
  `data_exame` date DEFAULT NULL,
  `paciente_id` int(11) DEFAULT NULL,
  `medico_id` int(11) DEFAULT NULL,
  `resultado` tinytext DEFAULT NULL,
  `status` enum('solicitado','em andamento','concluído') DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_exame_paciente` (`paciente_id`),
  KEY `fk_exame_medico` (`medico_id`),
  CONSTRAINT `fk_exame_medico` FOREIGN KEY (`medico_id`) REFERENCES `Medico` (`id`) ON DELETE SET NULL,
  CONSTRAINT `fk_exame_paciente` FOREIGN KEY (`paciente_id`) REFERENCES `Paciente` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Medico`
--

DROP TABLE IF EXISTS `Medico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Medico` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(20) DEFAULT NULL,
  `cpf` char(11) DEFAULT NULL,
  `especialidade_id` int(11) DEFAULT NULL,
  `telefone` char(9) DEFAULT NULL,
  `email` tinytext DEFAULT NULL,
  `status` enum('ativo','nao ativo') DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_especialidade` (`especialidade_id`),
  CONSTRAINT `fk_especialidade` FOREIGN KEY (`especialidade_id`) REFERENCES `especialidade` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Paciente`
--

DROP TABLE IF EXISTS `Paciente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Paciente` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(20) DEFAULT NULL,
  `cpf` char(11) DEFAULT NULL,
  `data_nascimento` date DEFAULT NULL,
  `sexo` enum('m','f') DEFAULT NULL,
  `telefone` char(11) DEFAULT NULL,
  `contato_emergencia` char(11) DEFAULT NULL,
  `alergia` tinytext DEFAULT NULL,
  `endereco_id` int(11) DEFAULT NULL,
  `convenio_id` int(11) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_endereco` (`endereco_id`),
  KEY `fk_convenio` (`convenio_id`),
  CONSTRAINT `fk_convenio` FOREIGN KEY (`convenio_id`) REFERENCES `convenio` (`id`) ON DELETE SET NULL,
  CONSTRAINT `fk_endereco` FOREIGN KEY (`endereco_id`) REFERENCES `Endereco` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `convenio`
--

DROP TABLE IF EXISTS `convenio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `convenio` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(30) DEFAULT NULL,
  `tipo_plano` enum('Individual','Familiar','Empresarial') DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `especialidade`
--

DROP TABLE IF EXISTS `especialidade`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `especialidade` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) DEFAULT NULL,
  `descricao` text DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `financeiro`
--

DROP TABLE IF EXISTS `financeiro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `financeiro` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `paciente_id` int(11) DEFAULT NULL,
  `convenio_id` int(11) DEFAULT NULL,
  `valor` float DEFAULT NULL,
  `data_emissao` date DEFAULT NULL,
  `data_vencimento` date DEFAULT NULL,
  `status_pagamento` enum('pago','pendente','cancelado') DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_financeiro_paciente` (`paciente_id`),
  KEY `fk_financeiro_convenio` (`convenio_id`),
  CONSTRAINT `fk_financeiro_convenio` FOREIGN KEY (`convenio_id`) REFERENCES `convenio` (`id`) ON DELETE SET NULL,
  CONSTRAINT `fk_financeiro_paciente` FOREIGN KEY (`paciente_id`) REFERENCES `Paciente` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `funcionario`
--

DROP TABLE IF EXISTS `funcionario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `funcionario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` tinytext DEFAULT NULL,
  `cpf` char(11) DEFAULT NULL,
  `cargo` enum('enfermeiro','técnico','recepcionista') DEFAULT NULL,
  `setor_id` int(11) DEFAULT NULL,
  `telefone` char(9) DEFAULT NULL,
  `email` tinytext DEFAULT NULL,
  `data_contratacao` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_funcionario_setor` (`setor_id`),
  CONSTRAINT `fk_funcionario_setor` FOREIGN KEY (`setor_id`) REFERENCES `setor` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `internacao`
--

DROP TABLE IF EXISTS `internacao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `internacao` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `paciente_id` int(11) DEFAULT NULL,
  `medico_id` int(11) DEFAULT NULL,
  `leito_id` int(11) DEFAULT NULL,
  `data_entrada` date DEFAULT NULL,
  `status` enum('em andamento','alta','obito') DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_internacao_paciente` (`paciente_id`),
  KEY `fk_internacao_medico` (`medico_id`),
  KEY `fk_internacao_leito` (`leito_id`),
  CONSTRAINT `fk_internacao_leito` FOREIGN KEY (`leito_id`) REFERENCES `leito` (`id`) ON DELETE SET NULL,
  CONSTRAINT `fk_internacao_medico` FOREIGN KEY (`medico_id`) REFERENCES `Medico` (`id`) ON DELETE SET NULL,
  CONSTRAINT `fk_internacao_paciente` FOREIGN KEY (`paciente_id`) REFERENCES `Paciente` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `leito`
--

DROP TABLE IF EXISTS `leito`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `leito` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `numero_leito` varchar(30) DEFAULT NULL,
  `setor_id` int(11) DEFAULT NULL,
  `tipo` enum('Enfermaria','Apartamento','UTI Adulto','UTI Neonatal','UTI Pediátrica') DEFAULT NULL,
  `status` enum('disponivel','ocupado') DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_setor` (`setor_id`),
  CONSTRAINT `fk_setor` FOREIGN KEY (`setor_id`) REFERENCES `setor` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `medicamento`
--

DROP TABLE IF EXISTS `medicamento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medicamento` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(30) DEFAULT NULL,
  `descricao` varchar(30) DEFAULT NULL,
  `fabricante` text DEFAULT NULL,
  `validade` date DEFAULT NULL,
  `quantidade_estoque` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `prescricao`
--

DROP TABLE IF EXISTS `prescricao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prescricao` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `paciente_id` int(11) DEFAULT NULL,
  `medico_id` int(11) DEFAULT NULL,
  `data_prescricao` date DEFAULT NULL,
  `medicamento_id` int(11) DEFAULT NULL,
  `dosagem` int(11) DEFAULT NULL,
  `frequencia` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_precricao_medico` (`medico_id`),
  KEY `fk_precricao_paciente` (`paciente_id`),
  KEY `fk_precricao_medicamento` (`medicamento_id`),
  CONSTRAINT `fk_precricao_medicamento` FOREIGN KEY (`medicamento_id`) REFERENCES `medicamento` (`id`) ON DELETE SET NULL,
  CONSTRAINT `fk_precricao_medico` FOREIGN KEY (`medico_id`) REFERENCES `Medico` (`id`) ON DELETE SET NULL,
  CONSTRAINT `fk_precricao_paciente` FOREIGN KEY (`paciente_id`) REFERENCES `Paciente` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `setor`
--

DROP TABLE IF EXISTS `setor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `setor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) DEFAULT NULL,
  `andar` int(11) DEFAULT NULL,
  `capacidade` int(11) DEFAULT NULL,
  `responsavel` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping events for database 'HospitalSaoLucas'
--

--
-- Dumping routines for database 'HospitalSaoLucas'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-10-01 20:08:15
