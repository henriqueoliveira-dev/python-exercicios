"""Conteúdo extraído de: 08_GEST_O_E_EXECU_O_DE_LOG.ipynb_1TkwtV39.ipynb
Célula original: 15
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

def custom_logger(level, message):
  import logging
  logger = logging.getLogger(__name__)
  if not (len(logger.handlers)):
    logging.basicConfig(level=logging.INFO)
    C_handler = logging.StreamHandler()
    f_handler = logging.FileHandler("file.log")
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    C_handler.setFormatter(formatter)
    f_handler.setFormatter(formatter)
    logger.addHandler(C_handler)
    logger.addHandler(f_handler)

  level = level.lower()
  if level == 'debug':
    logger.debug(message)
  elif level == 'info':
    logger.info(message)
  elif level == 'warning':
    logger.warning(message)
  elif level == 'error':
    logger.error(message)
  else:
    logger.critical(message)

custom_logger("error","Ateção, parametro errado!")
