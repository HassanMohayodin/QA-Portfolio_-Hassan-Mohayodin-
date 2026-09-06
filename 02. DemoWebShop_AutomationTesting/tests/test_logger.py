from utils.logger import get_logger


def test_logger():

    logger = get_logger(__name__)

    logger.info("Logger test started")

    assert True

    logger.info("Logger test completed")